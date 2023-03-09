from django.conf import settings
from django.urls import reverse


def get_webhook_url():
    host: str = settings.HOST
    if host.endswith("/"):
        host = host[:-1]
    return host + reverse(settings.BOT_WEBHOOK_PATH, args=(settings.BOT_TOKEN,))
