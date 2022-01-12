import logging
from aiogram import Bot, Dispatcher, executor, types

import buttons
import settings
from buttons import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, 'Welcome to our bot', reply_markup=buttons.menu)

@dp.message_handler()
async def exchange(message: types.Message):
        print('hello')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)