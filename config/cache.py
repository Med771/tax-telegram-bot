import os

from dotenv import load_dotenv

from config.main import MainConfig


class CacheConfig:
    load_dotenv(dotenv_path=MainConfig.MAIN_ENV_PATH)

    CACHE_FOLDER_NAME: str = os.getenv("CACHE_FOLDER_NAME")

    SALARY_FILE_NAME: str = os.getenv("SALARY_FILE_NAME")
    ACCOUNTING_FILE_NAME: str = os.getenv("ACCOUNTING_FILE_NAME")
    EXTRACT_FILE_NAME: str = os.getenv("EXTRACT_FILE_NAME")

    SALARY_RANGE_STR: str = os.getenv("SALARY_RANGE")
    ACCOUNTING_RANGE_STR: str = os.getenv("ACCOUNTING_RANGE")
    EXTRACT_RANGE_STR: str = os.getenv("EXTRACT_RANGE")

    FIRST_PHOTO_PATH: str = os.getenv("FIRST_PHOTO_PATH")
    SECOND_PHOTO_PATH: str = os.getenv("SECOND_PHOTO_PATH")

    if not CACHE_FOLDER_NAME:
        exit("Cache folder name environment variable not set")

    if not EXTRACT_FILE_NAME:
        exit("Extract file name environment variable not set")

    if not SALARY_FILE_NAME:
        exit("Salary name environment variable not set")

    if not ACCOUNTING_FILE_NAME:
        exit("Accounting name environment variable not set")

    if not FIRST_PHOTO_PATH:
        exit("First photo path environment variable not set")

    if not SECOND_PHOTO_PATH:
        exit("Second photo path environment variable not set")

    CACHE_PATH = MainConfig.MAIN_PATH.joinpath(CACHE_FOLDER_NAME)

    if not CACHE_PATH.exists():
        CACHE_PATH.mkdir(parents=True)

    EXTRACT_PATH = CACHE_PATH.joinpath(EXTRACT_FILE_NAME)
    SALARY_PATH = CACHE_PATH.joinpath(SALARY_FILE_NAME)
    ACCOUNTING_PATH = CACHE_PATH.joinpath(ACCOUNTING_FILE_NAME)

    try:
        _arr: list[str] = SALARY_RANGE_STR.split(':')
        salary_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        salary_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        SALARY_RANGE = (salary_cols[0], salary_cols[1], salary_rows[0], salary_rows[1])
    except TypeError:
        exit("Salary range environment variable not set")

    try:
        _arr: list[str] = ACCOUNTING_RANGE_STR.split(':')
        account_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        account_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        ACCOUNTING_RANGE = (account_cols[0], account_cols[1], account_rows[0], account_rows[1])
    except TypeError:
        exit("Accounting range environment variable not set")

    try:
        _arr: list[str] = EXTRACT_RANGE_STR.split(':')
        extract_cols = int(_arr[0].split("-")[0]), int(_arr[0].split("-")[1])
        extract_rows = int(_arr[1].split("-")[0]), int(_arr[1].split("-")[1])

        EXTRACT_RANGE = (extract_cols[0], extract_cols[1], extract_rows[0], extract_rows[1])
    except TypeError:
        exit("Extract range environment variable not set")
