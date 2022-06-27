import json
from os import getenv, makedirs
from pathlib import Path



PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / "config/config.json"

config: dict = json.loads(CONFIG_PATH.read_text())
config.setdefault("env", getenv("env"))
all_path_config_values = [Path(v) for k, v in config.items() if "path" in k.lower()]
for path in all_path_config_values:
    if not path.exists():
        makedirs(path)