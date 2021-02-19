from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    present = State()
    writing_down_questions = State()

    # Questionnaire states
    questionnaire = State()
    questionnaire_floor = State()
    questionnaire_room = State()
    questionnaire_mate = State()
