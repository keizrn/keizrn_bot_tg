from aiogram.utils.keyboard import ReplyKeyboardBuilder


def choose_calc():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Рациональные')
    keyboard_builder.button(text='Комплексные')
    keyboard_builder.button(text='Свободное выражение')
    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')


def choose_operation():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='a + b')
    keyboard_builder.button(text='a - b')
    keyboard_builder.button(text='a * b')
    keyboard_builder.button(text='a / b')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')


def choose_weather():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='По городу')
    keyboard_builder.button(text='По геолокации')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')


def take_geo():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')
