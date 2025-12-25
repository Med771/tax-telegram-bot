from aiogram.types import Message, InputMediaPhoto, FSInputFile

from config import CacheConfig

from addons.decorator import TelegramDecorator
from addons.lexicon import AddLexicon
from addons.markup import AddMarkup


class AddService:
    @classmethod
    @TelegramDecorator.log_call()
    async def add_btn(cls, message: Message):
        media_group = [
            InputMediaPhoto(media=FSInputFile(path=CacheConfig.FIRST_PHOTO_PATH)),
            InputMediaPhoto(media=FSInputFile(path=CacheConfig.FIRST_PHOTO_PATH))
        ]

        await message.answer_media_group(media=media_group)

        await message.answer(text=AddLexicon.ADD_MSG, reply_markup=AddMarkup.menu_markup)
