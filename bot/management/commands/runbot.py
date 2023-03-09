from django.core.management import BaseCommand
from django.conf import settings
import uvicorn

from bot.misc import dp, bot, on_startup, on_shutdown


class Command(BaseCommand):
    def handle(self, *args, **options):
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        if settings.BOT_WEBHOOK:
            uvicorn.run(
                app='main.asgi:application',
            )
        else:
            dp.run_polling(bot)

