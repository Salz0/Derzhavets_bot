from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text


start_message = text(emojize("Привіт!👋 Бачу, ти новенький\nДавай зареєструємось?📃"))
start_register = "Давай!"
start_registered = text(emojize("Я вже зареєстрований 💪"))
journal = text(emojize("Тут має бути список номерів, УРА! 😁😎"))

MESSAGES = {

    'start_message': start_message,
    'start_register': start_register,
    'i_have_an_account': start_registered,

}
