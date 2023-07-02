from aiogram.fsm.state import StatesGroup, State


class OrderImageGenerate(StatesGroup):
    image_generate = State()
