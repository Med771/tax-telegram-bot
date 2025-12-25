from config import CacheConfig

from tools.file import FileTools


class ExtractData:
    @classmethod
    async def get_extracts(cls):
        data = await ExtractData.read_json_async()

        return [val["cnt"] for val in data]

    @classmethod
    async def get_data_by_cnt(cls, cnt: int):
        data = await ExtractData.read_json_async()

        for row in data:
            if row["cnt"] == cnt:
                return row

        return None

    @classmethod
    async def update_data_async(cls, new_data: list[list]):
        _arr = []

        for row in new_data:
            _arr.append({"cnt": row[0], "price": int(row[1])})

        await FileTools.write_json_async(path=CacheConfig.EXTRACT_PATH,  data=_arr)

    @classmethod
    async def read_json_async(cls):
        return await FileTools.read_json_async(path=CacheConfig.EXTRACT_PATH)
