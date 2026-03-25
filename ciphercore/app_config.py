from __future__ import annotations
from pathlib import Path
from ciphercore import APP_NAME

APP_DIR = Path.home() / f'.{APP_NAME.lower().replace(" ", "_")}'
APP_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR = APP_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR = APP_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / 'vault.db'
STATE_PATH = DATA_DIR / 'app_state.json'
LOG_PATH = LOG_DIR / 'activity.log'
SUPPORTED_FILE_SUFFIX = '.ccore'
PBKDF2_ITERATIONS = 600_000
DEFAULT_LANGUAGE = 'de'
SOCIAL_LINKS = {
    'GitHub': 'https://github.com/bylickilabs',
    'Website': 'https://www.bylickilabs.de',
    'YouTube': 'https://www.youtube.com/@NextLevelScripts',
    'LinkedIn': '',
    'Email': 'mailto:thorsten.bylicki@web.de',
}
