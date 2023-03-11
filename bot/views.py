from .misc import dp, bot
import json
from django.http import HttpResponse


async def process_update(request, token: str):
    if token == bot.token:
        body_unicode = request.body.decode('utf-8')
        update = json.loads(body_unicode)
        await dp.feed_raw_update(bot, update)
        return HttpResponse(status=200)
    return HttpResponse(status=400)


process_update.csrf_exempt = True
