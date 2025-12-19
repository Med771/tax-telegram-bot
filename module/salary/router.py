from aiogram import Router

from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from module.salary.filter import SalaryFilter
from module.salary.service import SalaryService

salary_router = Router(name=__name__)


@salary_router.message(SalaryFilter.back_filter)
async def back_btn(message: Message, state: FSMContext):
    await SalaryService.back_btn(message=message, state=state)


@salary_router.message(SalaryFilter.salary_filter)
async def salary_btn(message: Message, state: FSMContext):
    await SalaryService.salary_btn(message=message, state=state)


@salary_router.message(SalaryFilter.empl_filter)
async def salary_btn(message: Message, state: FSMContext):
    await SalaryService.empl_msg(message=message, state=state)


@salary_router.message(SalaryFilter.white_filter)
async def white_btn(message: Message, state: FSMContext):
    await SalaryService.type_msg(message=message, state=state)

