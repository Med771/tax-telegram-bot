from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon


class AddFilter:
    @classmethod
    @TelegramDecorator.log_call()
    async def add_filter(cls, message: Message):
        is_btn = message.text == MenuLexicon.ADDONS_BTN_TEXT

        return is_btn
