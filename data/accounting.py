from config import CacheConfig
from tools.file import FileTools


class AccountingData:
    @classmethod
    async def get_types(cls):
        data = await AccountingData.read_json_async()

        return [accountant["type"] for accountant in data]

    @classmethod
    async def get_data_by_type(cls, _type: str) -> dict | None:
        data: list[dict] = await AccountingData.read_json_async()

        for value in data:
            if value["type"] == _type:
                return value

        return None

    @classmethod
    async def update_data_async(cls, data: list[list]):
        _arr = []

        for row in data:
            _arr.append({
                "type": row[0],
                "accountant": int(row[1]),
                "200-500": int(row[3]),
                "500-1000": int(row[4]),
                "1000-1500": int(row[5]),
                "1500-2000": int(row[6]),
            })

        await FileTools.write_json_async(path=CacheConfig.ACCOUNTING_PATH, data=_arr)

    @classmethod
    async def read_json_async(cls):
        return await FileTools.read_json_async(path=CacheConfig.ACCOUNTING_PATH)