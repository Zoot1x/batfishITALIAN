import asyncio
import time
import json
import re
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.command import Command
from texts.welcome import *
from keyboards.k_plans import plans_keyboard
from keyboards.k_main import keyboard_main
from keyboards.k_acces_age import access_age_free_keyboard, access_age_keyboard
from keyboards.k_rassilk import rassilk_keyboard
from collections import Counter
from fishbot import urlfish

# Создаем бота с увеличенным тайм-аутом
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

admin_id = 928304869
# Файл для хранения данных
USERS_FILE = 'users.json'

try:
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        if content:
            users_data = json.loads(content)
        else:
            users_data = {}
except FileNotFoundError:
    users_data = {}
    
@dp.message(Command('start'))
async def start(message: types.Message):
    user_id = str(message.from_user.id)
    language = message.from_user.language_code or "unknown"

    # Если пользователя ещё нет, добавляем
    if user_id not in users_data:
        users_data[user_id] = {"language": language}

        # Сохраняем в JSON
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, ensure_ascii=False, indent=4)
    try:
        photo = FSInputFile('media/welcome_img.jpg')
        await message.answer_photo(photo=photo, caption=welcome, parse_mode="HTML", reply_markup=keyboard_main, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await message.answer(welcome, parse_mode="HTML", reply_markup=keyboard_main)


@dp.message(lambda message: message.text == "❤️ Piani")
async def show_plans(message: types.Message):
    try:
        photo = FSInputFile('media/thourd.jpg')
        await message.answer_photo(photo=photo, caption=plans, reply_markup=plans_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await message.answer(plans, reply_markup=plans_keyboard)

@dp.message(lambda message: message.text == "🚀 PERIODO DI PROVA 🚀")
async def free_sub(message: types.Message):
    try:
        await message.delete()
    except:
        pass
    try:
        photo = FSInputFile('media/channel.jpg')
        await message.answer_photo(photo=photo, caption=free_plan, parse_mode="HTML", reply_markup=access_age_free_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await message.answer(free_plan, parse_mode="HTML", reply_markup=access_age_free_keyboard)
    
@dp.callback_query(F.data == 'free_sub')
async def free_sub(callback_query: types.CallbackQuery):
    try:
        await callback_query.message.delete()
    except:
        pass
    try:
        photo = FSInputFile('media/channel.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=free_plan, parse_mode="HTML", reply_markup=access_age_free_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await callback_query.message.answer(free_plan, parse_mode="HTML", reply_markup=access_age_free_keyboard)
    
@dp.callback_query(F.data == 'vip_sub')
async def vip_sub(callback_query: types.CallbackQuery):
    try:
        await callback_query.message.delete()
    except:
        pass
    try:
        photo = FSInputFile('media/channel.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=vip_plan, parse_mode="HTML", reply_markup=access_age_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await callback_query.message.answer(vip_plan, parse_mode="HTML", reply_markup=access_age_keyboard)
    
@dp.callback_query(F.data == 'premium_sub')
async def premium_sub(callback_query: types.CallbackQuery):
    try:
        await callback_query.message.delete()
    except:
        pass
    try:
        photo = FSInputFile('media/channel.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=premium_plan, parse_mode="HTML", reply_markup=access_age_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await callback_query.message.answer(premium_plan, parse_mode="HTML", reply_markup=access_age_keyboard)

@dp.callback_query(F.data == 'back_to_plans')
async def back(callback_query: types.CallbackQuery):
    try:
        await callback_query.message.delete()
    except:
        pass
    try:
        photo = FSInputFile('media/thourd.jpg')
        await callback_query.message.answer_photo(photo=photo, caption=plans, reply_markup=plans_keyboard, request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await callback_query.message.answer(plans, reply_markup=plans_keyboard)

@dp.message(lambda message: message.text == "👤 Abbonamento")
async def help(message: types.Message):
    await message.answer(text=subcribe, parse_mode="HTML")

@dp.message(lambda message: message.text == "🎁 Inserisci codice promozionale")
async def enter_promo_code(message: types.Message):
    await message.answer("Inserisci il codice promozionale:")


@dp.message(lambda message: message.text == "💌 I miei contatti")   
async def my_contacts(message: types.Message):
    await message.answer(text=contacts, parse_mode="HTML")


@dp.callback_query(F.data == 'age_check')
async def age_check(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="I'm 18", url=urlfish)],
        ]
    )
    try:
        photo = FSInputFile('media/second.jpg')
        await callback_query.message.answer_photo(
            photo=photo,
            caption=age_check_fish,
            reply_markup=keyboard,
            parse_mode="HTML",
            request_timeout=60)
    except Exception as e:
        print(f"Error sending photo: {e}")
        await callback_query.message.answer(
            age_check_fish,
            reply_markup=keyboard,
            parse_mode="HTML")
    
# Функция для загрузки пользователей из JSON
def load_users():
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Статистика бота
@dp.message(Command('rassilk'))
async def rassilk(message: types.Message):
    if message.from_user.id != admin_id:
        return  # только админ

    users_data = load_users()
    total_users = len(users_data)

    # Список языков пользователей
    countries_list = [v["language"] for v in users_data.values()]
    country_stats = Counter(countries_list)

    stats_text = "\n".join([f"{c}: {count}" for c, count in country_stats.items()])

    await message.answer(
        f"📊 Статистика бота:\n\n"
        f"Общее количество пользователей: {total_users}\n\n"
        f"По языкам:\n{stats_text}",
        reply_markup=rassilk_keyboard
    )

# Рассылка
@dp.callback_query(F.data == 'start_rassilka')
async def start_rassilka(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != admin_id:
        return  # только админ

    users_data = load_users()
    start_time = time.time()
    photo = FSInputFile('media/fifs.jpg')
    sent_count = 0

    for user_id_str in users_data.keys():
        try:
            await bot.send_photo(
                chat_id=int(user_id_str),  # ключи JSON — строки
                photo=photo,
                caption=rassilka,
                parse_mode="HTML",
                request_timeout=60
            )
            sent_count += 1
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id_str}: {e}")

    elapsed = time.time() - start_time
    await callback_query.message.answer(
        f"Рассылка завершена.\n📤 Отправлено сообщений: {sent_count}/{len(users_data)}\n⏱ Время выполнения: {elapsed:.2f} секунд"
    )
@dp.message()
async def enter_promo_code(message: types.Message):
    await message.answer("Codice promozionale non trovato")

# Запуск процесса поллинга новых апдейтов
async def main():
    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

