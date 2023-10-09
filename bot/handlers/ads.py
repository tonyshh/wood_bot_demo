from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.db_utils import add_ad
from main import dp


class AdCreation(StatesGroup):
    waiting_for_description = State()
    waiting_for_price = State()

@dp.message_handler(Command("create_ad"))
async def create_ad_start(message: Message):
    await message.answer("Пожалуйста, отправьте описание вашего изделия.")
    await AdCreation.waiting_for_description.set()

@dp.message_handler(state=AdCreation.waiting_for_description)
async def enter_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Теперь укажите цену вашего изделия.")
    await AdCreation.waiting_for_price.set()

@dp.message_handler(state=AdCreation.waiting_for_price)
async def enter_price(message: Message, state: FSMContext):
    data = await state.get_data()
    description = data.get("description")
    
    add_ad(user_id=message.from_user.id, description=description, price=message.text)
    
    await message.answer("Ваше объявление успешно создано!", reply_markup=ReplyKeyboardRemove())
    await state.finish()


from database.db_utils import get_all_ads

@dp.message_handler(Command("show_ads"))
async def show_all_ads(message: Message):
    ads = get_all_ads()
    
    if not ads:
        await message.answer("На данный момент объявлений нет.")
        return
    
    ads_text = ""
    for user_id, description, price in ads:
        ads_text += f"User ID: {user_id}\nDescription: {description}\nPrice: {price}\n\n"
    
    await message.answer(ads_text)

