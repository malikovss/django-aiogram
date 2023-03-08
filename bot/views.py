from .misc import dp, bot


async def process_update(request, token: str):
    if token == bot.token:
        update = request.body()
        await dp.feed_raw_update(bot, update)
