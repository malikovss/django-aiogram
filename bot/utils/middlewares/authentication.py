from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Awaitable, Any
from users.models import User


class AuthenticationMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
                       event: Update,
                       data: Dict[str, Any]
                       ) -> Any:
        if event.message:
            bot_user = event.message.from_user
        elif event.callback_query:
            bot_user = event.callback_query.from_user
        elif event.inline_query:
            bot_user = event.inline_query.from_user
        elif event.chosen_inline_result:
            bot_user = event.chosen_inline_result.from_user
        elif event.shipping_query:
            bot_user = event.shipping_query.from_user
        elif event.pre_checkout_query:
            bot_user = event.pre_checkout_query.from_user
        else:
            return handler(event, data)

        user, _ = await User.objects.aget_or_create(telegram_id=bot_user.id,
                                                    defaults={
                                                        'first_name': bot_user.first_name,
                                                        'language': bot_user.language_code
                                                    })
        data['user'] = user

        return await handler(event, data)
