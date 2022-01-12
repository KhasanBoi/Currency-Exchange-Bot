from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('USD to UZS')
btn2 = KeyboardButton('UZS to USD')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)