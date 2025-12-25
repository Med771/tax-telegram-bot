from config import CacheConfig

from tools.file import FileTools


class SalaryData:
    @classmethod
    async def update_data_async(cls, fix_with: int, fix_without: int, per_person_with: int, per_person_without: int):
        _dict = {
            "fix_with": fix_with,
            "fix_without": fix_without,
            "per_person_with": per_person_with,
            "per_person_without": per_person_without,
        }

        await FileTools.write_json_async(CacheConfig.SALARY_PATH, _dict)

    @classmethod
    async def read_json_async(cls):
        return await FileTools.read_json_async(CacheConfig.SALARY_PATH)