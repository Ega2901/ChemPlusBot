from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.afterstart import get_after, exam_age, cmd_special_buttons

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Привет это ChemBot, здесь вы можете купить необходимый набор реактивов для ЕГЭ",
        reply_markup=get_after()
    )

@router.message(F.text.lower() == "купить химический набор")
async def answer_yes(message: Message):
    await message.answer(
        "К какому экзамену готовитесь?",
        reply_markup=exam_age()
    )
    
@router.message(F.text.lower() == "<--в главное меню")
async def answer_yes(message: Message):
    await message.answer(
        "Привет это ChemBot, здесь вы можете купить необходимый набор реактивов для ЕГЭ",
        reply_markup=get_after()
    )
    
@router.message(F.text.lower() == "купить химический набор")
async def answer_yes(message: Message):
    await message.answer(
        "К какому экзамену готовитесь?",
        reply_markup=exam_age()
    )
@router.message(F.text.lower() == "огэ (8-9 класс)")
async def answer_yes(message: Message):
    await message.answer(
        "Введите данные для доставки:",
        reply_markup=cmd_special_buttons()
    )
@router.message(F.text.lower() == "егэ (10-11 класс)")
async def answer_yes(message: Message):
    await message.answer(
        "Введите данные для доставки:",
        reply_markup=cmd_special_buttons()
    )