from aiogram import Dispatcher, Bot
from aiogram.client.session.aiohttp import AiohttpSession
from django.conf import settings

from bot.helpers import get_webhook_url
from bot.routers import router
from bot.utils.storage import DjangoRedisStorage

dp = Dispatcher(storage=DjangoRedisStorage())
bot_session = AiohttpSession()

bot = Bot(settings.BOT_TOKEN, parse_mode='HTML', session=bot_session)

dp.include_router(router)


async def on_startup():
    if not settings.DEBUG:
        webhook_info = await bot.get_webhook_info()
        webhook_url = get_webhook_url()
        if webhook_url != webhook_info.url:
            await bot.set_webhook(
                url=webhook_url,
                allowed_updates=dp.resolve_used_update_types(),
                drop_pending_updates=True
            )


async def on_shutdown():
    await bot_session.close()
