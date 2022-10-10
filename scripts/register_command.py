import os
import requests


APP_ID = os.getenv('APP_ID')
GUILD_ID = os.getenv('GUILD_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')

def register():
    url = f'https://discord.com/api/v8/applications/{APP_ID}/guilds/{GUILD_ID}/commands'
    headers = {
        'Authorization': f'Bot {BOT_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'name': 'dummy',
        'type': 1,
        'description': 'Dummy command',
    }
    requests.post(url, headers=headers, data)

if __name__ == '__main__':
    register()
