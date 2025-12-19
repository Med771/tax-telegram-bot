from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import AccountantLexicon
from addons.markup import AccountantMarkup
from addons.state import AccountantState, SalaryState

from data.accounting import AccountingData
from data.extract import ExtractData

from tools.admin import AdminTools


class AccountantService:
    @classmethod
    @TelegramDecorator.log_call()
    async def accountant_btn(cls, message: Message, state: FSMContext):
        await state.set_state(AccountantState.DOCS_STATE)
        await state.set_data({
            "docs": 0,
            "_type": "",
            "ext": 0,
            "docs_sum": 0,
            "total": 0,
            "is_acc": False,
            "acc": "",
            "account": 0,
            "ex": "",
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
                AccountantLexicon.DOCS_RESULT_MSG.format(docs=int(message.text))
            ),
            reply_markup=await AccountantMarkup.get_types()
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def type_btn(cls, message: Message, state: FSMContext):
        val = await AccountingData.get_data_by_type(message.text)
        data = await state.get_data()

        amount = 0
        docs = data["docs"]

        for value in val["amounts"]:
            if value["cnt"] > docs:
                amount = value["price"]
                break

        await state.set_state(AccountantState.ACCOUNT_STATE)

        await state.update_data(_type=message.text)
        await state.update_data(docs_sum=amount)
        await state.update_data(total=amount)
        await state.update_data(account=val["account"])

        await message.answer(
            text=(
                    AccountantLexicon.ACCOUNTANT_MSG +
                    AccountantLexicon.RESULT_MSG +
                    AccountantLexicon.DOCS_RESULT_MSG.format(docs=data["docs"]) +
                    AccountantLexicon.TYPE_RESULT_MSG.format(type=message.text) +
                    AccountantLexicon.TOTAL_MSG.format(total=amount)
            ),
            reply_markup=AccountantMarkup.account_markup
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def account_btn(cls, message: Message, state: FSMContext):
        data = await state.get_data()

        docs_sum = data["docs_sum"]
        _type = data["_type"]
        account = data["account"]

        total = docs_sum

        if message.text == AccountantLexicon.YES_ACCOUNTANT_BTN_TEXT:
            total += account

            await state.update_data(is_acc=True)
            await state.update_data(total=total)

        await state.update_data(acc=message.text)

        await state.set_state(AccountantState.EXTRACT_STATE)

        await message.answer(
            text=(
                    AccountantLexicon.EXTRACT_COUNTER_MSG +
                    AccountantLexicon.RESULT_MSG +
                    AccountantLexicon.DOCS_RESULT_MSG.format(docs=data["docs"]) +
                    AccountantLexicon.TYPE_RESULT_MSG.format(type=_type) +
                    AccountantLexicon.ACCOUNTANT_RESULT_MSG.format(accountant=message.text) +
                    AccountantLexicon.TOTAL_MSG.format(total=total)
            ),
            reply_markup=await AccountantMarkup.get_extracts()
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def extract_btn(cls, message: Message, state: FSMContext):
        data = await state.get_data()
        extract = await ExtractData.get_data_by_cnt(int(message.text.split()[1]))

        docs = data["docs"]
        docs_sum = data["docs_sum"]
        _type = data["_type"]
        is_acc = data["is_acc"]
        acc = data["acc"]
        account = data["account"]
        ext = extract["price"]

        total = docs_sum + (account if is_acc else 0) + ext

        await state.update_data(ext=ext)
        await state.update_data(ex=message.text)
        await state.update_data(total=total)

        await state.set_state(AccountantState.RES_STATE)

        await message.answer(
            text= (
                    AccountantLexicon.RESULT_MSG +
                    AccountantLexicon.DOCS_RESULT_MSG.format(docs=docs) +
                    AccountantLexicon.TYPE_RESULT_MSG.format(type=_type) +
                    AccountantLexicon.ACCOUNTANT_RESULT_MSG.format(accountant=acc) +
                    AccountantLexicon.EXTRACT_RESULT_MSG.format(extract=message.text) +
                    AccountantLexicon.TOTAL_MSG.format(total=total)
            ),
            reply_markup=AccountantMarkup.res_markup
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def back_btn(cls, message: Message, state: FSMContext):
        _state = await AdminTools.get_state(state=state)

        if _state == SalaryState.EMPL_STATE:
            data = await state.get_data()

            await state.set_state(AccountantState.RES_STATE)

            docs = data["docs"]
            _type = data["_type"]
            acc = data["acc"]
            ex = data["ex"]
            total = data["total"]

            await message.answer(
                text=(
                        AccountantLexicon.RESULT_MSG +
                        AccountantLexicon.DOCS_RESULT_MSG.format(docs=docs) +
                        AccountantLexicon.TYPE_RESULT_MSG.format(type=_type) +
                        AccountantLexicon.ACCOUNTANT_RESULT_MSG.format(accountant=acc) +
                        AccountantLexicon.EXTRACT_RESULT_MSG.format(extract=ex) +
                        AccountantLexicon.TOTAL_MSG.format(total=total)
                ),
                reply_markup=AccountantMarkup.res_markup
            )
        elif _state == AccountantState.RES_STATE:
            await state.set_state(AccountantState.EXTRACT_STATE)

            await message.answer(
                text=AccountantLexicon.EXTRACT_COUNTER_MSG,
                reply_markup=await AccountantMarkup.get_extracts()
            )
        elif _state == AccountantState.EXTRACT_STATE:
            await state.set_state(AccountantState.ACCOUNT_STATE)

            await message.answer(
                text=AccountantLexicon.ACCOUNTANT_MSG,
                reply_markup=AccountantMarkup.account_markup
            )
        elif _state == AccountantState.ACCOUNT_STATE:
            await state.set_state(AccountantState.TYPE_STATE)

            await message.answer(
                text=AccountantLexicon.TYPE_MSG,
                reply_markup=await AccountantMarkup.get_types()
            )
        elif _state == AccountantState.TYPE_STATE:
            await state.set_state(AccountantState.DOCS_STATE)

            await message.answer(
                text=AccountantLexicon.DOCS_COUNTER_MSG,
                reply_markup=AccountantMarkup.back_markup
            )
