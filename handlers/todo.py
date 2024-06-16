from aiogram import Dispatcher, types

def register_handlers_todo(dp: Dispatcher):
    dp.callback_query.register(todo_menu, lambda c: c.data == 'todo')
    dp.callback_query.register(back_to_main, lambda c: c.data == 'back_to_main')

async def todo_menu(callback_query: types.CallbackQuery):
    await callback_query.answer("Todo event handled")

async def back_to_main(callback_query: types.CallbackQuery):
    from keyboards.keyboards import main_menu_keyboard, MAIN_MENU_MESSAGE
    await callback_query.message.edit_text(MAIN_MENU_MESSAGE, reply_markup=main_menu_keyboard())
