from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='чат')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пунк меню'
)