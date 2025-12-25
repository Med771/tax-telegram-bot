from config import GoogleConfig
from config import CacheConfig

from tools.google import GoogleTools

from data.salary import SalaryData
from data.accounting import AccountingData


class CacheData:
    @classmethod
    async def get_data(cls):
        await cls.salary_data()
        await cls.accounting_data()

    @classmethod
    async def salary_data(cls):
        data = GoogleTools.read_values(
            ws=GoogleConfig.WS,
            start_col=CacheConfig.SALARY_RANGE[0],
            end_col=CacheConfig.SALARY_RANGE[1],
            start_row=CacheConfig.SALARY_RANGE[2],
            end_row=CacheConfig.SALARY_RANGE[3],
        )

        await SalaryData.update_data_async(
            fix_with=int(data[3][0]),
            fix_without=int(data[0][0]),
            per_person_with=int(data[4][0]),
            per_person_without=int(data[1][0]),
        )

    @classmethod
    async def accounting_data(cls):
        data = GoogleTools.read_values(
            ws=GoogleConfig.WS,
            start_col=CacheConfig.ACCOUNTING_RANGE[0],
            end_col=CacheConfig.ACCOUNTING_RANGE[1],
            start_row=CacheConfig.ACCOUNTING_RANGE[2],
            end_row=CacheConfig.ACCOUNTING_RANGE[3],
        )

        await AccountingData.update_data_async(data=data)
