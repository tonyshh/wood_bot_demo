from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from aiogram.types import ParseMode
from aiogram.utils import executor

import config
from bot import handlers  # Импорт наших обработчиков

API_TOKEN = config.API_TOKEN

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from bot import handlers  # Импортируем обработчики
    executor.start_polling(dp, skip_updates=True)
