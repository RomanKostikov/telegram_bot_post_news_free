from django.http import HttpResponse
import requests
from telegram import Bot


def copy_news_to_channel(request):
    # Получаем новость с игрового сайта (здесь используется просто пример)
    response = requests.get('https://www.playground.ru/news')  # замените на реальный URL игрового сайта
    news = response.json()  # предполагается, что новость возвращается в формате JSON

    # Отправляем новость на ваш телеграм канал
    bot = Bot(token='AAGNxnKThlQ0oQOaRlQQkpkKmmSzp7WraIo')
    chat_id = 'https://t.me/dev_koplay'
    bot.send_message(chat_id=chat_id, text=news['title'] + '\n' + news['content'])

    return HttpResponse("Новость успешно скопирована и отправлена на канал")
