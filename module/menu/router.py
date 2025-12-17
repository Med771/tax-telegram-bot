from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from module.menu.service import MenuService

menu_router = Router(name=__name__)


@menu_router.message(Command(commands=["start", "reset"]))
async def start_command(message: Message, state: FSMContext):
    await MenuService.start_command(message=message, state=state)
