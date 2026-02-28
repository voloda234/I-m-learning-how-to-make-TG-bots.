from aiogram.fsm.state import StatesGroup, State


class chat(StatesGroup):
    text = State()
    wait = State()