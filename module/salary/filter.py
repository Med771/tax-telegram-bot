from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import SalaryLexicon
from addons.markup import SalaryMarkup
from addons.state import AccountantState, SalaryState
from tools.admin import AdminTools


class SalaryFilter:
    @classmethod
    @TelegramDecorator.log_call()
    async def salary_filter(cls, message: Message, state: FSMContext):
        is_btn = message.text == SalaryLexicon.SALARY_BTN_TEXT
        is_state = await AdminTools.get_state(state=state) == AccountantState.RES_STATE

        return is_btn and is_state

    @classmethod
    @TelegramDecorator.log_call()
    async def empl_filter(cls, message: Message, state: FSMContext):
        is_dig = message.text.isdigit()
        is_state = await AdminTools.get_state(state=state) == SalaryState.EMPL_STATE

        if not is_state:
            return False

        if not is_dig:
            await message.answer(text=SalaryLexicon.EMPL_ERROR_MSG, reply_markup=SalaryMarkup.res_markup)

            return False

        return True

    @classmethod
    @TelegramDecorator.log_call()
    async def white_filter(cls, message: Message, state: FSMContext):
        is_btn = message.text == SalaryLexicon.YES_WHITE_BTN_TEXT or message.text == SalaryLexicon.NO_WHITE_BTN_TEXT
        is_state = await AdminTools.get_state(state=state) == SalaryState.WHITE_STATE

        if not is_state:
            return False

        if not is_btn:
            await message.answer(text=SalaryLexicon.WHITE_ERROR_MSG, reply_markup=SalaryMarkup.type_markup)

            return False

        return True
