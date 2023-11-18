from aiogram import types
from aiogram.filters import Command

from loader import dp, bot

@dp.message(Command(commands='help'))
async def help_handler(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    await message.answer("\n".join(text))