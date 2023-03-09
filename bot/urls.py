from django.conf import settings
from django.urls import path

from .views import process_update

urlpatterns = [
    path("<str:token>/", process_update, name=settings.BOT_WEBHOOK_PATH)
]
