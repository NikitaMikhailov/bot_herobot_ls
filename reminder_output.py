from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import bs4, random, requests, vk_api
import datetime


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()

def sent_message(text, user_id):
    #print(text)
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=text
    )
try:
#/root/bot_herobot_ls/resurses/
    f=open('/root/bot_herobot_ls/resurses/zametki.txt',encoding='utf8')
    for line in f:
        zametka=line.split('***#***')
    #print(zametka)
        if line!='\n' and datetime.datetime.now().month==int(zametka[0]) and datetime.datetime.now().day==int(zametka[1]) and datetime.datetime.now().hour==int(zametka[2]) and datetime.datetime.now().minute==int(zametka[3]):
            sent_message('У меня есть для тебя напоминание:', int(zametka[5]))
            sent_message(zametka[4].capitalize(),int(zametka[5]))
except Exception as err:
    sent_message('Возникла ошибка ' + str(err) + ' в напоминаниях',195310233)
