import os
import traceback

import django
from asgiref.sync import ThreadSensitiveContext
from django.conf import settings
from django.core.asgi import ASGIHandler as _ASGIHandler
from django.utils.module_loading import import_string

from main.settings.base import DJANGO_SETTINGS_MODULE


class ASGIHandler(_ASGIHandler):
    async def __call__(self, scope, receive, send):
        assert scope["type"] in ("http", "lifespan")
        if scope["type"] == "lifespan":
            await self.lifespan(scope, receive, send)
            return
        async with ThreadSensitiveContext():
            await self.handle(scope, receive, send)

    @staticmethod
    async def lifespan(scope, receive, send):
        lifespan_context = import_string(settings.LIFESPAN_CONTEXT)
        started = False
        await receive()
        try:
            async with lifespan_context():
                await send({"type": "lifespan.startup.complete"})
                started = True
                await receive()
        except BaseException:
            exc_text = traceback.format_exc()
            if started:
                await send({"type": "lifespan.shutdown.failed", "message": exc_text})
            else:
                await send({"type": "lifespan.startup.failed", "message": exc_text})
            raise
        else:
            await send({"type": "lifespan.shutdown.complete"})


def get_asgi_application():
    """
    The public interface to Django's ASGI support. Return an ASGI 3 callable.

    Avoids making django.core.handlers.ASGIHandler a public API, in case the
    internal implementation changes or moves in the future.
    """
    django.setup(set_prefix=False)
    return ASGIHandler()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

application = get_asgi_application()
