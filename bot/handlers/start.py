from aiogram import types
from aiogram.dispatcher import Command
from main import dp

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nЯ - бот для заказов изделий из дерева.")
