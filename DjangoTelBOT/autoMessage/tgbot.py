import requests
from .models import autoMessageItem

textItem_1 = autoMessageItem.objects.filter(id=1).values()
textItem_2 = autoMessageItem.objects.filter(id=2).values()

for x in textItem_1:
    valueItem_1 = x.__getitem__('text')

for x in textItem_2:
    valueItem_2 = x.__getitem__('text')

BOT_API_KEY = '6034340967:AAEVXgqWQbFF3WmpFW1NZvS9NTWAHOibpyM'
MY_CHANNEL_NAME = '@testDjangoTel'
MY_MESSAGE_TEXT_1 = valueItem_1
MY_MESSAGE_TEXT_2 = valueItem_2

def sendMessage_1():
    requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
    'chat_id': MY_CHANNEL_NAME,
    'text': MY_MESSAGE_TEXT_1
})
    
def sendMessage_2():
    requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
    'chat_id': MY_CHANNEL_NAME,
    'text': MY_MESSAGE_TEXT_2
})
