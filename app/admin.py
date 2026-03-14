from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext

from app.states import Newsletter
from app.database.request import get_users


admin = Router()


class Admin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in [6872962542]
    

@admin.message(Admin(), Command('newsletter'))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer('Введите рассылку')


@admin.message(Newsletter.message)
async def newslatter_massage(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Рассылка началась')
    users = await get_users()
    for user in users:
        try:
            await message.send_copy(chat_id=user.tg_id)
        except Exception as e:
            pass
    await message.answer('Рассылка завершенна')
    
