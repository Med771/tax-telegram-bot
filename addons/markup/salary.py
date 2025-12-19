from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from addons.lexicon import MenuLexicon, SalaryLexicon, AccountantLexicon

YES_WHITE_BTN = KeyboardButton(text=SalaryLexicon.YES_WHITE_BTN_TEXT)
NO_WHITE_BTN = KeyboardButton(text=SalaryLexicon.NO_WHITE_BTN_TEXT)

BACK_TO_MENU_BTN = KeyboardButton(text=MenuLexicon.BACK_MENU_BTN_TEXT)

BACK_TO_RES_BTN = KeyboardButton(text=AccountantLexicon.BACK_TO_RES_BTN_TEXT)

BACK_TO_EMPL_BTN = KeyboardButton(text=SalaryLexicon.BACK_TO_EMPL_BTN_TEXT)
BACK_TO_TYPE_BTN = KeyboardButton(text=SalaryLexicon.BACK_TO_TYPE_BTN_TEXT)

EMPL_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[BACK_TO_RES_BTN], [BACK_TO_MENU_BTN]],
    resize_keyboard=True)

TYPE_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[YES_WHITE_BTN], [NO_WHITE_BTN], [BACK_TO_EMPL_BTN], [BACK_TO_MENU_BTN]],
    resize_keyboard=True)

RES_MARKUP = ReplyKeyboardMarkup(
    keyboard=[[BACK_TO_TYPE_BTN], [BACK_TO_MENU_BTN]],
    resize_keyboard=True)


class SalaryMarkup:
    empl_markup: ReplyKeyboardMarkup = EMPL_MARKUP
    type_markup: ReplyKeyboardMarkup = TYPE_MARKUP
    res_markup: ReplyKeyboardMarkup = RES_MARKUP
