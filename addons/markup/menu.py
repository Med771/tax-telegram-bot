from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from addons.lexicon import MenuLexicon


CALCULATE_BTN = KeyboardButton(text=MenuLexicon.CALCULATE_BTN_TEXT)

START_MARKUP = ReplyKeyboardMarkup(
    keyboard=[
        [CALCULATE_BTN],
    ],
    resize_keyboard=True,
)


class MenuMarkup:
    start_markup: ReplyKeyboardMarkup = START_MARKUP


