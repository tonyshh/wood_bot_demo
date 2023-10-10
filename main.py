from aiogram import Bot, Dispatcher
from config import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()

if __name__ == '__main__':
    from bot import handlers
    dp.start_polling(skip_updates=True)
