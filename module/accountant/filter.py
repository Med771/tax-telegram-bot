from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon, AccountantLexicon
from addons.markup import AccountantMarkup
from addons.state import AccountantState
from addons.state.salary import SalaryState

from data.accounting import AccountingData
from data.extract import ExtractData

from tools.admin import AdminTools


class AccountantFilter:

    @classmethod
    @TelegramDecorator.log_call()
    async def back_filter(cls, message: Message, state: FSMContext):
        _state = await AdminTools.get_state(state)

        is_empl = message.text == AccountantLexicon.BACK_TO_RES_BTN_TEXT and _state == SalaryState.EMPL_STATE
        is_ex = message.text == AccountantLexicon.BACK_TO_EXTRACT_COUNTER_BTN_TEXT and _state == AccountantState.RES_STATE
        # is_acc = message.text == AccountantLexicon.BACK_TO_ACCOUNTANT_BTN_TEXT and _state == AccountantState.EXTRACT_STATE
        is_type = message.text == AccountantLexicon.BACK_TO_TYPE_BTN_TEXT and _state == AccountantState.EXTRACT_STATE
        is_docs = message.text == AccountantLexicon.BACK_TO_DOCS_BTN_TEXT and _state == AccountantState.TYPE_STATE

        return is_empl or is_ex or is_type or is_docs

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

    # @classmethod
    # @TelegramDecorator.log_call()
    # async def account_filter(cls, message: Message, state: FSMContext):
    #     is_account = message.text in AccountantLexicon.ACCOUNTANT_TUP
    #     is_state = await AdminTools.get_state(state) == AccountantState.ACCOUNT_STATE
    #
    #     if not is_state:
    #         return False
    #
    #     if message.text == AccountantLexicon.BACK_TO_TYPE_BTN_TEXT:
    #         return False
    #
    #     if not is_account:
    #         await message.answer(text=AccountantLexicon.ACCOUNTANT_ERROR_MSG, reply_markup=AccountantMarkup.account_markup)
    #
    #         return False
    #
    #     return True

    @classmethod
    @TelegramDecorator.log_call()
    async def extract_filter(cls, message: Message, state: FSMContext):
        is_extract = False

        for extract in await ExtractData.get_extracts():
            if "До " + str(extract) == message.text:
                is_extract = True

                break

        is_state = await AdminTools.get_state(state) == AccountantState.EXTRACT_STATE

        if not is_state:
            return False

        if message.text == AccountantLexicon.BACK_TO_ACCOUNTANT_BTN_TEXT:
            return False

        if not is_extract:
            await message.answer(text=AccountantLexicon.EXTRACT_ERROR_MSG, reply_markup=await AccountantMarkup.get_extracts())

            return False

        return True