from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import BotCommand, BotCommandScopeDefault

async def command_start(message: Message) -> None:
    s1 = "какая-то строка (приветствие)"
    ans = f"Hello, {message.from_user.full_name}\n{s1}"
    await message.answer(ans)

async def command_help(message: Message) -> None:
    ans = """
    Выбирайте команду из меню и следуйте подсказкам. 
    Или вводите команды напрямую
    cmd1 - первая команда
    cmd2 - вторая команда
    """
    await message.answer(ans)