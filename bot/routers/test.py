from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def on_start(message: types.Message):
    await message.reply('hello world')
