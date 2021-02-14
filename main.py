# Imports
# Directory imports
import asyncio
import os
from messages import MESSAGES

# Keyboards
import keyboards as kb

# States And Filtering
from states import States
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.message import ContentType

# Logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger as log

# Bot
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext

# Telling Time
from datetime import datetime

# ORM
from models import User, Choice, Questions
from database import init

# Bot setup & logging
bot = Bot(token=os.environ.get('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

log.add("debug.log", format="{time} {level} {message}",
        level="DEBUG", rotation="10:00", compression="zip")


# ----------------------------------------------------------------------------------------------------------------------

async def startup(dispatcher):
    await init()


# HANDLER FOR CATCHING CALLBACK QUERIES (FROM INLINE KEYBOARDS):
@dp.callback_query_handler(lambda callback_query: True, lambda c: c.data == 'PRESENT09')
async def process_callback_button1(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    user = await User.get(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    user.presence = True
    await user.save()
    log.info(str("presence for {user} is set to 'True'").format(user=user))
    await bot.send_message(callback_query.from_user.id, MESSAGES["have_a_nice_lecture"])
    await asyncio.sleep(3600)  # average length of lecture
    user = await User.get(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    user.presence = False
    await user.save()
    log.info(str("presence for {user} is set to 'False'").format(user=user))
    await bot.send_message(callback_query.from_user.id, 'FINISHED')


# ----------------------------------------------------------------------------------------------------------------------

# STARTING THE BOT + REGISTERING THE USER TO "user":
@dp.message_handler(commands=["start"], state=None)
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    mention = message.from_user.get_mention()
    try:
        reg = User(id=user_id, name=mention, presence=False)
        choice_init = Choice(id=user_id, Name=mention)
        await reg.save()
        await choice_init.save()
    finally:
        return await message.reply(MESSAGES["start_message"])


# ----------------------------------------------------------------------------------------------------------------------

# USER Q&A:
@dp.message_handler(commands=["Q&A"])
async def process_start_command(message: types.Message):
    await States.writing_down_questions.set()
    return await message.reply(MESSAGES["Q_and_A_welcoming_message"],
                               reply_markup=kb.Q_and_A_keyboard)


@dp.message_handler(lambda message: message.text == MESSAGES["exit_Q"], state=States.writing_down_questions)
async def reply_hello(message: types.Message, state: FSMContext):
    await state.finish()
    return await message.reply(MESSAGES["Q_and_A_goodbye_message"])


@dp.message_handler(content_types=ContentType.TEXT or ContentType.AUDIO, state=States.writing_down_questions)
async def process_start_command(message: types.Message):
    message_text = message.text
    question = Questions(name=message.from_user.get_mention(), question=message_text)
    await question.save()
    return await message.reply(MESSAGES["Q_and_A_confirmation_message"],
                               reply_markup=kb.Q_and_A_keyboard)


# ----------------------------------------------------------------------------------------------------------------------

# Questionnaire: (UNDER DEVELOPMENT)
@dp.message_handler(commands=['questionnaire'], state=None)
async def process_start_command(message: types.Message, state: FSMContext):
    await States.questionnaire.set()
    await message.reply(MESSAGES["questionnaire_start"],
                        reply_markup=kb.place_kb)


# Branch1: (UNDER DEVELOPMENT)
@dp.message_handler(lambda message: message.text == MESSAGES["place1"] or MESSAGES["place2"],
                    state=States.questionnaire)
async def reply_hello(message: types.Message, state: FSMContext):
    choice = await Choice.get(id=message.from_user.id)
    if message == MESSAGES["place1"]:
        await States.maybach_place.set()
        choice.place = MESSAGES["place1"]
    else:
        await States.mountain_place.set()
        choice.place = MESSAGES["place2"]
    choice.p_date = datetime.utcnow()
    await choice.save()
    await message.reply(MESSAGES["questionnaire_floor"])


# Branch2: (UNDER DEVELOPMENT)
# @dp.message_handler(lambda msg: msg.text == kb.p_button2, state=States.questionnaire)
# async def reply_hello(msg: types.Message, state: FSMContext):
#     await state.finish()
#     await msg.reply(MESSAGES['THE JOURNAL'])


# ----------------------------------------------------------------------------------------------------------------------
"""
# SAMPLE Of "broadcast_message"
tasks.broadcast_message("ЛЕКЦІЯ ПОЧАЛАСЯ, УАЛІВЕЦЬ ВСТАВАЙ!",
                          buttons=[{'text': "Я тут, не кричи", 'callback_data': "PRESENT09"}]).delay()
"""

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup)

########################################################################################################################
