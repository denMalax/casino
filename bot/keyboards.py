from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.const import SPIN_TEXT, STAT_TEXT


def get_spin_keyboard():
    keyboard = [
        [KeyboardButton(text=SPIN_TEXT)],
        [KeyboardButton(text=STAT_TEXT)]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
