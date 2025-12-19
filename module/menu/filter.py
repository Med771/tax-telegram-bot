from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon


class MenuFilter:
    @classmethod
    @TelegramDecorator.log_call()
    async def back_btn(cls, message: Message, state: FSMContext):
        return message.text == MenuLexicon.BACK_MENU_BTN_TEXT

    @classmethod
    @TelegramDecorator.log_call()
    async def back_inl_btn(cls, callback: CallbackQuery, state: FSMContext):
        return callback.data == MenuLexicon.BACK_MENU_BTN_CALL