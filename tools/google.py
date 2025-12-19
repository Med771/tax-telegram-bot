from gspread import Worksheet
from gspread.utils import rowcol_to_a1, ValueRenderOption


class GoogleTools:
    @staticmethod
    def read_values(ws: Worksheet, start_row: int, start_col: int, end_row: int, end_col: int) -> list[list[str]]:
        range_row: str = rowcol_to_a1(start_row, start_col)
        range_col: str = rowcol_to_a1(end_row, end_col)

        return ws.get_values(
            range_name=f"{range_row}:{range_col}",
            value_render_option=ValueRenderOption.unformatted,
        )

    @staticmethod
    def write_values(values: list[list[str]], start_row: int, start_col: int, ws: Worksheet, raw: bool = True) -> None:
        end_row = start_row + len(values) - 1
        end_col = start_col + len(values[0]) - 1

        range_row: str = rowcol_to_a1(start_row, start_col)
        range_col: str = rowcol_to_a1(end_row, end_col)

        ws.update(
            range_name=f"{range_row}:{range_col}",
            values=values,
            raw=raw)
