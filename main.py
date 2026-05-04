import asyncio
# Aiogram import
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberUpdated
# Our import
from cfg import *
from tools import *

dp = Dispatcher()

@dp.message(Command("start"))
async def commandStartHandler(message: Message):
    await message.answer("Hello! I'm a bot created with aiogram.")



@dp.my_chat_member()
async def botStatus(event: ChatMemberUpdated):
    new_status = event.new_chat_member.status
    chat_id = event.chat.id

    if new_status in ("left", "kicked"):
        await printAndLog("Бота удалили из:", chat_id)
        await printAndLog(f"ChatID {chat_id} был удалён из базы данных")



    elif new_status in ("member", "administrator"):
        await printAndLog("Бота добавили в:", chat_id)
        await printAndLog(f"ChatID {chat_id} был добален в базу данных")

async def mainEntry():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(mainEntry())