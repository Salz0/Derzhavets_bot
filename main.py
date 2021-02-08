# Imported from directory
import os

import keyboards as kb
from states import States
from messages import MESSAGES

# For logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging

# Other
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types.message import ContentType

# Time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# ORM
from orm import UserModel, init

bot = Bot(token=os.environ.get('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def startup(dispatcher):
    await init()


@dp.message_handler(commands=['start'], state=None)
async def process_start_command(message: types.Message):
    await States.start.set()
    user_id = message.from_user.id
    mention = f"{message.from_user.get_mention()}"
    reg = UserModel(id=user_id, name=mention)  # , register_DateTime=current_time
    await reg.save()
    pr = await UserModel.filter(name__contains='@%').first()
    print(pr.name)
    await message.reply(MESSAGES['start_message'], reply_markup=kb.markup_PH_request)



# @dp.message_handler(content_types=ContentType.ANY, state=States.start)
# async def phone_registered(message: types.Message):
#     if message.content_type is ContentType.CONTACT:
#         if message.contact.user_id == message.from_user.id:  # check if own contact is sent
#             user_number = str(message.contact.phone_number)
#             await States.entered_number.set()
#             return await message.reply(MESSAGES['satisfied'] + user_number, reply_markup=kb.GoBack)
#         else:
#             return await message.reply(MESSAGES['tricked'], reply_markup=kb.markup_PH_request)  # retry number input
#     else:
#         return await message.reply(MESSAGES['unsatisfied'], reply_markup=kb.markup_PH_request)


# @dp.message_handler(lambda msg: msg.text == 'Переглянути наявні номери 📃', state=States.entered_number)
# async def reply_hello(msg: types.Message, state: FSMContext):
#     await state.finish()
#     await msg.reply(MESSAGES['THE JOURNAL'])

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup)
