from django.urls import path

from .views import process_update

urlpatterns = [
    path("<str:token>/", process_update, name='process-update')
]
