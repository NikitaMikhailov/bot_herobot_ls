from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api
from datetime import datetime


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

for event in longpoll.listen():
    print("id чата, в который переслали сообщение: " + str(event.object.peer_id))
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        count=requests.get("https://api.vk.com/method/messages.getConversationMembers?peer_id="+str(event.object.peer_id)+"&group_id=178949259&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.101")
        print("количество участников беседы: "+str(count))
    if event.object.fwd_messages and event.object.text.find('В прошедшей битве команда'):
        print("id чата, в который переслали сообщение: "+str(event.object.peer_id))
        if event.object.text:
            print("текст, с которым переслали сообщение: "+event.object.text)
        else: print('сообщение переслано без текста')
        print("команда, на которую совершено нападение: "+event.object.fwd_messages[0]['text'].split(' ')[4][1::])
        print("заработано денег игроком: "+event.object.fwd_messages[0]['text'].split('\n')[3][:-2:])
        print("заработано vk_coin игроком: "+event.object.fwd_messages[0]['text'].split('\n')[4][:-2:])
        print("дата битвы: " + datetime.utcfromtimestamp(event.object.fwd_messages[0]['date']).strftime('%Y-%m-%d'))
        print("id игрока, переславшего сообщение: "+str(event.object.from_id))

#'date': 1564053846, 'from_id': -178949259, 'text': 'спасибо, что напомнил', 'attachments': [], 'conversation_message_id': 8184, 'peer_id': 195310233, 'id': 10804