from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from ciphercore.app_config import DB_PATH
from ciphercore.utils import now_iso


@dataclass
class VaultRecord:
    id: int | None
    title: str
    category: str
    username: str
    secret: str
    notes: str
    created_at: str | None = None
    updated_at: str | None = None


class VaultStorage:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self._bootstrap()

    def _bootstrap(self) -> None:
        self.conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS vault_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                username TEXT NOT NULL,
                secret TEXT NOT NULL,
                notes TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            '''
        )
        self.conn.commit()

    def upsert(self, record: VaultRecord) -> int:
        ts = now_iso()
        if record.id is None:
            cur = self.conn.execute(
                '''
                INSERT INTO vault_entries (title, category, username, secret, notes, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (record.title, record.category, record.username, record.secret, record.notes, ts, ts),
            )
            self.conn.commit()
            return int(cur.lastrowid)
        self.conn.execute(
            '''
            UPDATE vault_entries
               SET title = ?, category = ?, username = ?, secret = ?, notes = ?, updated_at = ?
             WHERE id = ?
            ''',
            (record.title, record.category, record.username, record.secret, record.notes, ts, record.id),
        )
        self.conn.commit()
        return int(record.id)

    def delete(self, record_id: int) -> None:
        self.conn.execute('DELETE FROM vault_entries WHERE id = ?', (record_id,))
        self.conn.commit()

    def list_records(self, search: str = '') -> List[sqlite3.Row]:
        if search:
            term = f'%{search.lower()}%'
            cur = self.conn.execute(
                '''
                SELECT * FROM vault_entries
                 WHERE lower(title) LIKE ? OR lower(category) LIKE ? OR lower(username) LIKE ?
                 ORDER BY updated_at DESC
                ''',
                (term, term, term),
            )
        else:
            cur = self.conn.execute('SELECT * FROM vault_entries ORDER BY updated_at DESC')
        return list(cur.fetchall())

    def get(self, record_id: int) -> Optional[sqlite3.Row]:
        cur = self.conn.execute('SELECT * FROM vault_entries WHERE id = ?', (record_id,))
        return cur.fetchone()

    def count(self) -> int:
        cur = self.conn.execute('SELECT COUNT(*) AS cnt FROM vault_entries')
        return int(cur.fetchone()['cnt'])
