from aiogram import types
from aiogram import Router
from aiogram.filters import Text

from keyboards import get_main_menu

router = Router()

@router.callback_query(Text(startswith="menu_"))
async def process_main_menu(callback: types.CallbackQuery):
    """Обработка нажатий на главное меню"""
    section = callback.data.split('_')[1]
    
    text = f"Раздел: {section.upper()}"   # временная заглушка
    
    await callback.message.edit_text(
        text,
        reply_markup=get_main_menu(user_language.get(callback.from_user.id, "ru"))
    )
    await callback.answer()


# Функция регистрации (будем использовать в main.py)
def register_main_menu_handlers(dp):
    dp.include_router(router)
