from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon, AccountantLexicon
from addons.markup import AccountantMarkup
from addons.state import AccountantState

from data.accounting import AccountingData

from tools.admin import AdminTools


class AccountantFilter:

    @classmethod
    @TelegramDecorator.log_call()
    async def back_filter(cls, message: Message, state: FSMContext):
        _state = await AdminTools.get_state(state)

        is_type = message.text == AccountantLexicon.BACK_TO_TYPE_BTN_TEXT and _state == AccountantState.RES_STATE
        is_docs = message.text == AccountantLexicon.BACK_TO_DOCS_BTN_TEXT and _state == AccountantState.TYPE_STATE

        return is_type or is_docs

    @classmethod
    @TelegramDecorator.log_call()
    async def accountant_filter(cls, message: Message, state: FSMContext):
        return message.text == MenuLexicon.CALCULATE_BTN_TEXT

    @classmethod
    @TelegramDecorator.log_call()
    async def docs_filter(cls, message: Message, state: FSMContext):
        is_dig = message.text.isdigit()
        is_state = await AdminTools.get_state(state) == AccountantState.DOCS_STATE

        if not is_state:
            return False

        if not is_dig or int(message.text) < 200 or int(message.text) > 2000:
            await message.answer(text=AccountantLexicon.DOCS_ERROR_MSG, reply_markup=AccountantMarkup.back_markup)

            return False

        return True

    @classmethod
    @TelegramDecorator.log_call()
    async def type_filter(cls, message: Message, state: FSMContext):
        is_type = message.text in await AccountingData.get_types()
        is_state = await AdminTools.get_state(state) == AccountantState.TYPE_STATE

        if not is_state:
            return False

        if message.text == AccountantLexicon.BACK_TO_DOCS_BTN_TEXT:
            return False

        if not is_type:
            await message.answer(text=AccountantLexicon.TYPE_ERROR_MSG, reply_markup=await AccountantMarkup.get_types())

            return False

        return True
