import asyncio
from typing import Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import exceptions, executor

from cel_costil import celery_app
from models import User
import database
from loguru import logger as log


@celery_app.task()
def ping():
    log.info('Celery task triggered')
    return 'pong'


async def send_message(user_id: int,
                       text: str,
                       buttons: Optional[list[dict[str, str]]] = None,
                       disable_notification: bool = False) -> bool:
    """
    Safe messages sender

    :param user_id:
    :param text:
    :param buttons: List of inline buttons in format [{'text': 'text', 'callback_data': 'callback_data', **kwargs}].
        A button can have all the same keys that InlineKeyboardButton() take
    :param disable_notification:
    :return:
    """

    from main import bot

    try:
        await bot.send_message(user_id, text, reply_markup=InlineKeyboardMarkup(
            row_width=2,
            resize_keyboard=True,
            one_time_keyboard=True, ).add(
            *[InlineKeyboardButton(**button) for button in buttons])
        if buttons else None,
                               disable_notification=disable_notification)
        log.info(f"Sent message to target [ID:{user_id}]")
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text, buttons)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcaster(text: str,
                      buttons: Optional[list[dict[str, str]]] = None) -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """

    # Init Tortoise database first
    await database.init()

    count = 0
    try:
        async for user in User.all():
            # if user.is_active and (await user.profile).is_registered:
            if await send_message(user.pk, text, buttons):
                log.info(f'Sent a message to user [ID:{user.pk}] [USERNAME:{user.name}]')
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        log.info(f"{count} messages successful sent.")

    return count


@celery_app.task()
def broadcast_message(text: str,
                      buttons: Optional[list[dict[str, str]]] = None, *args):
    """
    Celery task used to broadcast new messages to users

    :param text: Text to be sent #TODO: [11/13/2020 by Mykola] Add formatting, such as HTML or Markdown
    :param buttons: List of inline buttons in format [{'text': 'text', 'callback_data': 'callback_data', **kwargs}]
    :return:
    """
    from main import dp
    executor.start(dp, broadcaster(text, buttons))
