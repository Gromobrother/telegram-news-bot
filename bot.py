import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Получаем токен бота и ID канала из переменных Railway
BOT_TOKEN = os.getenv("7615379082:AAF2rS8mU_UfUGzBUH2Opb-83gCw1t_BGv8")
CHANNEL_ID = os.getenv("@news_iz_uz")

# Инициализируем бота
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

async def send_news():
    while True:
        # Заглушка (сюда вставим парсинг новостей)
        news_text = "🚀 Новая новость!\n🔹 Это тестовое сообщение, заменим его на реальную новость."
        news_photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/480px-No_image_available.svg.png"
        
        # Отправка новости
        await bot.send_photo(CHANNEL_ID, photo=news_photo, caption=news_text)
        
        # Ждём 5 часов перед следующей отправкой
        await asyncio.sleep(5 * 60 * 60)

# Запуск бота
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(send_news())
    executor.start_polling(dp, skip_updates=True)
