from aiogram import types, F
from aiogram import Router

from keyboards import get_main_menu

router = Router()

# Ловим всё на главное меню, КРОМЕ готовых разделов ("menu_styles" и "menu_chemistry")
@router.callback_query(
    F.data.startswith("menu_") & 
    (F.data != "menu_styles") & 
    (F.data != "menu_chemistry") &
    (F.data != "menu_colors_coloristics") &
    
)
async def process_main_menu(callback: types.CallbackQuery):
    """Обработка нажатий на главное меню для разделов-заглушек"""
    section = callback.data.split('_')[1]
    
    lang = "ru"
    text = f"📌 **Раздел:** {section.upper()}\n\nКонтент в разработке..."
    
    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


def register_main_menu_handlers(dp):
    dp.include_router(router)


