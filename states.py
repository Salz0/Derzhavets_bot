from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    present = State()
    writing_down_questions = State()

    # Questionnaire states
    questionnaire = State()
    maybach_place = State()
    mountain_place = State()
