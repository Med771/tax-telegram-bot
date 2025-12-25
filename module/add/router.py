from aiogram import Router

from aiogram.types import Message

from module.add.filter import AddFilter
from module.add.service import AddService

add_router = Router(name=__name__)


@add_router.message(AddFilter.add_filter)
async def add_btn(message: Message):
    await AddService.add_btn(message)
