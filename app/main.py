from random import randint
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import BotCommand, BotCommandScopeDefault
from app.config import settings
from app.menu.commands_menu import set_command_menu
from app.handlers import handler_menu

dp = Dispatcher()

dp.message.register(handler_menu.command_start, Command(commands="start"))
dp.message.register(handler_menu.command_help, Command(commands="help"))


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        print(f"echo_handler {message.text}")
        await message.send_copy(chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())
    except TypeError:
        await message.answer("Nice try!")

async def main():
    print("Start tg main")
    bot = Bot(settings.token, parse_mode=ParseMode.HTML)
    await set_command_menu(bot)
    await dp.start_polling(bot, skip_updates=True)


