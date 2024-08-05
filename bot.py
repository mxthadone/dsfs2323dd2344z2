import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
TOKEN = '7336870106:AAFCdbMTWiAQMDEN41PyErEsf7Isks-L8o8'

# Получение токена из переменной окружения

# Создаём объект бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для получения цены TON
def get_ton_price():
    url = "https://api.coinpaprika.com/v1/price-converter?base_currency_id=ton-toncoin&quote_currency_id=usd-us-dollars&amount=1"
    response = requests.get(url)
    data = response.json()
    print(data)
    price= data['price']
    print(price)
    dt= data['quote_price_last_updated']
    print(dt)
    return [price,dt]
def get_ton_price2():
    while True:
        try:
            url = "https://api.coingecko.com/api/v3/coins/the-open-network"
            response = requests.get(url)
            data = response.json()
            print(data)
            price = data['market_data']['current_price']['usd']
            price3 = data['market_data']['current_price']['rub']
            price_change_24h = data['market_data']["price_change_percentage_24h"]
            price_change_7d = data['market_data']["price_change_percentage_7d"]
            price_change_30d = data['market_data']["price_change_percentage_30d"]
            print(price)
            return price, price3,price_change_24h,price_change_7d,price_change_30d
        except Exception as err:
            print(err)


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Бот начал отслеживать цену TON. Обновления будут приходить каждые 3 секунды.")
    while True:
        try:
            x1,x2,x3,x4,x5 = get_ton_price2()
            print(x1,x2,x3,x4,x5)
            if int(x3) < 0:
                one= f'🚬👵🏻 🔻{x3} '
            else:
                one= f'🥂 📈{x3}'
            if int(x4) < 0:
                one2= f'🚬👵🏻 🔻{x4} '
            else:
                one2= f'🥂 📈{x4}'
            if int(x5) < 0:
                one3= f'🚬👵🏻 🔻{x5} '
            else:
                one3= f'🥂 📈{x5}'
            text = f"<b>Текущая цена TON:</b>\n <code>\nUSD / {x1}\nRUB / {x2}\n\nStat24h -> {one}%\nStat7d -> {one2}%\nStat30d -> {one3}%</code>"
            await message.answer(text, parse_mode='HTML')
            await asyncio.sleep(16.66)
        except Exception as err:
            print(err)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
