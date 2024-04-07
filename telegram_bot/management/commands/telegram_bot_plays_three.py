from django.core.management.base import BaseCommand
import time
from telegram import Bot
import requests
from bs4 import BeautifulSoup
import asyncio
from .bot_token import TOKEN, CHAT_ID

# Список трех игровых источников для получения новостей
game_sources = [
    'https://www.playground.ru/news/',
    'https://vgtimes.ru/news/',
    'https://www.goha.ru/news/'
]

sent_news_links = set()
current_round = 1


def get_news_link_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if url == 'https://www.playground.ru/news/':
        post_title = soup.find('div', {'class': 'post-title'})
        news_link = post_title.find('a')['href']
    elif url == 'https://vgtimes.ru/news/':
        news_container = soup.find('div', {'class': 'item-name type0'})
        news_link = news_container.find('a')['href']
    elif url == 'https://www.goha.ru/news/':
        news_container = soup.find('div', {'class': 'article-snippet__body'})
        news_link = news_container.find('a')['href']
    else:
        news_link = None

    if news_link:
        return news_link
    else:
        print(f"News link is empty on {url}")
        return None


async def send_news_link_to_channel(news_link):
    bot = Bot(token=TOKEN)
    chat_id = CHAT_ID
    if news_link:
        await bot.send_message(chat_id=chat_id, text=news_link)
    else:
        print("Error: News link is empty.")


class Command(BaseCommand):
    help = 'My custom command to run Telegram bot at specific times'

    def handle(self, *args, **options):
        global current_round
        loop = asyncio.get_event_loop()
        current_source_index = 0

        while True:
            url = game_sources[current_source_index]
            news_link = get_news_link_from_website(url)

            if news_link in sent_news_links:
                print(f"News link {news_link} has already been sent. Moving to the next source.")
                current_source_index = (current_source_index + 1) % len(game_sources)
                continue

            if current_round % 9 == 0 and url == 'https://www.playground.ru/news/':
                print(f"Skipping news link {news_link} from {url} after 9 rounds.")
            else:
                sent_news_links.add(news_link)
                loop.run_until_complete(send_news_link_to_channel(news_link))

            current_source_index = (current_source_index + 1) % len(game_sources)
            time.sleep(60)  # 300 секунд = 5 минут

            if current_round % 9 == 0:
                sent_news_links.clear()
                current_round = 1
            else:
                current_round += 1
