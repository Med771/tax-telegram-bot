from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon
from addons.markup import MenuMarkup

from tools.admin import AdminTools


class MenuService:
    @classmethod
    @TelegramDecorator.log_call()
    async def start_command(cls, message: Message, state: FSMContext):
        await state.clear()

        await message.answer(
            text=MenuLexicon.START_MSG,
            reply_markup=MenuMarkup.start_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def back_inl_btn(cls, callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.clear()

        await callback.message.answer(
            text=MenuLexicon.START_MSG,
            reply_markup=MenuMarkup.start_markup)
