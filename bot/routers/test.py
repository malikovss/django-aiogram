from aiogram import Router, types
from aiogram.filters import Command
from django.utils.translation import gettext_lazy as _

from users.models import User

router = Router()


@router.message(Command("start"))
async def on_start(message: types.Message):
    await User.objects.aget_or_create(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await message.reply(
        _("Hello, {first_name}").format(first_name=message.from_user.first_name)
    )
