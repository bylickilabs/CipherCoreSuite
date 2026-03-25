from __future__ import annotations

import base64
import json
import mimetypes
import hmac
from pathlib import Path
from typing import Tuple

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from ciphercore.app_config import PBKDF2_ITERATIONS, SUPPORTED_FILE_SUFFIX
from ciphercore.utils import random_bytes, sha256_hex


HEADER_MAGIC = "CCORE1"


def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive a Fernet compatible key from a password and salt.
    Returns URL safe base64 encoded bytes suitable for Fernet.
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non empty string.")

    if not isinstance(salt, bytes) or not salt:
        raise ValueError("Salt must be non empty bytes.")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))


def build_payload(password: str, data: bytes, metadata: dict | None = None) -> str:
    """
    Build a portable encrypted JSON payload for text or file content.
    """
    if not isinstance(data, bytes):
        raise ValueError("Data must be bytes.")

    salt = random_bytes(16)
    key = derive_key(password, salt)
    token = Fernet(key).encrypt(data)

    payload = {
        "magic": HEADER_MAGIC,
        "salt": base64.b64encode(salt).decode("ascii"),
        "token": token.decode("ascii"),
        "metadata": metadata or {},
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def read_payload(password: str, payload_text: str) -> Tuple[bytes, dict]:
    """
    Read and decrypt a JSON payload created by build_payload().
    """
    try:
        payload = json.loads(payload_text)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid payload format.") from exc

    if payload.get("magic") != HEADER_MAGIC:
        raise ValueError("Unsupported payload format.")

    try:
        salt_b64 = payload["salt"]
        token = payload["token"]
    except KeyError as exc:
        raise ValueError("Payload is missing required fields.") from exc

    try:
        salt = base64.b64decode(salt_b64)
    except Exception as exc:
        raise ValueError("Invalid payload salt.") from exc

    key = derive_key(password, salt)

    try:
        data = Fernet(key).decrypt(token.encode("ascii"))
    except InvalidToken as exc:
        raise ValueError("Invalid password or corrupted payload.") from exc

    return data, payload.get("metadata", {})


def encrypt_text(text: str, password: str) -> str:
    """
    Encrypt plain text into a JSON payload.
    """
    metadata = {
        "type": "text",
        "encoding": "utf-8",
    }
    return build_payload(password, text.encode("utf-8"), metadata)


def decrypt_text(payload_text: str, password: str) -> str:
    """
    Decrypt a text payload and return the original string.
    """
    data, metadata = read_payload(password, payload_text)
    encoding = metadata.get("encoding", "utf-8")
    return data.decode(encoding)


def encrypt_file(input_path: Path, output_dir: Path, password: str) -> Path:
    """
    Encrypt a file into the CipherCore payload format.
    """
    if not input_path.exists() or not input_path.is_file():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    raw = input_path.read_bytes()
    metadata = {
        "type": "file",
        "filename": input_path.name,
        "suffix": input_path.suffix,
        "mime": mimetypes.guess_type(str(input_path))[0] or "application/octet-stream",
        "size": len(raw),
        "sha256": sha256_hex(raw),
    }

    payload = build_payload(password, raw, metadata)
    target = output_dir / f"{input_path.name}{SUPPORTED_FILE_SUFFIX}"
    target.write_text(payload, encoding="utf-8")
    return target


def decrypt_file(input_path: Path, output_dir: Path, password: str) -> Path:
    """
    Decrypt a CipherCore payload file back into its original file.
    """
    if not input_path.exists() or not input_path.is_file():
        raise FileNotFoundError(f"Encrypted file not found: {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    payload_text = input_path.read_text(encoding="utf-8")
    raw, metadata = read_payload(password, payload_text)

    filename = metadata.get("filename") or input_path.stem
    target = output_dir / filename
    target.write_bytes(raw)
    return target


def create_password_hash(password: str) -> dict[str, str]:
    """
    Create master password metadata for local storage.

    Important:
    - salt is stored as standard base64 string
    - verifier stores the already Fernet compatible derived key as UTF 8 string
    """
    salt = random_bytes(16)
    key = derive_key(password, salt)

    return {
        "salt": base64.b64encode(salt).decode("ascii"),
        "verifier": key.decode("utf-8"),
    }


def verify_password(password: str, stored_salt_b64: str, stored_verifier: str) -> bool:
    """
    Verify a password against the stored salt and verifier.
    """
    try:
        salt = base64.b64decode(stored_salt_b64)
    except Exception:
        return False

    try:
        candidate = derive_key(password, salt).decode("utf-8")
    except Exception:
        return False

    return hmac.compare_digest(candidate, stored_verifier)


def make_session_fernet(password: str, stored_salt_b64: str) -> Fernet:
    """
    Create a Fernet instance for the unlocked session.
    """
    try:
        salt = base64.b64decode(stored_salt_b64)
    except Exception as exc:
        raise ValueError("Invalid stored salt.") from exc

    return Fernet(derive_key(password, salt))