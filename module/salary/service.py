from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from addons.decorator import TelegramDecorator
from addons.lexicon import SalaryLexicon
from addons.markup import SalaryMarkup
from addons.state import SalaryState
from data.with_salary import WithData
from data.without_salary import WithoutData


class SalaryService:
    @classmethod
    @TelegramDecorator.log_call()
    async def salary_btn(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.EMPL_STATE)

        await message.answer(
            text=SalaryLexicon.EMPL_MSG,
            reply_markup=SalaryMarkup.empl_markup
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def empl_msg(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.WHITE_STATE)
        await state.update_data(empl=int(message.text))

        await message.answer(
            text=(
                SalaryLexicon.EMPL_MSG +
                SalaryLexicon.EMPL_RESULT_MSG.format(empl=message.text)
            ),
            reply_markup=SalaryMarkup.type_markup
        )

    @classmethod
    @TelegramDecorator.log_call()
    async def type_msg(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.RESULT_STATE)

        if message.text == SalaryLexicon.YES_WHITE_BTN_TEXT:
            _dict = await WithData.read_data_in_cache()
        else:
            _dict = await WithoutData.read_data_in_cache()

        fix = _dict["fix"]
        price = _dict["perPerson"]

        data = await state.get_data()

        docs = data["docs"]
        _type = data["_type"]
        acc = data["acc"]
        ex = data["ex"]
        empl = data["empl"]
        total1 = data["total"]
        total2 = fix + (empl - 1) * price

        await message.answer(
            text=SalaryLexicon.RESULT_MSG.format(
                docs=docs,
                type=_type,
                accountant=acc,
                extract=ex,
                total1=total1,
                empl=empl,
                white=message.text,
                total2=total2,
                total3=total1 + total2,
            ),
            reply_markup=SalaryMarkup.res_markup
        )
