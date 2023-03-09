from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from django.conf import settings

from bot.routers import router

dp = Dispatcher()
bot_session = AiohttpSession()

bot = Bot(settings.BOT_TOKEN, parse_mode='HTML', session=bot_session)

dp.include_router(router)


async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if settings.BOT_WEBHOOK:
        webhook_url = f'{settings.BOT_WEBHOOK}/bot/{settings.BOT_TOKEN}/'
        if webhook_url != webhook_info:
            await bot.set_webhook(url=webhook_url)
    elif webhook_info.url:
        await bot.delete_webhook()


async def on_shutdown():
    await bot_session.close()
