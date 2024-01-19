from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_after() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Купить химический набор")
    kb.button(text="Задать вопрос/Узнать статус заказа")
    kb.button(text="Групповые онлайн-занятия")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def exam_age():
    kb = ReplyKeyboardBuilder()
    kb.button(text="ОГЭ (8-9 класс)")
    kb.button(text="ЕГЭ (10-11 класс)")
    kb.button(text="<--В главное меню")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def cmd_special_buttons():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Запросить геолокацию", request_location=True),
    builder.button(text="Запросить контакт", request_contact=True)
    builder.button(text="<--В главное меню")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)