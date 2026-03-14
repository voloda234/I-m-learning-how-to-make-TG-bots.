from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


import app.keybords as kb
from app.states import chat, image
from app.generators import gpt_text, gpt_image
from app.database.request import set_user, get_user, calculate

from decimal import Decimal


user = Router()

@user.message(F.text == 'Отмена')
@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await message.answer('Добро пожаловать',reply_markup=kb.main)
    await state.clear()


@user.message(F.text == 'чат')
async def chatting(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balans) > 0:
        await state.set_state(chat.text)
        await message.answer('Введите ваш запрос', reply_markup=kb.cancel)
    else:
        await message.answer('не достаточно средст, пополните баланс')


@user.message(chat.text)
async def chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balans) > 0:
        await state.set_state(chat.wait)
        response = await gpt_text(message.text, 'gpt-4o-mini')
        await calculate(message.from_user.id, response['usege'], 'gpt-4o-mini')
        await message.answer(response['response'])
        await state.set_state(chat.text)
    else:
        await message.answer('не достаточно средст, пополните баланс')


@user.message(image.wait)
@user.message(chat.wait)
async def wait_wait(message: Message):
    await message.answer('Подожди')


@user.message(F.text == 'Генерация картинок')
async def chatting(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balans) > 0:
        await state.set_state(image.text)
        await message.answer('Введите ваш запрос', reply_markup=kb.cancel)
    else:
        await message.answer('не достаточно средст, пополните баланс')


@user.message(image.text)
async def chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balans) > 0:
        await state.set_state(image.wait)
        response = await gpt_image(message.text, 'dall-e-2')
        await calculate(message.from_user.id, response['usege'], 'dall-e-3')
        print(response)
        try:
            await message.answer_photo(photo=response['response'])
        except Exception as e:
            print(e)
            await message.answer(response['response'])
        await state.set_state(image.text)
    else:
        await message.answer('не достаточно средст, пополните баланс')


