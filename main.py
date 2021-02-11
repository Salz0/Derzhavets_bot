# Imported from directory
import asyncio
import os

import celery
from celery.app import task

import keyboards as kb
from cel_costil import celery_app
from states import States
from messages import MESSAGES

# For logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger as log

# Other
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext

# Time
from datetime import datetime
# from celery import Celery
# from celery import

# ORM
from models import User
from database import init

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

bot = Bot(token=os.environ.get('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

log.add("debug.log", format="{time} {level} {message}",
        level="DEBUG", rotation="10:00", compression="zip")


async def startup(dispatcher):
    await init()


@dp.message_handler(commands=['start'], state=None)
async def process_start_command(message: types.Message):
    await States.start.set()
    user_id = message.from_user.id
    mention = f"{message.from_user.get_mention()}"
    if user_id not in User:
        reg = User(id=user_id, name=mention)  # , register_DateTime=current_time
        await reg.save()
        return await message.reply(MESSAGES['start_message'], reply_markup=kb.markup_PH_request)
    else:
        return await message.reply(MESSAGES['start_message'], reply_markup=kb.markup_PH_request)


import tasks
from time import sleep
from datetime import date


@celery_app.task  # (task_track_started=True, apply_async=True)
def set_message(time1, date1):
    current_time1 = datetime.now().strftime("%H/%M/%S")
    current_date1 = date.today().strftime("%d/%m/%Y")

    while current_date1 != str(date1):
        current_date1 = date.today().strftime("%d/%m/%Y")
        print(current_date1)
        sleep(60 * 60)

    while str(time1) != current_time1:
        now = datetime.now()
        current_time1 = now.strftime("%H:%M:%S")
        print(current_time)
        sleep(0.5)
    return tasks.broadcast_message("async problem solved")

# when delay applied shows error
set_message.delay("11:46:00", "11/02/2021")
set_message.delay("11:46:10", "11/02/2021")
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup)