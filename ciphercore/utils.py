from __future__ import annotations
import json
import hashlib
import os
from pathlib import Path
from datetime import datetime
from typing import Any
from ciphercore.app_config import LOG_PATH, STATE_PATH, DEFAULT_LANGUAGE


def now_iso() -> str:
    return datetime.now().isoformat(timespec='seconds')


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def append_log(message: str) -> None:
    ensure_parent(LOG_PATH)
    with LOG_PATH.open('a', encoding='utf-8') as fh:
        fh.write(f'[{now_iso()}] {message}\n')


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def human_size(size: int) -> str:
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    value = float(size)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f'{value:.2f} {units[idx]}'


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {'language': DEFAULT_LANGUAGE}
    try:
        return json.loads(STATE_PATH.read_text(encoding='utf-8'))
    except Exception:
        return {'language': DEFAULT_LANGUAGE}


def save_state(data: dict[str, Any]) -> None:
    ensure_parent(STATE_PATH)
    STATE_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def secure_compare(a: bytes, b: bytes) -> bool:
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= x ^ y
    return result == 0


def random_bytes(length: int) -> bytes:
    return os.urandom(length)
