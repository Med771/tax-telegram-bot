import os

from pathlib import Path

from dotenv import load_dotenv


class MainConfig:
    MAIN_PATH = Path(__file__).parent.parent
    MAIN_ENV_PATH = MAIN_PATH / ".env"

    load_dotenv(dotenv_path=MAIN_ENV_PATH)

    IS_DROPPED_TABLE: bool = bool(int(os.getenv("IS_DROPPED_TABLE", "0")))
    IS_CREATED_TABLE: bool = bool(int(os.getenv("IS_CREATED_TABLE", "0")))

    if IS_DROPPED_TABLE is None:
        exit("IS_DROPPED_TABLE environment variable not set")

    if IS_CREATED_TABLE is None:
        exit("IS_CREATED_TABLE environment variable not set")
