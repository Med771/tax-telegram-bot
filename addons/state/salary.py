from aiogram.fsm.state import StatesGroup, State


class SalaryState(StatesGroup):
    EMPL_STATE = State(state="EMPL_STATE")
