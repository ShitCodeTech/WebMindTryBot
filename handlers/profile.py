from aiogram import Dispatcher, types
from keyboards.keyboards import profile_menu_keyboard, PROFILE_MENU_MESSAGE
from db.database import get_user

def register_handlers_profile(dp: Dispatcher):
    dp.callback_query.register(profile_menu, lambda c: c.data == 'profile')
    dp.callback_query.register(back_to_main, lambda c: c.data == 'back_to_main')

async def profile_menu(callback_query: types.CallbackQuery):
    user = get_user(callback_query.from_user.id)
    if user is not None:
        user_info = {
            "uid": user[0],
            "name": user[1],
            "direction": user[2],
            "accounts": user[3]
        }
    else:
        user_info = {
            "uid": callback_query.from_user.id,
            "name": callback_query.from_user.full_name,
            "direction": "unknown",
            "accounts": 0
        }

    message = PROFILE_MENU_MESSAGE.format(
        uid=user_info["uid"],
        name=user_info["name"],
        direction=user_info["direction"],
        accounts=user_info["accounts"]
    )
    await callback_query.message.edit_text(message, reply_markup=profile_menu_keyboard())

async def back_to_main(callback_query: types.CallbackQuery):
    from keyboards.keyboards import main_menu_keyboard, MAIN_MENU_MESSAGE
    await callback_query.message.edit_text(MAIN_MENU_MESSAGE, reply_markup=main_menu_keyboard())



