from django.core.management import BaseCommand

from bot.apps import on_startup, on_shutdown
from bot.misc import dp, bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        dp.run_polling(bot)
