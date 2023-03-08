import contextlib

from django.apps import AppConfig

from .misc import bot_session


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'


async def on_startup():
    pass


async def on_shutdown():
    await bot_session.close()


@contextlib.asynccontextmanager
async def lifespan_context():
    try:
        await on_startup()
        yield
    finally:
        await on_shutdown()
