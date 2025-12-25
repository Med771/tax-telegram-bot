from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from addons.lexicon import MenuLexicon


CALCULATE_BTN = KeyboardButton(text=MenuLexicon.CALCULATE_BTN_TEXT)
SALARY_BTN = KeyboardButton(text=MenuLexicon.SALARY_BTN_TEXT)
ADDONS_BTN = KeyboardButton(text=MenuLexicon.ADDONS_BTN_TEXT)

START_MARKUP = ReplyKeyboardMarkup(
    keyboard=[
        [CALCULATE_BTN],
        [SALARY_BTN],
        [ADDONS_BTN]
    ],
    resize_keyboard=True,
)


class MenuMarkup:
    start_markup: ReplyKeyboardMarkup = START_MARKUP


