from aiogram.types import (InlineKeyboardButton, WebAppInfo, 
                           InlineKeyboardButton, Message)
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = 'EnterYourToken'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

web_app = WebAppInfo(url="https://eda.yandex.ru/moscow?shippingType=delivery")
keyboard = InlineKeyboardBuilder()
button = InlineKeyboardButton(text="Открыть Web App", web_app=web_app)
keyboard.add(button)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Нажмите на кнопку',
        reply_markup=keyboard.as_markup()
    )

if __name__ == '__main__':
    dp.run_polling(bot)
