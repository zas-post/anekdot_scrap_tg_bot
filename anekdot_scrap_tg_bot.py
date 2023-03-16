from aiogram import Bot, Dispatcher, types
from config import tg_bot_token


bot = Bot(token=tg_bot_token)
dp =Dispatcher(bot)

@dp.message_handler(coma)
async def start(message: types.Message)
    await message.reply("Ti kto?")