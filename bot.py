import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from rfc3986.validators import check_password

from btn import *
from utils import *

BOT_TOKEN = "6969955344:AAEEokJqbXMZlrgfo8Uo4sbbii7pQUUxtvY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

async def command_menu(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Ishga tushirin'),
    ])


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    btn = await start_btn()
    await message.answer("Asalomu Aleykum", reply_markup=btn)





@dp.message_handler(text="🔒Parol yaratish")
async def password_generate_handler(message: types.Message):
    btn = await password_options_btn()
    await message.answer("Parol LEVELNI tanlang:", reply_markup=btn)



@dp.message_handler(text="👤Administrator")
async def bot_xaqida_handler(message: types.Message):
    btn = await start_btn()
    await message.answer("Admin Telegram https://t.me/Burhon_B", reply_markup=btn)


@dp.message_handler(text="🔙Ortga")
async def back_handler(message: types.Message):
    await start_bot(message)

@dp.message_handler(content_types=['text'])
async def get_password_options_handler(message: types.Message):
    text = message.text
    password = await generate_password(text)
    if password:
        crack_time_text = await check_password(password)
        await message.answer(f"Password: <code>{password}</code>\n<u>{crack_time_text}</u>")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=command_menu)


