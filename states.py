from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    start = State()

    email_input = State()
    password_input = State()

    email_check = State()
    password_check = State()

    checked_in = State()
    entered_number = State()

