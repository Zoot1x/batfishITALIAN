from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

plans_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔥 ACCESSO DI PROVA – GRATUITO", callback_data='free_sub')
    ],
    [
        InlineKeyboardButton(text="🔞 30 giorni di accesso VIP – $60", callback_data='vip_sub')
    ],
    [
        InlineKeyboardButton(text="👅 Accesso PREMIUM a vita – $200", callback_data='premium_sub')
    ]
])