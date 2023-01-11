from textwrap import dedent

from aiogram import Router
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message

from bot.const import START_POINTS, STAT_TEXT

flags = {"throttling_key": "stat"}
router = Router()

@router.message(commands="stat", flags=flags)
@router.message(Text(text=STAT_TEXT), flags=flags)
async def cmd_stat(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_score = user_data.get("score", START_POINTS)

    answer_text_template = """\
        Ваш счёт: <b>{user_score}</b>.
        """

    await message.answer(
        dedent(answer_text_template).format(
            user_score=user_score
        )
    )
