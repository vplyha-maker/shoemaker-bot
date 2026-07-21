from aiogram import types
from aiogram import Router
from aiogram.filters import F

from keyboards import get_main_menu

router = Router()

@router.callback_query(F.data.startswith("menu_"))
async def process_main_menu(callback: types.CallbackQuery):
    """Обработка нажатий на главное меню"""
    section = callback.data.split('_')[1]
    
    # Временная заглушка
    text = f"📌 **Раздел:** {section.upper()}\n\nКонтент в разработке..."
    
    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu("ru"),   # пока русский
        parse_mode="Markdown"
    )
    await callback.answer()


def register_main_menu_handlers(dp: Dispatcher):
    dp.include_router(router)
