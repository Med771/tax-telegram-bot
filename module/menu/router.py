from aiogram import Router

from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from module.menu.filter import MenuFilter
from module.menu.service import MenuService

menu_router = Router(name=__name__)


@menu_router.message(Command(commands=["start", "reset"]))
@menu_router.message(MenuFilter.back_btn)
async def start_command(message: Message, state: FSMContext):
    await MenuService.start_command(message=message, state=state)

@menu_router.callback_query(MenuFilter.back_inl_btn)
async def back_inl_btn(callback: CallbackQuery, state: FSMContext):
    await MenuService.back_inl_btn(callback=callback, state=state)
