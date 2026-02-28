import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.admin import admin
from app.user import user


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(user, admin)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот завершил работу')