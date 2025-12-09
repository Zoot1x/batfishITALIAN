from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

access_age_free_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎀 Ottieni", callback_data='age_check')
    ],
    [
        InlineKeyboardButton(text="⬅️ Indietro", callback_data='back_to_plans')
    ]
])

access_age_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💳 Paga", callback_data='age_check')
    ],
    [
        InlineKeyboardButton(text="⬅️ Indietro", callback_data='back_to_plans')
    ]
])