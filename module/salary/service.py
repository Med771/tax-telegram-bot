from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from data import SalaryData

from addons.decorator import TelegramDecorator
from addons.lexicon import SalaryLexicon
from addons.markup import SalaryMarkup
from addons.state import SalaryState

from tools.admin import AdminTools


class SalaryService:
    @classmethod
    @TelegramDecorator.log_call()
    async def back_btn(cls, message: Message, state: FSMContext):
        _state = await AdminTools.get_state(state=state)

        if _state == SalaryState.RESULT_STATE:
            await state.set_state(SalaryState.WHITE_STATE)

            await message.answer(
                text=(
                        SalaryLexicon.EMPL_MSG +
                        SalaryLexicon.EMPL_RESULT_MSG.format(empl=message.text)),
                reply_markup=SalaryMarkup.type_markup)
        elif _state == SalaryState.WHITE_STATE:
            await state.set_state(SalaryState.EMPL_STATE)

            await message.answer(
                text=SalaryLexicon.EMPL_MSG,
                reply_markup=SalaryMarkup.empl_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def salary_btn(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.EMPL_STATE)

        await state.set_data({"empl": 0})

        await message.answer(
            text=SalaryLexicon.EMPL_MSG,
            reply_markup=SalaryMarkup.empl_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def empl_msg(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.WHITE_STATE)
        await state.update_data(empl=int(message.text))

        await message.answer(
            text=(
                SalaryLexicon.EMPL_MSG +
                SalaryLexicon.EMPL_RESULT_MSG.format(empl=message.text)),
            reply_markup=SalaryMarkup.type_markup)

    @classmethod
    @TelegramDecorator.log_call()
    async def type_msg(cls, message: Message, state: FSMContext):
        await state.set_state(SalaryState.RESULT_STATE)

        data = await state.get_data()
        _dict = await SalaryData.read_json_async()

        fix_key = "fix_with" if message.text == SalaryLexicon.YES_WHITE_BTN_TEXT else "fix_without"
        per_key = "per_person_with" if message.text == SalaryLexicon.YES_WHITE_BTN_TEXT else "per_person_without"

        fix = _dict.get(fix_key, 0)
        price = _dict.get(per_key, 0)
        empl = data.get("empl", 0)

        total = fix + (empl - 1) * price

        await message.answer(
            text=SalaryLexicon.RESULT_MSG.format(
                empl=empl,
                white=message.text,
                total=total),
            reply_markup=SalaryMarkup.res_markup)
