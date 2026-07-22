# 👞 Shoemaker Bot — Telegram-бот для мастеров обуви

Интерактивный Telegram-бот, который предоставляет профессиональную справочную информацию о конструкциях, материалах, технологиях и инструментах для производства обуви. Бот поддерживает **русский** и **украинский** языки.

## 🎯 Возможности

- 📐 **Размеры, мерки и ортопедия**
- 👞 **Фасоны и конструкции обуви**
- 🧪 **Материалы и химические реагенты**
- 🎨 **Цвета и колористика**
- 🧮 **Калькуляторы и конвертеры**
- 🧼 **Реставрация и уход**
- 🛠️ **Инструменты и техника безопасности**
- 🧩 **Экспресс-помощник** (подбор склейки, чек-листы)
- 📖 **Глоссарий профессиональных терминов**
- 👥 **Сообщество мастеров**

---

## 🚀 Быстрый старт

### Требования

- Python 3.10+
- Git
- Аккаунт Telegram
- Telegram Bot Token (от [@BotFather](https://t.me/botfather))

### Установка

1. **Клонируй репозиторий**
```bash
git clone https://github.com/vplyha-maker/shoemaker-bot.git
cd shoemaker-bot
```

2. **Создай виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установи зависимости**
```bash
pip install -r requirements.txt
```

4. **Создай файл `.env` в корне проекта**
```env
BOT_TOKEN=твой_токен_от_botfather
WEBHOOK_URL=https://твой-домен.com  # Опционально (для Render устанавливается автоматически)
```

5. **Запусти бота**
```bash
python main.py
```

---

## 📦 Зависимости

```
aiogram==3.13.0          # Telegram Bot Framework
aiohttp==3.10.0          # Асинхронный HTTP клиент
python-dotenv==1.0.1     # Управление переменными окружения
pydantic==2.8.2          # Валидация данных
```

---

## 🏗️ Архитектура проекта

```
shoemaker-bot/
├── main.py                      # Точка входа, инициализация Webhook
├── config.py                    # Конфигурация (BOT_TOKEN)
├── keyboards.py                 # Клавиатуры для Telegram (~295 строк)
├── requirements.txt             # Зависимости Python
├── .env                         # Переменные окружения (НЕ коммитить!)
│
├── handlers/                    # Обработчики команд и callback'ов
│   ├── __init__.py
│   ├── base.py                  # /start команда, выбор языка
│   ├── main_menu.py             # Главное меню
│   ├── styles.py                # Фасоны и силуэты (3.3 KB)
│   ├── materials.py             # Материалы и полимеры (3.4 KB)
│   ├── colors.py                # Цвета и колористика (3.6 KB)
│   ├── constructions.py         # Конструкции обуви (1.7 KB)
│   ├── glossary.py              # Глоссарий терминов (1.9 KB)
│   └── assistant.py             # Экспресс-помощник (4.7 KB)
│
├── texts/                       # База знаний (текстовый контент)
│   ├── __init__.py
│   ├── styles_texts.py          # Вся информация о фасонах (14.1 KB)
│   ├── materials_texts.py       # Материалы обуви (16.8 KB)
│   ├── chemistry_texts.py       # Химические реагенты (19.3 KB)
│   ├── colors_texts.py          # Колористика (11 KB)
│   ├── constructions_texts.py   # Методы конструирования (8.4 KB)
│   ├── glossary_texts.py        # Терминология (10 KB)
│   └── assistant_texts.py       # Контент помощника (15.2 KB)
│
├── utils/                       # Утилитарные функции
│   ├── __init__.py
│   └── keepalive.py             # Keep-alive механизм для Render
│
└── LICENSE                      # MIT License
```

---

## 📝 Структура кода

### **main.py** — Основной файл
```python
# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Webhook конфигурация
WEBHOOK_URL = "https://shoemaker-bot.onrender.com"

# Регистрация обработчиков
register_main_menu_handlers(dp)
register_styles_handlers(dp)
# ... и т.д.

# Запуск веб-сервера на порту 10000
```

### **keyboards.py** — Клавиатуры
Содержит функции для создания интерактивных кнопок:
```python
get_language_keyboard()              # Выбор языка РУ/УК
get_main_menu(lang="ru")            # Главное меню (12+ кнопок)
get_styles_constructions_keyboard() # Подменю фасонов
get_materials_chemistry_keyboard()  # Материалы & Химия
# ... и многие другие
```

### **handlers/** — Обработчики
Каждый handler регистрирует callback-функции для обработки нажатий на кнопки:
```python
def register_main_menu_handlers(dp):
    dp.callback_query.register(menu_callback_handler, ...)

@router.callback_query(F.data.startswith("style_cat_"))
async def style_category_handler(query: CallbackQuery, state: FSMContext):
    # Обработка нажатия на кнопку
```

### **texts/** — База знаний
Словари с информацией для каждого раздела:
```python
STYLES_TEXTS = {
    "classic_oxford": {
        "ru": "Оксфорд — классический полуботинок...",
        "uk": "Оксфорд — класичний напівчеревик..."
    },
    # ... больше записей
}
```

---

## 🌐 Развертывание

### На Render.com (Рекомендуется)

1. **Отправь код на GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Создай новый Service на [render.com](https://render.com)**
   - Выбери Git репозиторий
   - Runtime: Python 3.10
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Port: 10000

3. **Установи переменные окружения**
   - `BOT_TOKEN` — твой токен от @BotFather
   - `WEBHOOK_URL` — автоматически устанавливается URL Render

4. **Deploy!** 🚀

### Локально (Для разработки)

```bash
# Установи переменные окружения
export BOT_TOKEN="твой_токен"

# Запусти
python main.py
```

**Примечание:** Локальный запуск не будет иметь webhook, используй polling вместо этого.

---

## 🔐 Безопасность

⚠️ **ВАЖНО:**
- **НИКОГДА** не коммитий файл `.env` с токеном!
- Добавь `.env` в `.gitignore`
- Каждый разработчик должен иметь свой BOT_TOKEN

```gitignore
.env
venv/
__pycache__/
*.pyc
.DS_Store
```

---

## 📚 API Документация

### Команды бота

| Команда | Описание |
|---------|---------|
| `/start` | Начать работу, выбор языка |
| Кнопки меню | Навигация по разделам |

### Структура callback_data

Бот использует `callback_data` для навигации:
- `lang_ru` / `lang_uk` — выбор языка
- `menu_*` — разделы главного меню
- `sub_*` — подменю
- `back_to_main` — возврат в главное меню

---

## 🧪 Разработка

### Добавление нового раздела

1. **Создай файл с текстами** `texts/new_section_texts.py`
```python
NEW_SECTION_TEXTS = {
    "item_1": {
        "ru": "Русский текст",
        "uk": "Украинский текст"
    }
}
```

2. **Создай обработчик** `handlers/new_section.py`
```python
from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == "menu_new_section")
async def new_section_handler(query: CallbackQuery):
    await query.message.edit_text("Здесь твое сообщение...")
```

3. **Зарегистрируй в main.py**
```python
from handlers.new_section import register_new_section_handlers

register_new_section_handlers(dp)
```

---

## 🐛 Отладка

### Логирование

Бот выводит логи в консоль:
```
2024-01-15 10:30:45 - INFO - ✅ Webhook установлен: https://...
2024-01-15 10:30:46 - INFO - 🚀 Сервер запущен на порту 10000
```

### Keep-Alive на Render

Файл `utils/keepalive.py` автоматически робит ping каждые 5 минут для предотвращения "засыпания" бесплатного Render сервиса.

---

## 📊 Статистика кода

- **Всего строк:** ~2,500+
- **Обработчиков:** 8 основных
- **Текстового контента:** ~100 KB
- **Кнопок клавиатуры:** 100+
- **Поддерживаемых языков:** 2 (РУ/УК)

---

## 🤝 Контрибьют

Если хочешь добавить новый контент или улучшить бота:

1. Fork репозиторий
2. Создай ветку (`git checkout -b feature/amazing-feature`)
3. Сделай commit (`git commit -m 'Add amazing feature'`)
4. Push в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

---

## 📝 Лицензия

Этот проект лицензирован под MIT License — см. файл [LICENSE](LICENSE).

---

## 📞 Контакты

- GitHub: [@vplyha-maker](https://github.com/vplyha-maker)
- Telegram Bot: [@shoemaker_bot](https://t.me/your_bot_username)

---

## 🎓 Полезные ресурсы

- [Aiogram 3 Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [@BotFather](https://t.me/botfather) — Telegram Bot Manager
- [Render Deployment](https://render.com/)

---

**Разработано с ❤️ для мастеров обуви** 👞

Если бот был полезен, не забудь поставить ⭐ на GitHub!
