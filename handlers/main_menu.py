from aiogram import types, F
from aiogram import Router

from keyboards import get_main_menu
from handlers.base import user_language  # Подтянем язык из базы, чтобы заглушка была на нужном языке!

router = Router()

# Ловим всё на главное меню, КРОМЕ уже созданных и работающих разделов
@router.callback_query(
    F.data.startswith("menu_") & 
    (F.data != "menu_styles") & 
    (F.data != "menu_chemistry") &
    (F.data != "menu_colors") &
    (F.data != "menu_sizes") &        # <--- Добавили исключение для Размеров
    (F.data != "menu_glossary") &
    (F.data != "menu_helper") &
    (F.data != "menu_calculators")
)
async def process_main_menu(callback: types.CallbackQuery):
    """Обработка нажатий на главное меню для разделов-заглушек"""
    section = callback.data.split('_')[1]
    
    # Берем реальный язык пользователя, а не хардкодный "ru"
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = (
        f"📌 *Раздел находится в разработке.*\n\Скоро здесь появятся материалы!"
        if lang == "ru" else
        f"📌 *Розділ знаходиться в розробці.*\n\nНезабаром тут з'являться матеріали!"
    )
    
    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


def register_main_menu_handlers(dp):
    dp.include_router(router)
