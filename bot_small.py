from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.obj.peer_id==195310233:
        vk.messages.send(
            user_id=195310233,
            random_id=get_random_id(),
            message='Привет')
