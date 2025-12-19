from aiogram.fsm.state import StatesGroup, State


class SalaryState(StatesGroup):
    EMPL_STATE = State(state="EMPL_STATE")
    WHITE_STATE = State(state="WHITE_STATE")
    RESULT_STATE = State(state="RESULT_STATE")
