from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from messages import MESSAGES

# Q&A Keyboard
Q_and_A_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

q_and_exit_button = KeyboardButton(MESSAGES["exit_Q"])
Q_and_A_keyboard.add(q_and_exit_button)
# -----------------------------------------------------------------

# Questionnaire place keyboard
place_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, )

place1_button = KeyboardButton(MESSAGES["place1"])
place2_button = KeyboardButton(MESSAGES["place2"])

place_kb.add(place2_button).add(place1_button)
# -----------------------------------------------------------------
