"""
Система кеширования текстов для оптимизации производительности бота.
Загружает все текстовые данные в памяти при запуске и кеширует их,
вместо повторной загрузки с файлов.
"""

import logging
from typing import Dict, Any, Optional
from functools import lru_cache

logger = logging.getLogger(__name__)


class TextCache:
    """Менеджер кеша текстовых данных бота"""
    
    def __init__(self):
        self._cache: Dict[str, Any] = {}
        self._is_loaded = False
    
    def load_cache(self) -> None:
        """Загружает все текстовые данные в кеш при запуске бота"""
        if self._is_loaded:
            logger.info("⚡ Кеш уже загружен, пропускаем повторную загрузку")
            return
        
        try:
            logger.info("📦 Загружаю текстовые данные в кеш...")
            
            # Импортируем все текстовые модули
            from texts.styles_texts import STYLES_INTRO_RU, STYLES_INTRO_UK, TEXTS_RU as STYLES_TEXTS_RU, TEXTS_UK as STYLES_TEXTS_UK
            from texts.materials_texts import MATERIALS_INTRO_RU, MATERIALS_INTRO_UK, TEXTS_RU as MATERIALS_TEXTS_RU, TEXTS_UK as MATERIALS_TEXTS_UK
            from texts.chemistry_texts import CHEMISTRY_INTRO_RU, CHEMISTRY_INTRO_UK, TEXTS_RU as CHEMISTRY_TEXTS_RU, TEXTS_UK as CHEMISTRY_TEXTS_UK
            from texts.colors_texts import COLORS_INTRO_RU, COLORS_INTRO_UK, TEXTS_RU as COLORS_TEXTS_RU, TEXTS_UK as COLORS_TEXTS_UK
            from texts.constructions_texts import CONSTRUCTIONS_INTRO_RU, CONSTRUCTIONS_INTRO_UK, TEXTS_RU as CONSTRUCTIONS_TEXTS_RU, TEXTS_UK as CONSTRUCTIONS_TEXTS_UK
            from texts.glossary_texts import GLOSSARY_INTRO_RU, GLOSSARY_INTRO_UK, TEXTS_RU as GLOSSARY_TEXTS_RU, TEXTS_UK as GLOSSARY_TEXTS_UK
            from texts.assistant_texts import ASSISTANT_INTRO_RU, ASSISTANT_INTRO_UK, TEXTS_RU as ASSISTANT_TEXTS_RU, TEXTS_UK as ASSISTANT_TEXTS_UK
            
            # Кешируем интро-тексты
            self._cache["styles_intro"] = {"ru": STYLES_INTRO_RU, "uk": STYLES_INTRO_UK}
            self._cache["materials_intro"] = {"ru": MATERIALS_INTRO_RU, "uk": MATERIALS_INTRO_UK}
            self._cache["chemistry_intro"] = {"ru": CHEMISTRY_INTRO_RU, "uk": CHEMISTRY_INTRO_UK}
            self._cache["colors_intro"] = {"ru": COLORS_INTRO_RU, "uk": COLORS_INTRO_UK}
            self._cache["constructions_intro"] = {"ru": CONSTRUCTIONS_INTRO_RU, "uk": CONSTRUCTIONS_INTRO_UK}
            self._cache["glossary_intro"] = {"ru": GLOSSARY_INTRO_RU, "uk": GLOSSARY_INTRO_UK}
            self._cache["assistant_intro"] = {"ru": ASSISTANT_INTRO_RU, "uk": ASSISTANT_INTRO_UK}
            
            # Кешируем основные тексты (словари)
            self._cache["styles_texts"] = {"ru": STYLES_TEXTS_RU, "uk": STYLES_TEXTS_UK}
            self._cache["materials_texts"] = {"ru": MATERIALS_TEXTS_RU, "uk": MATERIALS_TEXTS_UK}
            self._cache["chemistry_texts"] = {"ru": CHEMISTRY_TEXTS_RU, "uk": CHEMISTRY_TEXTS_UK}
            self._cache["colors_texts"] = {"ru": COLORS_TEXTS_RU, "uk": COLORS_TEXTS_UK}
            self._cache["constructions_texts"] = {"ru": CONSTRUCTIONS_TEXTS_RU, "uk": CONSTRUCTIONS_TEXTS_UK}
            self._cache["glossary_texts"] = {"ru": GLOSSARY_TEXTS_RU, "uk": GLOSSARY_TEXTS_UK}
            self._cache["assistant_texts"] = {"ru": ASSISTANT_TEXTS_RU, "uk": ASSISTANT_TEXTS_UK}
            
            self._is_loaded = True
            logger.info("✅ Кеш успешно загружен! Все текстовые данные в памяти.")
            
        except Exception as e:
            logger.error(f"❌ Ошибка при загрузке кеша: {e}")
            raise
    
    def get_intro_text(self, section: str, lang: str = "ru") -> Optional[str]:
        """
        Получает интро-текст раздела из кеша
        
        Args:
            section: название раздела (styles, materials, chemistry, etc.)
            lang: язык (ru или uk)
        
        Returns:
            Текст или None если не найден
        """
        intro_key = f"{section}_intro"
        if intro_key not in self._cache:
            logger.warning(f"⚠️ Интро-текст '{intro_key}' не найден в кеше")
            return None
        
        return self._cache[intro_key].get(lang, "")
    
    def get_text(self, section: str, text_key: str, lang: str = "ru") -> Optional[str]:
        """
        Получает конкретный текст из раздела
        
        Args:
            section: название раздела (styles, materials, chemistry, etc.)
            text_key: ключ текста внутри раздела (style_cat_toe, mat_cat_leather, etc.)
            lang: язык (ru или uk)
        
        Returns:
            Текст или None если не найден
        """
        texts_key = f"{section}_texts"
        
        if texts_key not in self._cache:
            logger.warning(f"⚠️ Раздел '{texts_key}' не найден в кеше")
            return None
        
        texts_dict = self._cache[texts_key].get(lang, {})
        if text_key not in texts_dict:
            logger.warning(f"⚠️ Текст '{text_key}' не найден в разделе '{section}' для языка '{lang}'")
            return None
        
        return texts_dict.get(text_key, "")
    
    def get_all_texts(self, section: str, lang: str = "ru") -> Dict[str, str]:
        """
        Получает все тексты раздела
        
        Args:
            section: название раздела
            lang: язык (ru или uk)
        
        Returns:
            Словарь со всеми текстами раздела
        """
        texts_key = f"{section}_texts"
        
        if texts_key not in self._cache:
            logger.warning(f"⚠️ Раздел '{texts_key}' не найден в кеше")
            return {}
        
        return self._cache[texts_key].get(lang, {})
    
    def clear_cache(self) -> None:
        """Очищает кеш (используется при перезагрузке)"""
        self._cache.clear()
        self._is_loaded = False
        logger.info("🗑️ Кеш очищен")
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Возвращает статистику кеша"""
        sections = [key.replace("_intro", "").replace("_texts", "") for key in self._cache.keys()]
        sections = list(set(sections))
        
        return {
            "loaded": self._is_loaded,
            "sections": sections,
            "total_keys": len(self._cache),
            "memory_info": f"~{len(str(self._cache)) / 1024:.2f} KB"
        }


# Глобальный экземпляр кеша
text_cache = TextCache()


@lru_cache(maxsize=128)
def get_cached_intro(section: str, lang: str) -> Optional[str]:
    """
    Быстрое получение интро-текста с дополнительным LRU кешем
    Используется @lru_cache для еще более быстрого доступа
    """
    return text_cache.get_intro_text(section, lang)


@lru_cache(maxsize=256)
def get_cached_text(section: str, text_key: str, lang: str) -> Optional[str]:
    """
    Быстрое получение текста с дополнительным LRU кешем
    Используется @lru_cache для еще более быстрого доступа
    """
    return text_cache.get_text(section, text_key, lang)
