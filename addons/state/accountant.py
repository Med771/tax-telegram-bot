from aiogram.fsm.state import StatesGroup, State


class AccountantState(StatesGroup):
    DOCS_STATE = State(state="DOCS_STATE")
    TYPE_STATE = State(state="TYPE_STATE")
    ACCOUNT_STATE = State(state="ACCOUNT_STATE")
    EXTRACT_STATE = State(state="EXTRACT_STATE")
    RES_STATE = State(state="RES_STATE")
