from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text

# QUESTIONNAIRE MESSAGES:
questionnaire_start = text(emojize("Привіт!👋\n Розкажи, будь ласка: де та з ким ти хочеш жити 😏"))
questionnaire_floor = text(emojize("На якому поверсі ти хотів/ла би оселитися?🧳"))
questionnaire_room = text(emojize("Який номер кімнати в тебе з щасливих?🎰"))
questionnaire_roommates = text(emojize("Останнє, з ким ти хотів/ла би жити? 🐸"))

# QUESTIONNAIRE BUTTONS:
place1 = text(emojize("На Майбороди, з коліверами"))
place2 = text(emojize("У горах, наодинці🌄"))

# SINGLE-PURPOSE MESSAGES:
start_message = text(emojize("Привіт!👋"))
registered_message = "Давно не бачилися!"
have_a_nice_lecture = text(emojize("Продуктивної лекції тобі! 😉"))

# Q&A RESPONSES:
Q_and_A_welcoming_message = text(emojize("Привіт, тут ти можеш задати стільки питань, скільки забажаєш\n"
                                         "Коли закінчиш, натисни клавішу 'Вийти'😉"))
Q_and_A_confirmation_message = text(emojize("Записав!📃"))
exit_Q = "Вийти"
Q_and_A_goodbye_message = text(emojize("Я обов'язково передам твої повідомлення 🧭"))


# TEMPLATE = text(emojize())

MESSAGES = {

    "start_message": start_message,
    "registered_message": registered_message,
    "have_a_nice_lecture": have_a_nice_lecture,
    # Q&A RESPONSES:
    "Q_and_A_welcoming_message": Q_and_A_welcoming_message,
    "Q_and_A_confirmation_message": Q_and_A_confirmation_message,
    "exit_Q": exit_Q,
    "Q_and_A_goodbye_message": Q_and_A_goodbye_message,
    # QUESTIONNAIRE RESPONSES:
    "questionnaire_start": questionnaire_start,
    "questionnaire_floor": questionnaire_floor,
    "questionnaire_room": questionnaire_room,
    "questionnaire_roommates": questionnaire_roommates,
    # QUESTIONNAIRE BUTTONS
    "place1": place1,
    "place2": place2

}

