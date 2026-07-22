from aiogram import types, F
from aiogram import Router

from keyboards import get_main_menu

router = Router()

@router.callback_query(F.data.startswith("menu_"))
async def process_main_menu(callback: types.CallbackQuery):
    """Обработка нажатий на главное меню"""
    section = callback.data.split('_')[1]
    
    # ЕСЛИ РАЗДЕЛ УЖЕ РЕАЛИЗОВАН — ПРОПУСКАЕМ ЕГО, 
    # чтобы сработал его собственный файл-обработчик (например, handlers/styles.py)
    if section == "styles":
        return
    
    # Для остальных пока еще нереализованных разделов оставляем заглушку
    lang = "ru" # Здесь можно будет тоже подтягивать язык, если нужно
    text = f"📌 **Раздел:** {section.upper()}\n\nКонтент в разработке..."
    
    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


def register_main_menu_handlers(dp):
    dp.include_router(router)
