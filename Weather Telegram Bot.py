import datetime
import requests
from pprint import pprint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = "openweathermap token"
bot = Bot("Your bot token")

dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_command (message: types.Message):
    await message.reply('Привет. Напиши название города и узнай текущую погоду.')

@dp.message_handler()
async def get_weather(message: types.Message):
     try:
         r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&lang=ru&units=metric")
         data = r.json()


         city = data ['name']
         cur_weather = data ['main']['temp']
         wind = data ['wind']['speed']

         await message.reply(f"*** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
         f'Погода в городе:  {city}\nТемпература: {cur_weather} C\n'f'Ветер:{wind} м/с')

     except:
        await message.reply('Проверь название города.')


if __name__ == "__main__":
    # main()

    executor.start_polling(dp)