from django.core.management.base import BaseCommand
import time
from telegram import Bot
import requests
from bs4 import BeautifulSoup
import asyncio


def get_news_link_from_website():
    url = 'https://www.playground.ru/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    post_title = soup.find('div', {'class': 'post-title'})
    news_link = post_title.find('a')['href']
    return news_link


async def send_news_link_to_channel():
    bot = Bot(token='YOUR_BOT_TOKEN_HERE')
    chat_id = '-YOUR_CHAT_ID_HERE'
    news_link = get_news_link_from_website()
    await bot.send_message(chat_id=chat_id, text=news_link)


class Command(BaseCommand):
    help = 'My custom command to run Telegram bot at specific times'

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        while True:
            loop.run_until_complete(send_news_link_to_channel())
            time.sleep(300)  # 300 секунд = 5 минут
