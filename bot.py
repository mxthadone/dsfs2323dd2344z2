import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
TOKEN = '7336870106:AAFCdbMTWiAQMDEN41PyErEsf7Isks-L8o8'

# Создайте объект бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Функция для получения цены TON
def get_ton_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "toncoin", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("toncoin", {}).get("usd")

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Бот начал отслеживать цену TON. Обновления будут приходить каждые 3 секунды.")

    # Отправка цены каждые 3 секунды
    while True:
        price = get_ton_price()
        if price is not None:
            text = f"Текущая цена TON: ${price:.2f}"
            await bot.send_message(chat_id=message.chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
        await asyncio.sleep(3)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
