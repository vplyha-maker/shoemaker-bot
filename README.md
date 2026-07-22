# 👞 Shoemaker Bot — Telegram-бот для майстрів взуття

Інтерактивний Telegram-бот, який надає професійну довідкову інформацію про конструкції, матеріали, технології та інструменти для виробництва взуття. Бот підтримує **російську** та **українську** мови.

## 🎯 Можливості

- 📐 **Розміри, мірки та ортопедія**
- 👞 **Фасони і конструкції взуття**
- 🧪 **Матеріали і хімічні реагенти**
- 🎨 **Кольори і колористика**
- 🧮 **Калькулятори і конвертери**
- 🧼 **Реставрація та догляд**
- 🛠️ **Інструменти і техніка безпеки**
- 🧩 **Експрес-помічник** (підбір склейки, чек-листи)
- 📖 **Глосарій професійних термінів**
- 👥 **Спільнота майстрів**

---

## 🚀 Швидкий старт

### Передумови

- Python 3.10+
- Git
- Telegram аккаунт
- Telegram Bot Token (від [@BotFather](https://t.me/botfather))

### Установка

1. **Клонуй репозиторій**
```bash
git clone https://github.com/vplyha-maker/shoemaker-bot.git
cd shoemaker-bot
```

2. **Створи віртуальне оточення**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# або
venv\Scripts\activate  # Windows
```

3. **Встанови залежності**
```bash
pip install -r requirements.txt
```

4. **Створи файл `.env` в корені проекту**
```env
BOT_TOKEN=твій_токен_від_botfather
WEBHOOK_URL=https://твій-домен.com  # Опціонально (для Render використовується автоматично)
```

5. **Запусти бота**
```bash
python main.py
```

---

## 📦 Залежності

```
aiogram==3.13.0          # Telegram Bot Framework
aiohttp==3.10.0          # Асинхронний HTTP клієнт
python-dotenv==1.0.1     # Управління змінними окружения
pydantic==2.8.2          # Валідація даних
```

---

## 🏗️ Архітектура проекту

```
shoemaker-bot/
├── main.py                      # Точка входу, ініціалізація Webhook
├── config.py                    # Конфігурація (BOT_TOKEN)
├── keyboards.py                 # Клавіатури для Telegram (~295 рядків)
├── requirements.txt             # Залежності Python
├── .env                         # Змінні окружения (НЕ комітувати!)
│
├── handlers/                    # Обробники команд і callback'ів
│   ├── __init__.py
│   ├── base.py                  # /start команда, вибір мови
│   ├── main_menu.py             # Головне меню
│   ├── styles.py                # Фасони і силуети (3.3 KB)
│   ├── materials.py             # Матеріали і полімери (3.4 KB)
│   ├── colors.py                # Кольори і колористика (3.6 KB)
│   ├── constructions.py         # Конструкції взуття (1.7 KB)
│   ├── glossary.py              # Глосарій термінів (1.9 KB)
│   └── assistant.py             # Експрес-помічник (4.7 KB)
│
├── texts/                       # База знань (текстовий контент)
│   ├── __init__.py
│   ├── styles_texts.py          # Вся інформація про фасони (14.1 KB)
│   ├── materials_texts.py       # Матеріали взуття (16.8 KB)
│   ├── chemistry_texts.py       # Хімічні реагенти (19.3 KB)
│   ├── colors_texts.py          # Колористика (11 KB)
│   ├── constructions_texts.py   # Методи конструювання (8.4 KB)
│   ├── glossary_texts.py        # Термінологія (10 KB)
│   └── assistant_texts.py       # Контент помічника (15.2 KB)
│
├── utils/                       # Утилітарні функції
│   ├── __init__.py
│   └── keepalive.py             # Keep-alive механізм для Render
│
└── LICENSE                      # MIT License
```

---

## 📝 Структура коду

### **main.py** — Основний файл
```python
# Ініціалізація бота і диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Webhook конфігурація
WEBHOOK_URL = "https://shoemaker-bot.onrender.com"

# Реєстрація обробників
register_main_menu_handlers(dp)
register_styles_handlers(dp)
# ... і т.д.

# Запуск веб-сервера на порту 10000
```

### **keyboards.py** — Клавіатури
Містить функції для створення інтерактивних кнопок:
```python
get_language_keyboard()              # Вибір мови РУ/УК
get_main_menu(lang="ru")            # Головне меню (12+ кнопок)
get_styles_constructions_keyboard() # Підменю фасонів
get_materials_chemistry_keyboard()  # Матеріали & Хімія
# ... і багато інших
```

### **handlers/** — Обробники
Кожен handler реєструє callback-функції для обробки натискань на кнопки:
```python
def register_main_menu_handlers(dp):
    dp.callback_query.register(menu_callback_handler, ...)

@router.callback_query(F.data.startswith("style_cat_"))
async def style_category_handler(query: CallbackQuery, state: FSMContext):
    # Обробка натиску на кнопку
```

### **texts/** — База знань
Словники з інформацією для кожного розділу:
```python
STYLES_TEXTS = {
    "classic_oxford": {
        "ru": "Оксфорд — класичний чоловічий напівчеревик...",
        "uk": "Оксфорд — класичний напівчеревик..."
    },
    # ... більше записів
}
```

---

## 🌐 Розгортання

### На Render.com (Рекомендується)

1. **Виштовхни код на GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Створи новий Service на [render.com](https://render.com)**
   - Обери Git репозиторій
   - Runtime: Python 3.10
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Port: 10000

3. **Встав змінні окружения**
   - `BOT_TOKEN` — твій токен від @BotFather
   - `WEBHOOK_URL` — автоматично встановлюється Render URL

4. **Deploy!** 🚀

### Локально (Для розробки)

```bash
# Встанови змінні окружения
export BOT_TOKEN="твій_токен"

# Запусти
python main.py
```

**Примітка:** Локальний запуск не буде мати webhook, використовуй polling замість цього.

---

## 🔐 Безпека

⚠️ **ВАЖЛИВО:**
- **НІКОЛИ** не комітуй `.env` файл з токеном!
- Додай `.env` в `.gitignore`
- Кожен розробник повинен мати свій BOT_TOKEN

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## 📚 API Документація

### Команди бота

| Команда | Описание |
|---------|---------|
| `/start` | Почати роботу, вибір мови |
| Кнопки меню | Навігація по розділам |

### Структура callback_data

Бот використовує `callback_data` для навігації:
- `lang_ru` / `lang_uk` — вибір мови
- `menu_*` — головне меню розділи
- `sub_*` — підменю
- `back_to_main` — повернення в головне меню

---

## 🧪 Розробка

### Додавання нового розділу

1. **Створи файл з текстами** `texts/new_section_texts.py`
```python
NEW_SECTION_TEXTS = {
    "item_1": {
        "ru": "Російський текст",
        "uk": "Український текст"
    }
}
```

2. **Створи handler** `handlers/new_section.py`
```python
from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == "menu_new_section")
async def new_section_handler(query: CallbackQuery):
    await query.message.edit_text("...")
```

3. **Зареєструй в main.py**
```python
from handlers.new_section import register_new_section_handlers

register_new_section_handlers(dp)
```

---

## 🐛 Відладка

### Логування

Бот виводить логи в консоль:
```
2024-01-15 10:30:45 - INFO - ✅ Webhook установлен: https://...
2024-01-15 10:30:46 - INFO - 🚀 Сервер запущен на порту 10000
```

### Keep-Alive на Render

Файл `utils/keepalive.py` автоматично робить ping кожні 5 хвилин для запобігання "засинанню" безплатного Render сервіса.

---

## 📊 Статистика коду

- **Всього рядків:** ~2,500+
- **Обробників:** 8 основних
- **Текстового контенту:** ~100 KB
- **Кнопок клавіатури:** 100+
- **Підтримуваних мов:** 2 (РУ/УК)

---

## 🤝 Внесок

Якщо хочеш добавити новий контент або поліпшити бота:

1. Fork репозиторій
2. Створи гілку (`git checkout -b feature/amazing-feature`)
3. Зроби commit (`git commit -m 'Add amazing feature'`)
4. Push в гілку (`git push origin feature/amazing-feature`)
5. Відкрий Pull Request

---

## 📝 Ліцензія

Цей проект ліцензіюється під MIT License — див. файл [LICENSE](LICENSE).

---

## 📞 Контакти

- GitHub: [@vplyha-maker](https://github.com/vplyha-maker)
- Telegram Bot: [@shoemaker_bot](https://t.me/your_bot_username)

---

## 🎓 Корисні ресурси

- [Aiogram 3 Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [@BotFather](https://t.me/botfather) — Telegram Bot Manager
- [Render Deployment](https://render.com/)

---

**Розроблено з ❤️ для майстрів взуття** 👞

Якщо бот був корисним, не забудь поставити ⭐ на GitHub!
