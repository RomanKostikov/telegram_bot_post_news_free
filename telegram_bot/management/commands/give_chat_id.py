from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Get chat ID from Telegram channel'

    def handle(self, *args, **options):
        bot_token = 'your_bot_token_here'

        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')

        if response.status_code == 200:
            data = response.json()

            if 'result' in data and data['result']:
                chat_id = data['result'][0]['message']['chat']['id']
                self.stdout.write(f'Chat ID: {chat_id}')
            else:
                self.stdout.write('No new updates or chat ID found')
        else:
            self.stdout.write(f'Failed to get updates. Status code: {response.status_code}')
