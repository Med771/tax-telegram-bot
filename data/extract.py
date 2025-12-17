from config import CacheConfig
from config import GoogleConfig

from tools.google import GoogleTools
from tools.file import FileTools


async def update_extract():
    try:
        new_data_in_table: list[dict[str, int]] = ExtractData.read_data_in_table()

        await ExtractData.update_data_in_cache(new_data_in_table)
    except:
        pass

class ExtractData:
    @classmethod
    def create_obj(cls, cnt: int, price: int) -> dict[str, int]:
        return {"cnt": cnt, "price": price}

    @classmethod
    def read_data_in_table(cls) -> list[dict[str, int]]:
        rows = GoogleTools.read_values(
            ws=GoogleConfig.WS,
            start_col=CacheConfig.EXTRACT_RANGE_TUP[0], end_col=CacheConfig.EXTRACT_RANGE_TUP[1],
            start_row=CacheConfig.EXTRACT_RANGE_TUP[2], end_row=CacheConfig.EXTRACT_RANGE_TUP[3])

        return [cls.create_obj(cnt=int(row[0]), price=int(row[1])) for row in rows]

    @classmethod
    async def update_data_in_cache(cls, new_data: list[dict[str, int]]):
        await FileTools.write_json_async(path=CacheConfig.EXTRACT_PATH,  data=new_data)

    @classmethod
    async def read_data_in_cache(cls):
        return await FileTools.read_json_async(path=CacheConfig.EXTRACT_PATH)
