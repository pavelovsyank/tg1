from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_command_menu(bot: Bot):
    command1 = BotCommand(command="/start", description="Начало работы")
    command2 = BotCommand(command="/help", description="Помощь")
    commands = [command1, command2]
    await bot.set_my_commands(commands, BotCommandScopeDefault())