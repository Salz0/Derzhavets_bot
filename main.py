# region Imports

# Async
import asyncio
import nest_asyncio

# Env
import os

# Directory imports
import tasks
from messages import MESSAGES, ROOMS, PETS_AND_FRIENDS

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
from models import User, Choice, Questions, Voting
from database import init

# endregion ------------------------------------------------------------------------------------------------------------

nest_asyncio.apply()

# region Bot setup & logging
bot = Bot(token=os.environ.get('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

log.add("debug.log", format="{time} {level} {message}",
        level="DEBUG", rotation="10:00", compression="zip")


# endregion ------------------------------------------------------------------------------------------------------------

async def startup(dispatcher):
    await init()


# region PRESENCE CALLBACK HANDLER
@dp.callback_query_handler(lambda callback_query: True,
                           lambda c: c.data == MESSAGES["presence"])
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    user = await User.get(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    user.presence = True
    await user.save()
    log.info(str("presence for {user} is set to 'True'").format(user=callback_query.from_user.get_mention()))
    await bot.send_message(callback_query.from_user.id, MESSAGES["have_a_nice_lecture"])
    await asyncio.sleep(20)  # average length of lecture 3600 (customizable)
    user = await User.get(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    user.presence = False
    await user.save()
    log.info(str("presence for {user} is set to 'False'").format(user=callback_query.from_user.get_mention()))
    await bot.send_message(callback_query.from_user.id, MESSAGES["FINISHED"])


# endregion ------------------------------------------------------------------------------------------------------------
# region VOTING CALLBACK HANDLER (VOTE1)
@dp.callback_query_handler(lambda callback_query: True, lambda c: c.data == MESSAGES["against"])
async def process_callback_vote(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    vote = await Voting.get_or_create(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    vote[0].vote1 = "Against"
    vote[0].vote1_date = datetime.utcnow()
    await vote[0].save()
    log.info(str("Accepted positive vote from {user} ").format(user=callback_query.from_user.get_mention()))
    await bot.send_message(callback_query.from_user.id, MESSAGES["vote_thank_you"])


# endregion ------------------------------------------------------------------------------------------------------------
# region VOTING CALLBACK HANDLER (VOTE1)
@dp.callback_query_handler(lambda callback_query: True, lambda c: c.data == MESSAGES["voter"])
async def process_callback_vote(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    vote = await Voting.get_or_create(id=callback_query.from_user.id, name=callback_query.from_user.get_mention())
    vote[0].vote1 = "For"
    vote[0].vote1_date = datetime.utcnow()
    await vote[0].save()
    log.info(str("Accepted negative vote from {user} ").format(user=callback_query.from_user.get_mention()))
    await bot.send_message(callback_query.from_user.id, MESSAGES["vote_thank_you"])


# endregion ------------------------------------------------------------------------------------------------------------

# region STARTING THE BOT + REGISTERING THE USER TO "user" table
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


# endregion ----------------------------------------------------------------------------------------------------------

# region USER Q&A
@dp.message_handler(commands=["Q&A"], state=None)
async def process_start_command(message: types.Message):
    await States.writing_down_questions.set()
    await message.reply(MESSAGES["Q_and_A_welcoming_message"], reply_markup=kb.Q_and_A_keyboard)


@dp.message_handler(text=MESSAGES["exit_Q"], state=States.writing_down_questions)
async def reply_hello(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(MESSAGES["Q_and_A_goodbye_message"])


@dp.message_handler(content_types=ContentType.TEXT or ContentType.AUDIO, state=States.writing_down_questions)
async def process_start_command(message: types.Message):
    question = Questions(name=message.from_user.get_mention(), question=message.text)
    await question.save()
    await message.reply(MESSAGES["Q_and_A_confirmation_message"], reply_markup=kb.Q_and_A_keyboard)


# endregion ------------------------------------------------------------------------------------------------------------

# region Questionnaire
@dp.message_handler(commands=['questionnaire'], state=None)
async def questionnaire_start(message: types.Message):
    await States.questionnaire.set()
    choice = await Choice.get_or_create(id=message.from_user.id, Name=message.from_user.get_mention())
    await choice[0].save()
    await message.reply(MESSAGES["questionnaire_start"], reply_markup=kb.place_kb)


# region LEVEL 1 (CHOICE OF PLACE)
@dp.message_handler(content_types=ContentType.ANY, state=States.questionnaire)
async def questionnaire_place(message: types.Message):
    choice = await Choice.get(id=message.from_user.id)
    if message == MESSAGES["place1"]:
        choice.place_name = MESSAGES["place1"]
        await message.reply(MESSAGES["questionnaire_floor"], reply_markup=kb.place1_floor_kb)
    else:
        choice.place_name = MESSAGES["place2"]
        await message.reply(MESSAGES["questionnaire_floor"], reply_markup=kb.place2_floor_kb)
    await choice.save()
    choice.p_date = datetime.utcnow()
    await States.questionnaire_floor.set()


# endregion ------------------------------------------------------------------------------------------------------------
# region LEVEL 2 (FLOOR)
@dp.message_handler(content_types=ContentType.ANY, state=States.questionnaire_floor)
async def questionnaire_floor(message: types.Message):
    choice = await Choice.get(id=message.from_user.id)
    if message == MESSAGES["floor1"]:
        choice.floor = MESSAGES["floor1"]
        await message.reply(MESSAGES["questionnaire_room"], reply_markup=kb.place1_floor1_kb)
    elif message == MESSAGES["floor2"]:
        choice.floor = MESSAGES["floor2"]
        await message.reply(MESSAGES["questionnaire_room"], reply_markup=kb.place1_floor2_kb)
    elif message == MESSAGES["mountain_bot"]:
        choice.floor = MESSAGES["mountain_bot"]
        await message.reply(MESSAGES["mountain_msg"], reply_markup=kb.place2_floor1_kb)
    else:
        choice.floor = MESSAGES["mountain_top"]
        await message.reply(MESSAGES["mountain_msg"], reply_markup=kb.place2_floor2_kb)
    choice.f_date = datetime.utcnow()
    await choice.save()
    await States.questionnaire_room.set()


# endregion ------------------------------------------------------------------------------------------------------------
# region LEVEL 3 (ROOMS)
@dp.message_handler(content_types=ContentType.ANY, state=States.questionnaire_room)
async def questionnaire_rooms(message: types.Message):
    choice = await Choice.get(id=message.from_user.id)
    if message == ROOMS["room1"]:
        choice.room = ROOMS["room1"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room1_kb)
    elif message == ROOMS["room2"]:
        choice.room = ROOMS["room2"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room2_kb)
    elif message == ROOMS["room3"]:
        choice.room = ROOMS["room3"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room3_kb)
    elif message == ROOMS["room4"]:
        choice.room = ROOMS["room4"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room4_kb)
    elif message == ROOMS["room5"]:
        choice.room = ROOMS["room5"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room5_kb)
    elif message == ROOMS["room6"]:
        choice.room = ROOMS["room6"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.room6_kb)
    elif message == ROOMS["river"]:
        choice.room = ROOMS["river"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.river_kb)
    elif message == ROOMS["tree"]:
        choice.room = ROOMS["tree"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.tree_kb)
    elif message == ROOMS["igloo"]:
        choice.room = ROOMS["igloo"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.igloo_kb)
    else:
        choice.room = ROOMS["cave"]
        await message.reply(MESSAGES["questionnaire_roommates"], reply_markup=kb.cave_kb)

    choice.r_date = datetime.utcnow()
    await choice.save()
    await States.questionnaire_mate.set()


# endregion ------------------------------------------------------------------------------------------------------------
# region LEVEL 4 (FRIENDS)
@dp.message_handler(content_types=ContentType.ANY, state=States.questionnaire_mate)
async def questionnaire_friends(message: types.Message, state: FSMContext):
    choice = await Choice.get(id=message.from_user.id)
    if message == PETS_AND_FRIENDS["pet_river1"]:
        choice.roommates = PETS_AND_FRIENDS["pet_river1"]
    elif message == PETS_AND_FRIENDS["pet_river2"]:
        choice.roommates = PETS_AND_FRIENDS["pet_river2"]
    elif message == PETS_AND_FRIENDS["pet_tree1"]:
        choice.roommates = PETS_AND_FRIENDS["pet_tree1"]
    elif message == PETS_AND_FRIENDS["pet_tree2"]:
        choice.roommates = PETS_AND_FRIENDS["pet_tree2"]
    elif message == PETS_AND_FRIENDS["pet_igloo1"]:
        choice.roommates = PETS_AND_FRIENDS["pet_igloo1"]
    elif message == PETS_AND_FRIENDS["pet_igloo2"]:
        choice.roommates = PETS_AND_FRIENDS["pet_igloo2"]
    elif message == PETS_AND_FRIENDS["pet_cave1"]:
        choice.roommates = PETS_AND_FRIENDS["pet_cave1"]
    elif message == PETS_AND_FRIENDS["pet_cave2"]:
        choice.roommates = PETS_AND_FRIENDS["pet_cave2"]
    elif message == PETS_AND_FRIENDS["room1_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room1_friend1"]
    elif message == PETS_AND_FRIENDS["room1_friend2"]:
        choice.roommates = PETS_AND_FRIENDS["room1_friend2"]
    elif message == PETS_AND_FRIENDS["room2_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room2_friend1"]
    elif message == PETS_AND_FRIENDS["room2_friend2"]:
        choice.roommates = PETS_AND_FRIENDS["room2_friend2"]
    elif message == PETS_AND_FRIENDS["room3_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room3_friend1"]
    elif message == PETS_AND_FRIENDS["room3_friend2"]:
        choice.roommates = PETS_AND_FRIENDS["room3_friend2"]
    elif message == PETS_AND_FRIENDS["room4_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room4_friend1"]
    elif message == PETS_AND_FRIENDS["room4_friend2"]:
        choice.roommates = PETS_AND_FRIENDS["room4_friend2"]
    elif message == PETS_AND_FRIENDS["room5_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room5_friend1"]
    elif message == PETS_AND_FRIENDS["room5_friend2"]:
        choice.roommates = PETS_AND_FRIENDS["room5_friend2"]
    elif message == PETS_AND_FRIENDS["room6_friend1"]:
        choice.roommates = PETS_AND_FRIENDS["room6_friend1"]
    else:
        choice.roommates = PETS_AND_FRIENDS["room6_friend2"]
    choice.rm_date = datetime.utcnow()
    await choice.save()
    await state.finish()
    await message.reply(MESSAGES["questionnaire_goodbye"])


# endregion ------------------------------------------------------------------------------------------------------------

# endregion ------------------------------------------------------------------------------------------------------------

# region CHECKING PRESENCE OF USERS ON LECTURE (customizable)
@dp.message_handler(commands="start_presence")  # to activate: /start_presence
async def presence_function(h):
    h = 7
    log.info(f'Task will be done in less than {h} seconds')
    await asyncio.sleep(h)
    # await asyncio.sleep(3600) # 1 HOUR
    # await asyncio.sleep(3600 * 10) # 10 HOURS
    # await asyncio.sleep(3600 * 24) # 24 HOURS
    # await asyncio.sleep(3600 * 24 * 7) # WEEK
    # await asyncio.sleep(3600 * 24 * 7 * 30) # 30 days (all from now)
    tasks.broadcast_message(MESSAGES["LECTURE_START"],
                            buttons=[{'text': "Я тут, не кричи", 'callback_data': MESSAGES["presence"]}])


# endregion
# region INDIVIDUAL VOTING (customizable)
@dp.message_handler(commands="start_voting")  # to activate /start_voting
async def individual_voting(h):
    h = 7
    log.info(f'Individual voting will be sent in {h} seconds')
    await asyncio.sleep(h)
    # await asyncio.sleep(3600) # 1 HOUR
    # await asyncio.sleep(36000) # 10 HOURS
    # await asyncio.sleep(3600 * 24) # 24 HOURS
    # await asyncio.sleep(3600 * 24 * 7) # WEEK
    tasks.broadcast_message(MESSAGES["NEW_VALUE"],
                            buttons=[{"text": MESSAGES["za"], "callback_data": MESSAGES["voter"]},
                                     {"text": MESSAGES["proty"], "callback_data": MESSAGES['against']}])


# endregion ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup)

########################################################################################################################
