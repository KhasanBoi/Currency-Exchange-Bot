import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5092633868:AAGe8bjrGo1k4X78XOrB-xq9MCl-KiZgFug'
url = 'https://v6.exchangerate-api.com/v6/a9bacf51ad20839f4bf9adda/latest/USD'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)  # check bot for new messages and requests and connects with backend

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Welcome to our bot')



@dp.message_handler()
async def exchange(message: types.Message):
        print('hello')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)