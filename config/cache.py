import os

from dotenv import load_dotenv

from config.main import MainConfig


class CacheConfig:
    load_dotenv(dotenv_path=MainConfig.MAIN_ENV_PATH)

    CACHE_FOLDER_NAME: str = os.getenv("CACHE_FOLDER_NAME")

    EXTRACT_FILE_NAME: str = os.getenv("EXTRACT_FILE_NAME")
    WITHOUT_SALARY_FILE_NAME: str = os.getenv("WITHOUT_SALARY_FILE_NAME")
    WITH_SALARY_FILE_NAME: str = os.getenv("WITH_SALARY_FILE_NAME")
    ACCOUNTING_FILE_NAME: str = os.getenv("ACCOUNTING_FILE_NAME")

    EXTRACT_RANGE: str = os.getenv("EXTRACT_RANGE")
    WITHOUT_RANGE: str = os.getenv("WITHOUT_RANGE")
    WITH_RANGE: str = os.getenv("WITH_RANGE")
    ACCOUNTING_RANGE: str = os.getenv("ACCOUNTING_RANGE")

    if not CACHE_FOLDER_NAME:
        exit("Cache folder name environment variable not set")

    if not EXTRACT_FILE_NAME:
        exit("Extract file name environment variable not set")

    if not WITHOUT_SALARY_FILE_NAME:
        exit("Without salary name environment variable not set")

    if not WITH_SALARY_FILE_NAME:
        exit("With salary name environment variable not set")

    if not ACCOUNTING_FILE_NAME:
        exit("Accounting name environment variable not set")

    CACHE_PATH = MainConfig.MAIN_PATH.joinpath(CACHE_FOLDER_NAME)

    if not CACHE_PATH.exists():
        CACHE_PATH.mkdir(parents=True)

    EXTRACT_PATH = CACHE_PATH.joinpath(EXTRACT_FILE_NAME)
    WITHOUT_PATH = CACHE_PATH.joinpath(WITHOUT_SALARY_FILE_NAME)
    WITH_PATH = CACHE_PATH.joinpath(WITH_SALARY_FILE_NAME)
    ACCOUNTING_PATH = CACHE_PATH.joinpath(ACCOUNTING_FILE_NAME)

    try:
        _arr: list[str] = EXTRACT_RANGE.split(':')
        extract_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        extract_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        EXTRACT_RANGE_TUP = (extract_cols[0], extract_cols[1], extract_rows[0], extract_rows[1])
    except ValueError:
        exit("Invalid extract range")

    try:
        _arr: list[str] = WITHOUT_RANGE.split(':')
        without_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        without_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        WITHOUT_RANGE_TUP = (without_cols[0], without_cols[1], without_rows[0], without_rows[1])
    except ValueError:
        exit("Invalid without range")

    try:
        _arr: list[str] = WITH_RANGE.split(':')
        with_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        with_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        WITH_RANGE_TUP = (with_cols[0], with_cols[1], with_rows[0], with_rows[1])
    except ValueError:
        exit("Invalid with range")

    try:
        _arr: list[str] = ACCOUNTING_RANGE.split(':')
        accounting_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        accounting_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        ACCOUNTING_RANGE_TUP = (accounting_cols[0], accounting_cols[1], accounting_rows[0], accounting_rows[1])
    except ValueError:
        exit("Invalid accounting range")
