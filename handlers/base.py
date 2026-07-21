from aiogram import types

from keyboards import get_language_keyboard, get_main_menu

# Словарь для хранения выбранного языка пользователя
# Ключ - user_id, значение - "ru" или "uk"
user_language = {}


async def cmd_start(message: types.Message):
    """Запускается при команде /start"""
    user_id = message.from_user.id
    lang = user_language.get(user_id, "ru")   # по умолчанию русский

    if user_id not in user_language:
        # Если язык ещё не выбран — показываем выбор языка
        await message.answer(
            "🌍 **Оберіть мову / Выберите язык:**",
            reply_markup=get_language_keyboard(),
            parse_mode="Markdown"
        )
    else:
        # Если язык уже выбран — сразу показываем главное меню
        title = "🏛 **Главное меню «Энциклопедии Сапожника»**" if lang == "ru" else "🏛 **Головне меню «Енциклопедії Чоботаря»**"
        await message.answer(title, reply_markup=get_main_menu(lang), parse_mode="Markdown")


async def process_language(callback: types.CallbackQuery):
    """Обрабатывает нажатие на кнопку выбора языка"""
    user_id = callback.from_user.id
    lang = "ru" if callback.data == "lang_ru" else "uk"
    
    user_language[user_id] = lang   # сохраняем выбор

    text = "✅ Язык изменён на Русский" if lang == "ru" else "✅ Мову змінено на Українську"

    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()
