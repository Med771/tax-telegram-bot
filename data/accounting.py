from config import CacheConfig
from config import GoogleConfig

from tools.google import GoogleTools
from tools.file import FileTools


async def update_accounting():
    try:
        new_data_in_table: list[dict] = AccountingData.read_data_in_table()

        await AccountingData.update_data_in_cache(new_data_in_table)
    except:
        pass


class AccountingData:
    @classmethod
    def create_obj(cls, _type: str, account: int, amounts: list[tuple[int, int]]) -> dict:
        return {"type": _type, "account": account, "amounts": [{"cnt": pair[0], "price": pair[1]} for pair in amounts]}

    @classmethod
    def read_data_in_table(cls) -> list[dict]:
        rows = GoogleTools.read_values(
            ws=GoogleConfig.WS,
            start_col=CacheConfig.ACCOUNTING_RANGE_TUP[0], end_col=CacheConfig.ACCOUNTING_RANGE_TUP[1],
            start_row=CacheConfig.ACCOUNTING_RANGE_TUP[2], end_row=CacheConfig.ACCOUNTING_RANGE_TUP[3])

        res = []
        cnt = rows[0][3:]

        for row in rows[1:]:
            amounts = []

            for i in range(3, len(row)):
                amounts.append((cnt[i - 3], row[i]))

            obj = cls.create_obj(row[0], int(row[1]), amounts)

            res.append(obj)

        return res

    @classmethod
    async def update_data_in_cache(cls, new_data: list[dict]):
        await FileTools.write_json_async(path=CacheConfig.ACCOUNTING_PATH, data=new_data)

    @classmethod
    async def read_data_in_cache(cls):
        return await FileTools.read_json_async(path=CacheConfig.ACCOUNTING_PATH)