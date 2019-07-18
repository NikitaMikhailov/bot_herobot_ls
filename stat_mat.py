from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll
import requests, vk_api

session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений

f=open('mat.txt','r')
dism={}
for line in f:
    if line in dism:
        dism[line]+=1
    else:
        dism[line]=1
print(dism)
f.close()
mat=[]
for i in dism:
    fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(i)[:-1:] + "&fields=bdate&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
    print(fio.text)
    first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
    last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
    mat.append(first_name+' '+last_name+' '+str(dism[i])+'\n')
print(mat)
mat=''.join(mat)
'''
vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    #keyboard=keyboard.get_keyboard(),
    message="Статистика мата\n"+mat
)
'''
vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    #keyboard=keyboardgor.get_keyboard(),
    message="Статистика мата\n"+mat
)