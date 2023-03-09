from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from django.utils.translation import gettext_lazy as _

from bot.filters.states import Registration
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


@router.message(Command("registration"))
async def start_register_user(message: types.Message, state: FSMContext):
    await message.reply("Enter your first name:")
    await state.set_state(Registration.first_name)


@router.message(Registration.first_name)
async def registration_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.reply("Enter your last name:")
    await state.set_state(Registration.last_name)


@router.message(Registration.last_name)
async def registration_finish(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer("Registration finished!")
    await message.answer(
        f"First name: {data.get('first_name')}\n"
        f"Last name: {message.text}\n"
    )
    await state.clear()
