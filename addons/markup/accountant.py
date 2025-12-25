from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon, AccountantLexicon

from data.accounting import AccountingData
from data.extract import ExtractData

BACK_TO_MENU_BTN = KeyboardButton(text=MenuLexicon.BACK_MENU_BTN_TEXT)

BACK_TO_DOCS_BTN = KeyboardButton(
    text=AccountantLexicon.BACK_TO_DOCS_BTN_TEXT)

BACK_TO_TYPE_BTN = KeyboardButton(
    text=AccountantLexicon.BACK_TO_TYPE_BTN_TEXT)

BACK_TO_ACCOUNTANT_BTN = KeyboardButton(
    text=AccountantLexicon.BACK_TO_ACCOUNTANT_BTN_TEXT)

BACK_TO_EXTRACT_COUNTER_BTN = KeyboardButton(
    text=AccountantLexicon.BACK_TO_EXTRACT_COUNTER_BTN_TEXT)

YES_ACCOUNTANT_BTN = KeyboardButton(
    text=AccountantLexicon.YES_ACCOUNTANT_BTN_TEXT)
NO_ACCOUNTANT_BTN = KeyboardButton(
    text=AccountantLexicon.NO_ACCOUNTANT_BTN_TEXT)

BACK_TO_MENU_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[BACK_TO_MENU_BTN]],
    resize_keyboard=True)

ACCOUNTANT_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[YES_ACCOUNTANT_BTN], [NO_ACCOUNTANT_BTN], [BACK_TO_TYPE_BTN], [BACK_TO_MENU_BTN]],
    resize_keyboard=True)

RES_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[BACK_TO_EXTRACT_COUNTER_BTN], [BACK_TO_MENU_BTN]],
    resize_keyboard=True
)


class AccountantMarkup:
    back_markup: ReplyKeyboardMarkup = BACK_TO_MENU_MARKUP
    account_markup: ReplyKeyboardMarkup = ACCOUNTANT_MARKUP
    res_markup: ReplyKeyboardMarkup = RES_MARKUP

    @classmethod
    @TelegramDecorator.log_call()
    async def get_types(cls) -> ReplyKeyboardMarkup:
        data = await AccountingData.get_types()

        keyboard = []

        for account in data:
            keyboard.append([KeyboardButton(text=account)])

        keyboard.append([BACK_TO_DOCS_BTN])
        keyboard.append([BACK_TO_MENU_BTN])

        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    @classmethod
    @TelegramDecorator.log_call()
    async def get_extracts(cls) -> ReplyKeyboardMarkup:
        data = await ExtractData.get_extracts()

        keyboard = []

        for account in data:
            keyboard.append([KeyboardButton(text="До " + str(account))])

        keyboard.append([BACK_TO_TYPE_BTN])
        keyboard.append([BACK_TO_MENU_BTN])

        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
