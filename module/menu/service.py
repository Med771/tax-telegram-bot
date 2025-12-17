from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon
from addons.markup import MenuMarkup


class MenuService:
    @classmethod
    @TelegramDecorator.log_call()
    async def start_command(cls, message: Message, state: FSMContext):
        await state.clear()

        await message.answer(
            text=MenuLexicon.START_MSG,
            reply_markup=MenuMarkup.start_markup)