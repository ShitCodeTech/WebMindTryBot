from aiogram import Dispatcher, types
from keyboards.keyboards import settings_menu_keyboard, SETTINGS_MENU_MESSAGE

def register_handlers_settings(dp: Dispatcher):
    dp.callback_query.register(settings_menu, lambda c: c.data == 'settings')
    dp.callback_query.register(back_to_main, lambda c: c.data == 'back_to_main')

async def settings_menu(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(SETTINGS_MENU_MESSAGE, reply_markup=settings_menu_keyboard())

async def back_to_main(callback_query: types.CallbackQuery):
    from keyboards.keyboards import main_menu_keyboard, MAIN_MENU_MESSAGE
    await callback_query.message.edit_text(MAIN_MENU_MESSAGE, reply_markup=main_menu_keyboard())
