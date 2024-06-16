import sys
import asyncio
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.middleware import FSMContextMiddleware, BaseEventIsolation
from keyboards.keyboards import main_menu_keyboard, MAIN_MENU_MESSAGE
from handlers import register_handlers_profile, register_handlers_settings, register_handlers_todo, register_handlers_avito
from utils.event_isolation import CustomEventIsolation
from db.database import init_db

load_dotenv()
TOKEN = os.getenv('API_TOKEN')

# Initialize the database
init_db()

# Initialize Bot and Dispatcher with storage
bot = Bot(
    token=TOKEN,
    session=AiohttpSession(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

# Add FSM middleware
events_isolation = CustomEventIsolation()
dp.update.middleware(FSMContextMiddleware(storage=MemoryStorage(), events_isolation=events_isolation))

# Register handlers
register_handlers_profile(dp)
register_handlers_settings(dp)
register_handlers_todo(dp)
register_handlers_avito(dp)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Help message"),
    ]
    await bot.set_my_commands(commands)

async def send_welcome(message: types.Message):
    await message.answer(MAIN_MENU_MESSAGE, reply_markup=main_menu_keyboard())


dp.message.register(send_welcome, Command(commands=["start", "help"]))

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
