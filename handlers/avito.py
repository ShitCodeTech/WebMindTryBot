from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram import Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from keyboards.keyboards import (
    avito_initial_message, avito_direction_message, avito_link_message,
    avito_contact_message, avito_password_message, avito_success_message,
    back_to_main_keyboard, direction_keyboard, skip_contact_keyboard, skip_password_keyboard
)
from utils.utils import add_to_google_sheet  # Import from utils
from db.database import account_increment


# Define FSM states
class AvitoForm(StatesGroup):
    waiting_for_uid = State()
    waiting_for_username = State()
    waiting_for_direction = State()
    waiting_for_link = State()
    waiting_for_contact = State()
    waiting_for_password = State()

def register_handlers_avito(dp: Dispatcher):
    dp.callback_query.register(start_avito_dialog, lambda c: c.data == 'load_avito')
    dp.message.register(process_username, AvitoForm.waiting_for_username)
    dp.callback_query.register(process_direction, AvitoForm.waiting_for_direction)
    dp.message.register(process_link, AvitoForm.waiting_for_link)
    dp.message.register(process_contact, AvitoForm.waiting_for_contact)
    dp.message.register(process_password, AvitoForm.waiting_for_password)
    dp.callback_query.register(back_to_main, lambda c: c.data == 'back_to_main')
    dp.callback_query.register(skip_contact, lambda c: c.data == 'skip_contact')
    dp.callback_query.register(skip_password, lambda c: c.data == 'skip_password')

async def start_avito_dialog(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.edit_caption(caption=avito_initial_message(), reply_markup=back_to_main_keyboard())
    await state.set_state(AvitoForm.waiting_for_username)

async def process_username(message: types.Message, state: FSMContext):
    await state.update_data(uid=message.from_user.id)
    await state.update_data(username=message.text)
    await message.answer(avito_direction_message(), reply_markup=direction_keyboard())
    await state.set_state(AvitoForm.waiting_for_direction)

async def process_direction(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(direction=callback_query.data)
    await callback_query.message.edit_text(avito_link_message(), reply_markup=None)
    await state.set_state(AvitoForm.waiting_for_link)

async def process_link(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    msg = await message.answer(avito_contact_message(), reply_markup=skip_contact_keyboard(), parse_mode=ParseMode.HTML)
    await state.update_data(contact_message_id=msg.message_id)
    await state.set_state(AvitoForm.waiting_for_contact)

async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    data = await state.get_data()
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['contact_message_id'])
    msg = await message.answer(avito_password_message(), reply_markup=skip_password_keyboard(), parse_mode=ParseMode.HTML)
    await state.update_data(password_message_id=msg.message_id)
    await state.set_state(AvitoForm.waiting_for_password)

async def skip_contact(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback_query.message.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=data['contact_message_id'])
    await state.update_data(contact='*', password='*')
    user_data = await state.get_data()
    await state.clear()
    await store_data(callback_query.message, user_data)

async def process_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.bot.delete_message(chat_id=message.chat.id, message_id=data['password_message_id'])
    user_data = await state.get_data()
    user_data['password'] = message.text
    await state.clear()
    await store_data(message, user_data)

async def skip_password(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback_query.message.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=data['password_message_id'])
    user_data = await state.get_data()
    user_data['password'] = '*'
    await state.clear()
    await store_data(callback_query.message, user_data)


async def store_data(message: types.Message, user_data: dict):
    data = [
        user_data['uid'],
        user_data['username'],
        user_data['direction'],
        user_data['link'],
        user_data['contact'],
        user_data['password']
    ]
    add_to_google_sheet(data)
    account_increment(user_data['uid'])
    await message.answer_animation(
        animation=FSInputFile('./images/1.mp4'),
        caption=avito_success_message(), 
        reply_markup=back_to_main_keyboard()
        )

async def back_to_main(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if 'contact_message_id' in data:
        await callback_query.message.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    if 'password_message_id' in data:
        await callback_query.message.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await message.answer_animation(
        animation=FSInputFile('./images/1.mp4'),
        caption=avito_success_message(), 
        reply_markup=back_to_main_keyboard()
        )
    await state.clear()