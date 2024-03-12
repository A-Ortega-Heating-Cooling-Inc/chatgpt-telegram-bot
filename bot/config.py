import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

telegram_token = dotenv.dotenv_values(config_dir / "config.env")["TELEGRAM_TOKEN"]