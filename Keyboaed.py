import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да'), KeyboardButton(text='Нет')]
], resize_keyboard=True)

One = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рига'), KeyboardButton(text='Париж')],
    [KeyboardButton(text='Прага'), KeyboardButton(text='Вильнюс')]
], resize_keyboard=True)

Two = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Wolk'), KeyboardButton(text='Work')],
    [KeyboardButton(text='Vowl'), KeyboardButton(text='Wolf')]
], resize_keyboard=True)

Three = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мики и Маус'), KeyboardButton(text='Джордж и Джеймс')],
    [KeyboardButton(text='Джесика и Алекс'), KeyboardButton(text='Филипп и Дрисс')]
], resize_keyboard=True)

Four = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='«Spider-Verse» (Паучьи миры)'), KeyboardButton(text='«Spider-Woman» (Женщина паук)')],
    [KeyboardButton(text='«The Amazing Spider-Man» (Удивительный Человек-паук)'),
     KeyboardButton(text='«Spider-Man; Noir» (Человек-Паук: Нуар)')]
], resize_keyboard=True)

Fife = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Павел Дуров'), KeyboardButton(text='РКН')],
    [KeyboardButton(text='Николай Дуров'), KeyboardButton(text='ОАЭ')]
], resize_keyboard=True)

End = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать заново')]
], resize_keyboard=True)
