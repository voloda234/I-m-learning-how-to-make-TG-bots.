from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


import app.keybords as kb
from app.states import chat
from app.generators import gpt_text
from app.database.request import set_user, get_user

from decimal import Decimal


user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Добро пожаловать',reply_markup=kb.main)


@user.message(F.text == 'чат')
async def chatting(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balans) > 0:
        await state.set_state(chat.text)
        await message.answer('Введите ваш запрос')
    else:
        await message.answer('не достаточно средст, пополните баланс')


@user.message(chat.text)
async def chat_response(message: Message, state: FSMContext):
    await state.set_state(chat.wait)
    response = await gpt_text(message.text, 'gpt-4o-mini')
    await message.answer(response)
    await state.clear()


@user.message(chat.wait)
async def wait_wait(message: Message):
    await message.answer('Подожди')