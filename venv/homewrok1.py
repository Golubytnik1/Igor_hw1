# 12.01.2023
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from random import choice
import os

load_dotenv()

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text=f"Приветствую вас уважаемый {message.from_user.first_name}")
    await message.delete()

@dp.message_handler(commands=["help"])
async def star_command(message: types.Message):
    await message.answer(text=f"""
    Список команд: 
    start - старт бота
    help - список команд
    myinfo - информация обо мне
    picture - показать случайную картинку
                                """)
    await message.delete()

@dp.message_handler(commands=["myinfo"])
async def start_command(message: types.Message):
    await message.answer(text=f"""
    Ваш ID: {message.from_user.id}
    Ваше имя: {message.from_user.first_name}
    Ваш никнейм: {message.from_user.username}
                                """)

@dp.message_handler(commands=['picture'])
async def start_command(message: types.Message):
    photo = open('images/' + choice(os.listdir('images')), 'rb')
    await bot.send_photo(message.chat.id, photo)
    await message.delete()

@dp.message_handler()
async def start_command(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)