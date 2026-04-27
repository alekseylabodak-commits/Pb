import asyncio
import Keyboaed as kb


from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Хочешь стать миллионером? \n '
                         'правила: необходимо правильно ответить на 5 вопросов подряд',
                         reply_markup=kb.main)


@dp.message(F.text == "Да")
async def one(message: Message):
    await message.answer('Круто! \n Балланс: 0 рублей \n '
                         'Первый вопрос: Какая столица Латвии?',
                         reply_markup=kb.One)


@dp.message(F.text == "Рига")
async def two(message: Message):
    await message.answer('Правильно! \n Балланс: 200.000 рублей \n '
                         'Второй вопрос: Как по английски будет работа?',
                         reply_markup=kb.Two)


@dp.message(F.text == "Work")
async def three(message: Message):
    await message.answer('Правильно! \n Балланс: 400.000 рублей \n '
                         'Третий вопрос: Какие имена у главных героев в фильме "1+1"?',
                         reply_markup=kb.Three)


@dp.message(F.text == "Филипп и Дрисс")
async def four(message: Message):
    await message.answer('Правильно! \n Балланс: 600.000 рублей \n Четвёртый вопрос: '
                         'Каким комиксом вдохновлён мультфильм «Человек-паук: Через вселенные» (2018)?',
                         reply_markup=kb.Four)


@dp.message(F.text == "«Spider-Verse» (Паучьи миры)")
async def fife(message: Message):
    await message.answer('Правильно! \n Балланс: 800.000 рублей \n Пятый вопрос: Кто владелец телеграм?',
                         reply_markup=kb.Fife)


@dp.message(F.text == "Павел Дуров")
async def end(message: Message):
    await message.answer('Ты победил! \n Балланс: 1.000.000 рублей',
                         reply_markup=kb.End)


@dp.message(F.text == "Начать заново")
async def cmd_clean_history(message: Message):
    for i in range(0, 101):
        try:
            await bot.delete_message(message.chat.id, message.message_id - i)
        except Exception:
            break


@dp.message(F.text == "Нет")
async def end(message: Message):
    await message.answer('Хорошо, приходи, когда будешь готов!',
                         reply_markup=kb.End)


@dp.message(F.text != "Начать заново" or "Павел Дуров" or "«Spider-Verse» (Паучьи миры)" or
            "Филипп и Дрисс" or "Work" or "Рига" or "Да" or "Нет")
async def note(message: Message):
    await message.answer('Ответ не правильный. Начать заново?',
                         reply_markup=kb.End)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
