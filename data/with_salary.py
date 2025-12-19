from config import CacheConfig
from config import GoogleConfig

from tools.google import GoogleTools
from tools.file import FileTools


async def update_with():
    try:
        new_data_in_table: dict[str, int] = WithData.read_data_in_table()

        await WithData.update_data_in_cache(new_data_in_table)
    except:
        pass

class WithData:
    @classmethod
    def create_obj(cls, fix: int, per_person: int) -> dict[str, int]:
        return {"fix": fix, "perPerson": per_person}

    @classmethod
    def read_data_in_table(cls) -> dict[str, int]:
        rows = GoogleTools.read_values(
            ws=GoogleConfig.WS,
            start_col=CacheConfig.WITH_RANGE_TUP[0], end_col=CacheConfig.WITH_RANGE_TUP[1],
            start_row=CacheConfig.WITH_RANGE_TUP[2], end_row=CacheConfig.WITH_RANGE_TUP[3])

        return cls.create_obj(int(rows[0][0]), int(rows[1][0]))

    @classmethod
    async def update_data_in_cache(cls, new_data: dict[str, int]):
        await FileTools.write_json_async(path=CacheConfig.WITH_PATH, data=new_data)

    @classmethod
    async def read_data_in_cache(cls):
        return await FileTools.read_json_async(path=CacheConfig.WITH_PATH)