from aiogram import Router

from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from module.accountant.filter import AccountantFilter
from module.accountant.service import AccountantService

accountant_router = Router(name=__name__)


@accountant_router.message(AccountantFilter.back_filter)
async def back_btn(message: Message, state: FSMContext):
    await AccountantService.back_btn(message=message, state=state)


@accountant_router.message(AccountantFilter.accountant_filter)
async def accountant_btn(message: Message, state: FSMContext):
    await AccountantService.accountant_btn(message=message, state=state)


@accountant_router.message(AccountantFilter.docs_filter)
async def docs_msg(message: Message, state: FSMContext):
    await AccountantService.docs_msg(message=message, state=state)


@accountant_router.message(AccountantFilter.type_filter)
async def type_btn(message: Message, state: FSMContext):
    await AccountantService.type_btn(message=message, state=state)
