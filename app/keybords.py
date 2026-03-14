from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='чат')],
    [KeyboardButton(text='Генерация картинок')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пунк меню'
)


cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отмена')]
], resize_keyboard=True)