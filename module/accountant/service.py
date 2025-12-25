from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import AccountantLexicon
from addons.markup import AccountantMarkup
from addons.state import AccountantState

from data.accounting import AccountingData

from tools.admin import AdminTools


class AccountantService:
    @classmethod
    @TelegramDecorator.log_call()
    async def accountant_btn(cls, message: Message, state: FSMContext):
        await state.set_state(AccountantState.DOCS_STATE)
        await state.set_data({
            "docs": 0,
            "_type": "",
            "docs_sum": 0,
        })

        await message.answer(
            text=AccountantLexicon.DOCS_COUNTER_MSG,
            reply_markup=AccountantMarkup.back_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def docs_msg(cls, message: Message, state: FSMContext):
        await state.set_state(AccountantState.TYPE_STATE)
        await state.update_data(docs=int(message.text))

        await message.answer(
            text=(
                AccountantLexicon.TYPE_MSG +
                AccountantLexicon.RESULT_MSG +
                AccountantLexicon.DOCS_RESULT_MSG.format(docs=int(message.text))),
            reply_markup=await AccountantMarkup.get_types())

    @classmethod
    @TelegramDecorator.log_call()
    async def type_btn(cls, message: Message, state: FSMContext):
        val = await AccountingData.get_data_by_type(message.text)
        data = await state.get_data()

        docs = data.get("docs", 0)
        accountant = val.get("accountant", 0)

        if docs < 501:
            key = "200-500"
        elif docs < 1001:
            key = "500-1000"
        elif docs < 1501:
            key = "1000-1500"
        else:
            key = "1500-2000"

        price = val.get(key, 0)

        total = accountant + (((docs + 99) // 100) - 1) * price

        await state.set_state(AccountantState.EXTRACT_STATE)

        await message.answer(
            text=(
                    AccountantLexicon.RESULT_MSG +
                    AccountantLexicon.DOCS_RESULT_MSG.format(docs=docs) +
                    AccountantLexicon.TYPE_RESULT_MSG.format(type=message.text) +
                    AccountantLexicon.TOTAL_MSG.format(total=total)),
            reply_markup=AccountantMarkup.res_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def back_btn(cls, message: Message, state: FSMContext):
        _state = await AdminTools.get_state(state=state)

        if _state == AccountantState.RES_STATE:
            await state.set_state(AccountantState.TYPE_STATE)

            await message.answer(
                text=AccountantLexicon.TYPE_MSG,
                reply_markup=await AccountantMarkup.get_types())
        elif _state == AccountantState.TYPE_STATE:
            await state.set_state(AccountantState.DOCS_STATE)

            await message.answer(
                text=AccountantLexicon.DOCS_COUNTER_MSG,
                reply_markup=AccountantMarkup.back_markup)
