from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rassilk_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📢 Начать рассылку", callback_data="start_rassilka")
    ]
])