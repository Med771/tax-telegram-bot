from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from addons.lexicon import MenuLexicon

BACK_TO_MENU_BTN = KeyboardButton(text=MenuLexicon.BACK_MENU_BTN_TEXT)

BACK_TO_MENU_MARKUP = ReplyKeyboardMarkup(keyboard=[[BACK_TO_MENU_BTN]], resize_keyboard=True)


class AddMarkup:
    menu_markup: ReplyKeyboardMarkup = BACK_TO_MENU_MARKUP
