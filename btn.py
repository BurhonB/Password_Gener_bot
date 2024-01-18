from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)

    btn.row(KeyboardButton(text="🔒Parol yaratish"))
    btn.row(KeyboardButton(text="👤Administrator"))

    return btn


async def password_options_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


    btn.add(KeyboardButton(text="Easy"),
            KeyboardButton(text="Medium"),
            KeyboardButton(text="Hard"),
            KeyboardButton(text="🔙Ortga"))

    return btn