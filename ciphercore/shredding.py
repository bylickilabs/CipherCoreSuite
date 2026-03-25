from __future__ import annotations
import os
from pathlib import Path


def shred_file(path: Path, passes: int = 3) -> None:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(str(path))
    length = path.stat().st_size
    if length == 0:
        path.unlink(missing_ok=True)
        return
    with path.open('r+b') as fh:
        for _ in range(max(1, passes)):
            fh.seek(0)
            remaining = length
            chunk = 1024 * 1024
            while remaining > 0:
                size = min(chunk, remaining)
                fh.write(os.urandom(size))
                remaining -= size
            fh.flush()
            os.fsync(fh.fileno())
    path.unlink(missing_ok=True)
