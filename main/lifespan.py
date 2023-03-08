import contextlib

from bot.misc import (
    on_startup as bot_on_startup,
    on_shutdown as bot_on_shutdown
)


@contextlib.asynccontextmanager
async def lifespan_context():
    try:
        await bot_on_startup()
        yield
    finally:
        await bot_on_shutdown()
