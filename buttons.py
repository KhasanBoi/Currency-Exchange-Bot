from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('1')
btn2 = KeyboardButton('2')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)