from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api, random




session = requests.Session()
vk_session = vk_api.VkApi(token='59d1581bbabeed832e089565cf41f6fafd6567c210f3b68075493e34e75aa6f4f4d854adaf036fd9e3604')
longpoll = VkBotLongPoll(vk_session, '183679552')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений


def mainfunc():

    try:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:

                fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                    event.obj.from_id) + "&fields=bdate&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
#195310233  51556033

                slovar_Katya=["Ну Пееееть","Ну Пееетяяя"]
                if event.from_chat and random.randint(0,2)==0 and event.obj.from_id==51556033 and len(event.obj.text.split(" "))>5:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message=slovar_Katya[random.randint(0,1)]
                    )

                if event.from_chat and random.randint(0,2)==0 and event.obj.text.find("Катя")!=-1 or event.obj.text.find("Катю")!=-1 or event.obj.text.find("Катей")!=-1 or event.obj.text.find("Катюха")!=-1:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message="Я тут!"
                    )

    except Exception as err:
        try:
            print(err,type(err))
            if str(err.find("Errno 2"))!=-1:
                vk.messages.send(
                    user_id=195310233,
                    random_id=get_random_id(),
                    message='Возникла ошибка ' + str(err) + ' в главном цикле программы сообщений Катибота, цикл перезапущен\nНа сообщении пользователя: '+first_name+' '+last_name+'\nC текстом сообщения: '+event.obj.text
                )
            mainfunc()
        except:
            print(err)

            vk.messages.send(
                user_id=195310233,
                random_id=get_random_id(),
                message='Возникла ошибка ' + str(err) + ' в главном цикле программы сообщений Катибота, цикл перезапущен\nОшибка без участия пользователя.'
            )
            mainfunc()


mainfunc()