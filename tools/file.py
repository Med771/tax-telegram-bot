import json
from pathlib import Path

import aiofiles

from typing import Any

from config.main import MainConfig


class FileTools:
    @staticmethod
    async def read_json_async(path: Path) -> Any:
        """
        Асинхронно читает JSON-файл и возвращает Python-объект.
        """

        try:
            async with aiofiles.open(path, mode="r", encoding=MainConfig.ENCODING) as file:
                content = await file.read()

                return json.loads(content)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    @staticmethod
    async def write_json_async(path: Path, data: Any) -> None:
        """
        Асинхронно записывает Python-объект в JSON-файл.
        """
        async with aiofiles.open(path, mode="w", encoding=MainConfig.ENCODING) as file:
            content = json.dumps(data, ensure_ascii=False, indent=2)

            await file.write(content)
