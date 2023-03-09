from django.conf import settings
from django.urls import reverse


def get_webhook_url():
    host: str = settings.HOST
    if not host.endswith("/"):
        host += "/"
    return host + reverse(settings.BOT_WEBHOOK_PATH, args=(settings.BOT_TOKEN,))
