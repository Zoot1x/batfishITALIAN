from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
k_main =[
    [KeyboardButton(text="🚀 PERIODO DI PROVA 🚀")],
    [KeyboardButton(text='❤️ Piani'), KeyboardButton(text='👤 Abbonamento')],
    [KeyboardButton(text='🎁 Inserisci codice promozionale'), KeyboardButton(text='💌 I miei contatti')],
]

keyboard_main = ReplyKeyboardMarkup(keyboard=k_main, resize_keyboard=True)