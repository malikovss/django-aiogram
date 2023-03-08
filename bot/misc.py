from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from django.conf import settings

from bot.routers import router

dp = Dispatcher()
bot_session = AiohttpSession()

bot = Bot(settings.BOT_TOKEN, parse_mode='HTML', session=bot_session)

dp.include_router(router)


async def on_startup():
    pass


async def on_shutdown():
    await bot_session.close()
