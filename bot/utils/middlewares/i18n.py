from aiogram import BaseMiddleware
from aiogram.types import Update
from django.utils.translation import activate
from django.conf import settings
from typing import Callable, Dict, Awaitable, Any, Optional
from users.models import User


class I18Middleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], 
                       event: Update, 
                       data: Dict[str, Any]
                       ) -> Any:
        
        user: Optional[User] = data.get('user', None)
        if user is None or user.language not in dict(settings.LANGUAGES):
            activate(settings.LANGUAGE_CODE)
        else:
            activate(user.language)
            
        return await handler(event, data)