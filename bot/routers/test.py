from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from django.utils.translation import gettext_lazy as _

from bot.filters.states import Registration
from users.models import User

router = Router()


@router.message(Command("start"))
async def on_start(message: types.Message, user: User):
    await message.reply(
        _("Salom, {first_name}").format(first_name=user.first_name)
    )


@router.message(Command("registration"))
async def start_register_user(message: types.Message, state: FSMContext):
    await message.reply(str(_("Ismingizni kiriting:")))
    await state.set_state(Registration.first_name)


@router.message(Registration.first_name)
async def registration_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.reply(str(_("Familiyangizni kiriting:")))
    await state.set_state(Registration.last_name)


@router.message(Registration.last_name)
async def registration_finish(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(_("Ro'yhatga olish yakunlandi.")))
    await message.answer(
        _("Ism: {first_name}\n").format(first_name=data.get('first_name')) +
        _("Familiya: {last_name}\n").format(last_name=message.text),
    )
    await state.clear()
