import os

import gspread

from gspread import Client, Spreadsheet, Worksheet

from dotenv import load_dotenv

from config.main import MainConfig


class GoogleConfig:
    load_dotenv(dotenv_path=MainConfig.MAIN_ENV_PATH)

    GOOGLE_CREDS_PATH: str = os.getenv('GOOGLE_CREDS_PATH')
    SPREADSHEET_ID: str = os.getenv('SPREADSHEET_ID')
    SCOPE_SHEET: str = os.getenv('SCOPE_SHEET')
    LIST_NAME: str = os.getenv('LIST_NAME')

    if not GOOGLE_CREDS_PATH:
        exit('GOOGLE_CREDS_PATH environment variable not set')

    if not SPREADSHEET_ID:
        exit('SPREADSHEET_ID environment variable not set')

    if not SCOPE_SHEET:
        exit('SCOPE_SHEET environment variable not set')

    if not LIST_NAME:
        exit('LIST_NAME environment variable not set')

    try:
        CLIENT: Client = gspread.service_account(filename=GOOGLE_CREDS_PATH, scopes=[SCOPE_SHEET])
        TABLE: Spreadsheet = CLIENT.open_by_key(SPREADSHEET_ID)
    except gspread.exceptions.APIError:
        exit('Google connected to Google spreadsheet not found')

    try:
        WS: Worksheet = TABLE.worksheet(LIST_NAME)
    except gspread.exceptions.APIError:
        exit('Google connected to Google worksheet not found')
