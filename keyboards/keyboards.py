from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def first_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Code", callback_data='dir_code')],
        [InlineKeyboardButton(text="Design", callback_data='dir_design')],
        [InlineKeyboardButton(text="Photo", callback_data='dir_photo')]
    ])
    return keyboard


# Main Menu Keyboard
def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Profile', callback_data='profile'), InlineKeyboardButton(text='TODO(InProgress)', callback_data='todo')], [InlineKeyboardButton(text='Settings', callback_data='settings'), InlineKeyboardButton(text='Load Avito', callback_data='load_avito')]])
    return keyboard

# Profile Menu Keyboard
def profile_menu_keyboard():
#   InlineKeyboardButton(text="Back", callback_data='back_to_main')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Feature 1', callback_data='feature_1'), InlineKeyboardButton(text='Feature 2', callback_data='feature_2')], [InlineKeyboardButton(text='Feature 3', callback_data='feature_3'), InlineKeyboardButton(text='Feature 4', callback_data='feature_4')], [InlineKeyboardButton(text="Back", callback_data='back_to_main')]])
    return keyboard

# Settings Menu Keyboard
def settings_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Feature 1', callback_data='feature_1'), InlineKeyboardButton(text='Feature 2', callback_data='feature_2')], [InlineKeyboardButton(text='Feature 3', callback_data='feature_3'), InlineKeyboardButton(text='Feature 4', callback_data='feature_4')], [InlineKeyboardButton(text="Back", callback_data='back_to_main')]])
    return keyboard

# Avito Menu Keyboard
def avito_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Next", callback_data='next')],
        [InlineKeyboardButton(text="Back", callback_data='back_to_main')]
    ])
    return keyboard

# Back to Main Keyboard
def back_to_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back to Main Menu", callback_data='back_to_main')]
    ])
    return keyboard

# Skip Contact Keyboard
def skip_contact_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Skip", callback_data='skip_contact')],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data='back_to_main')]
    ])
    return keyboard

# Skip Password Keyboard
def skip_password_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Skip", callback_data='skip_password')],
        [InlineKeyboardButton(text="Back to Main Menu", callback_data='back_to_main')]
    ])
    return keyboard

# Direction Inline Keyboard
def direction_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Code", callback_data='code')],
        [InlineKeyboardButton(text="Design", callback_data='design')],
        [InlineKeyboardButton(text="Photo", callback_data='photo')]
    ])
    return keyboard

# Bot Replies
MAIN_MENU_MESSAGE = "Main Menu"
PROFILE_MENU_MESSAGE = "Profile Menu:\n\nInfo:\nTelegram UID: {uid}\nName: {name}\nDirection: {direction}\nLoaded Avito Accounts: {accounts}"
SETTINGS_MENU_MESSAGE = "Settings Menu: dsfjkljsdklfjklsdjklj;lkaf"
TODO_MENU_MESSAGE = "Todo Menu"
AVITO_MENU_MESSAGE = "Wanna load Avito Account?\n\nFirst of all get me the name of Account"

def avito_initial_message():
    return "Wanna load Avito Account?\n\nFirst of all, get me the name of the account"

def avito_direction_message():
    return "Send me the account's direction"

def avito_link_message():
    return "Send me the advertisement's link"

def avito_contact_message():
    return "Now send me the account's mail/phone\n\n<b>Optional</b>"

def avito_password_message():
    return "Send me the pass\n\n<b>Optional</b>"

def avito_success_message():
    return "Account data has been successfully saved!"

def first_text():
    return 'Wake up, Neo... \nThe Matrix has you... \nFollow the white rabbit. \n\nIt`s time to choose your side'