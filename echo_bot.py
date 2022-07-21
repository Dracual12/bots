from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import logging
from aiogram.utils import executor

token = '5347933446:AAHxVHEBWLskMr0RaOKfSJP8TgdgYq2adDc'
bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await message.answer('Это не текст')


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer('Напиши мне что-нибудь')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
