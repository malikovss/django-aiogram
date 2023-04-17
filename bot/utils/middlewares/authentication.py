from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Awaitable, Any
from users.models import User


class AuthenticationMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
                       event: Update,
                       data: Dict[str, Any]
                       ) -> Any:
        bot_user = data['event_from_user']
        if bot_user is None:
            return await handler(event, data)

        user, _ = await User.objects.aget_or_create(telegram_id=bot_user.id,
                                                    defaults={
                                                        'first_name': bot_user.first_name,
                                                        'language': bot_user.language_code
                                                    })
        data['user'] = user

        return await handler(event, data)
