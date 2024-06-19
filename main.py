import sys
import asyncio
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand,  FSInputFile
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.middleware import FSMContextMiddleware, BaseEventIsolation
from keyboards.keyboards import main_menu_keyboard, first_keyboard, first_text, MAIN_MENU_MESSAGE
from handlers import register_handlers_profile, register_handlers_settings, register_handlers_todo, register_handlers_avito
from utils.event_isolation import CustomEventIsolation
from db.database import init_db, add_user, get_user
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class UserForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_direction = State()

load_dotenv()
TOKEN = os.getenv('API_TOKEN')

init_db()

bot = Bot(
    token=TOKEN,
    session=AiohttpSession(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

events_isolation = CustomEventIsolation()
dp.update.middleware(FSMContextMiddleware(storage=MemoryStorage(), events_isolation=events_isolation))

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

async def send_welcome(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id)
    if user is None:
        await state.update_data(name=message.from_user.id)
        await message.answer_photo(
            photo=FSInputFile('/home/killmilk/WM-dev/WebMindTryBot/images/2.jpg'),
            caption=first_text(),
            reply_markup=first_keyboard())
        await state.set_state(UserForm.waiting_for_direction)
    else:
        await message.answer_animation(
            animation=FSInputFile('/home/killmilk/WM-dev/WebMindStaffBot/images/1.mp4'),
            reply_markup=main_menu_keyboard()
            )

@dp.message(Command(commands=["start", "help"]))
async def handle_start_help(message: types.Message, state: FSMContext):
    await send_welcome(message, state)



@dp.callback_query(lambda c: c.data in ['dir_code', 'dir_design', 'dir_photo'], UserForm.waiting_for_direction)
async def process_direction(callback_query: types.CallbackQuery, state: FSMContext):
    direction_map = {
        'dir_code': 'Code',
        'dir_design': 'Design',
        'dir_photo': 'Photo'
    }
    direction = direction_map[callback_query.data]
    user_data = callback_query.from_user.full_name
    print(user_data, "MAIN")
    add_user(callback_query.from_user.id, user_data, direction)
    await state.clear()
    await bot.delete_message( 
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
        )
    await callback_query.message.answer_animation(
        animation=FSInputFile('/home/killmilk/WM-dev/WebMindStaffBot/images/1.mp4'),
        reply_markup=main_menu_keyboard()
        )

async def main() -> None:
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
