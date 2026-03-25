from __future__ import annotations
import webbrowser
from ciphercore.app_config import SOCIAL_LINKS


def open_social(name: str) -> None:
    url = SOCIAL_LINKS.get(name)
    if url:
        webbrowser.open(url)
