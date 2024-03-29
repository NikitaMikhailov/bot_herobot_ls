#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -

from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random, requests, vk_api, os, bs4
from google_images_download import google_images_download
from lxml import html
import urllib.parse


dict = [".", ",", "!", "?", ")", "(", ":", ";", "'", ']', '[', '"']
dictan = [")", "(", ":", ";", "'", ']', '[', '"', '\\', 'n', '&', 'q', 'u', 'o', 't']
dict7 = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
dict8 = {'овен':'aries','телец':'taurus' ,'близнецы':'gemini' ,'рак':'cancer' ,'лев':'leo' ,'дева':'virgo' ,'весы':'libra' ,'скорпион':'scorpio' ,'стрелец':'sagittarius','козерог':'capricorn' ,'водолей':'aquarius' ,'рыбы':'pisces'}
kolresp = 0
attachments = []
chand = 0
flagtime = False
fltm1 = False
fltm2 = False
flaggoroscop=True

#защита от пидарасов


f=open('/root/bot_herobot_ls/token.txt','r')
token=f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений

def goroscop(bd_date):
    if bd_date[1] == '1':
        if int(bd_date[0]) < 20:
            return 'capricorn'
        else:
            return 'aquarius'
    if bd_date[1] == '2':
        if int(bd_date[0]) < 19:
            return 'aquarius'
        else:
            return 'pisces'
    if bd_date[1] == '3':
        if int(bd_date[0]) < 21:
            return 'pisces'
        else:
            return 'aries'
    if bd_date[1] == '4':
        if int(bd_date[0]) < 21:
            return 'aries'
        else:
            return 'taurus'
    if bd_date[1] == '5':
        if int(bd_date[0]) < 21:
            return 'taurus'
        else:
            return 'gemini'
    if bd_date[1] == '6':
        if int(bd_date[0]) < 22:
            return 'gemini'
        else:
            return 'cancer'
    if bd_date[1] == '7':
        if int(bd_date[0]) < 23:
            return 'cancer'
        else:
            return 'leo'
    if bd_date[1] == '8':
        if int(bd_date[0]) < 23:
            return 'leo'
        else:
            return 'virgo'
    if bd_date[1] == '9':
        if int(bd_date[0]) < 23:
            return 'virgo'
        else:
            return 'libra'
    if bd_date[1] == '10':
        if int(bd_date[0]) < 23:
            return 'libra'
        else:
            return 'scorpio'
    if bd_date[1] == '11':
        if int(bd_date[0]) < 22:
            return 'scorpio'
        else:
            return 'sagittarius'
    if bd_date[1] == '12':
        if int(bd_date[0]) < 22:
            return 'sagittarius'
        else:
            return 'capricorn'

keyboardgor = VkKeyboard(one_time=False)
keyboardgor.add_button('Овен', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Телец', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Близнецы', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Рак', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_line()  # Переход на вторую строку
keyboardgor.add_button('Лев', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Дева', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Весы', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Скорпион', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_line()  # Переход на вторую строку
keyboardgor.add_button('Стрелец', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Козерог', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Водолей', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_button('Рыбы', color=VkKeyboardColor.PRIMARY)
keyboardgor.add_line()  # Переход на вторую строку
keyboardgor.add_button('Убери гороскоп', color=VkKeyboardColor.NEGATIVE)

keyboardosn = VkKeyboard(one_time=False)
keyboardosn.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboardosn.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboardosn.add_button('Факт', color=VkKeyboardColor.PRIMARY)
keyboardosn.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
#keyboardosn.add_line()  # Переход на вторую строку
#keyboardosn.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)

'''
print(keyboardgor.get_keyboard())
vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    keyboard=keyboardgor.get_keyboard(),
    message="Я перезагружен!"
)
'''
def goroscop1():
    spisok_znakov=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
    for i in range (0,12):
        f = requests.get(
            "http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html")  # .text,"html.parser"
        f.encoding = 'utf-8'
        text_gor = (bs4.BeautifulSoup(f.text, "html.parser").find('div', 'col-12'))
        print(str(str(text_gor).split('\n')[2]).lstrip())
        filegor = open('/root/bot_herobot_chat/resurses/goroskop_files/' + spisok_znakov[i] + '.txt', 'w')  # /root/bot_herobot_chat
        filegor.write(str(str(text_gor).split('\n')[2]).lstrip())
        filegor.close()

def sentLS(text,user):
    vk.messages.send(
        user_id=user,
        random_id=get_random_id(),
        message=text
    )

iscl=["легкое", "сложное", "среднее", "❓ что это такое", "♻ другое слово", "!рестарт крокодил"]

def mainfunc():
    flaggoroscop=True
    attachments = []
    try:
        for event in longpoll.listen():

            attachments = []
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
                text_osn=event.obj.text
                # преобразование текста сообщения
                event.obj.text = event.obj.text.lower();
                evtxt = ''
                for i in range(0, len(event.obj.text)):
                    if not event.obj.text[i] in dict or (i == 0 and event.obj.text[i] == '!'):
                        evtxt += event.obj.text[i]
                if evtxt == '':
                    event.obj.text = event.obj.text
                else:
                    event.obj.text = evtxt


                # если сообщение получено от пользователя
                if event.from_user and event.obj.text not in iscl:
                    fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                        event.obj.peer_id) + "&fields=bdate&access_token="+token+"&v=5.92")
                    first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                    last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
                    #print(last_name, ' ', first_name, ' ', event.obj.peer_id, ' ', event.obj.text)
                    flaggorod1 = False


                    s=open('logs_ls.txt','a')
                    s.write(last_name + ' *_* ' + first_name + ' *_* ' + str(event.obj.from_id) + ' *_* ' + str(event.chat_id) + ' *_* ' + text_osn + '\n')
                    s.close()

                    f = open('resurses/goroda1.txt', 'r')
                    for i in f:
                        if str(event.obj.peer_id) == i[:-1:]:
                            flaggorod1 = True
                    f.close()

                    if event.obj.text == '!города' and flaggorod1 != True:

                        f = open('resurses/goroda1.txt', 'a')
                        f.write(str(event.obj.peer_id) + '\n')
                        f1 = open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'w')
                        f1.close()
                        f.close()

                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Давай сыграем, ' + first_name + ', думаю, правила ты знаешь, если захочешь закончить игру-напиши "!хватит играть"'+"."
                        )
                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Начинай, пиши первый город, я подхвачу'+"."
                        )
                    elif event.obj.text == 'начать':
                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Привет, меня зовут Херабот и я бот @id195310233(Никиты Михайлова) \n'
                                    'В ЛС мне доступны следующие функции:\n1) !города\n'
                                    '2) !гороскоп\n3) !кубик ..\n4) !факт\n5) !цитата\n6) !мысль\n7) !клавиатура вкл/выкл\n8) !анекдот\n9) Напомни мне\n'
                                    'Остальное время я буду просто болтать с тобой, '+first_name + ', но не обижайся, если невпопад, мой хозяин никак '
                                                                                                   'не доделает нейронку.\nА ещё я советую тебе включить клавиатуру, '
                                                                                                   'она упрощает взаимодействие со мной.'

                        )            
                    elif event.obj.text == '!обнови гороскоп' and event.obj.peer_id == 195310233:
                        goroscop1()
                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='обновил'+"."
                        )

                    elif event.obj.text == '!хелп' or event.obj.text == '!помощь' or event.obj.text == '!help':

                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Привет! В ЛС мне доступны следующие функции:\n1) !города\n'
                                    '2) !гороскоп\n3) !кубик ..\n4) !факт\n5) !цитата\n6) !мысль\n7) !клавиатура вкл/выкл\n8) !анекдот\n9) Напомни мне\n'
                                    'Остальное время я буду просто болтать с тобой, '+first_name + ', но не обижайся, если невпопад, мой хозяин никак '
                                                                                                   'не доделает нейронку.\nА ещё я советую тебе включить клавиатуру,'
                                                                                                   ' она упрощает взаимодействие со мной.'
                        )
                    elif event.obj.text == '!анекдот' or event.obj.text == 'анекдот':
                        anes = random.randint(0, 135500)
                        for linenum, line in enumerate(open('/root/bot_herobot_chat/resurses/anec.txt', 'r')):
                            if linenum == anes:
                                anecdot = (line.strip()).replace('#', '\n')
                        keyboardanec = VkKeyboard(one_time=False, inline=True)
                        keyboardanec.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardanec.get_keyboard(),
                            message=anecdot
                        )
                    elif event.obj.text == '!факт' or event.obj.text == 'факт':
                        cit = random.randint(0, 764)
                        for linenum, line in enumerate(open('/root/bot_herobot_chat/resurses/facts_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardfacts = VkKeyboard(one_time=False, inline=True)
                        keyboardfacts.add_button('Факт', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardfacts.get_keyboard(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == '!мысль' or event.obj.text == 'мысль':
                        cit = random.randint(0, 1355)
                        for linenum, line in enumerate(open('/root/bot_herobot_chat/resurses/quotes_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardquotes = VkKeyboard(one_time=False, inline=True)
                        keyboardquotes.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardquotes.get_keyboard(),
                            message=str(messagecit)

                        )

                    elif event.obj.text == '!цитата' or event.obj.text == 'цитата':
                        cit = random.randint(0, 1391)
                        for linenum, line in enumerate(open('/root/bot_herobot_chat/resurses/twtrr.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardtwtrr = VkKeyboard(one_time=False, inline=True)
                        keyboardtwtrr.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardtwtrr.get_keyboard(),
                            message=str(messagecit)
                        )

                    elif event.obj.text.find('!кубик') != -1:
                        kub = event.obj.text[7::]
                        try:
                            vk.messages.send(  # Отправляем собщение
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message='Выпало число ' + str(random.randint(1, int(kub)))+"."
                            )
                        except:
                            vk.messages.send(  # Отправляем собщение
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message='С твоим числом что-то не так'+"."
                            )

                    elif event.obj.text == '!гороскоп':
                        print(1223)
                        flaggoroscop=True
                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardgor.get_keyboard(),
                            message='Воспользуйся клавиатурой'+"."
                        )
                    
                    elif event.obj.text[:11:] == "напомни мне":
                        continue

                    elif event.obj.text in dict8 and flaggoroscop is True:
                        zodiak = dict8[event.obj.text]
                        f=open('/root/bot_herobot_chat/resurses/goroskop_files/'+zodiak+'.txt','r')
                        goroskp=f.read()
                        f.close()
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardgor.get_keyboard(),
                            message=goroskp
                        )

                    elif (event.obj.text == '!клавиатура вкл' or event.obj.text == 'клавиатура вкл'):
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardosn.get_keyboard(),
                            message="Окей, "+first_name+"."
                        )
                    elif (event.obj.text == '!клавиатура выкл' or event.obj.text == 'клавиатура выкл' or event.obj.text == 'выключить клавиатуру'):
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardosn.get_empty_keyboard(),
                            message="Окей, "+first_name+"."
                        )
                    elif (event.obj.text == '!убери гороскоп' or event.obj.text == 'убери гороскоп') and flaggoroscop is True:
                        flaggoroscop = False
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardosn.get_keyboard(),
                            message="Включена обычная клавиатура."
                        )
                        keyboardvkl = VkKeyboard(one_time=False, inline=True)
                        keyboardvkl.add_button('Выключить клавиатуру', color=VkKeyboardColor.NEGATIVE)
                        vk.messages.send(  # Отправляем собщение
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            keyboard=keyboardvkl.get_keyboard(),
                            message="Хочешь выключить её?"
                        )

                    elif event.obj.text == '!города' and flaggorod1 == True:

                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Так мы уже играем, ' + first_name+'.'
                        )

                    elif event.obj.text == '!хватит играть' and flaggorod1 == True:

                        try:
                            os.remove(str(event.obj.peer_id) + '.txt')
                        except:
                            print('еще нет файла 1')

                        f = open('resurses/goroda1.txt', 'r')
                        r = ''
                        for line in f:
                            if line[:-1:] == str(event.obj.peer_id):
                                r = r
                            else:
                                r += line + '\n'
                        f.close()
                        r1 = r.split('\n')
                        r2 = []
                        # print(r1)
                        for i in r1:
                            if i != '':
                                r2.append(i)
                        # print(r2)
                        r = '\n'.join(r2) + '\n'
                        # print(r)
                        os.remove('resurses/goroda1.txt')
                        f = open('resurses/goroda1.txt', 'w')
                        f.write(r)
                        f.close()

                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Как скажешь, ' + first_name+'.'
                        )
                        vk.messages.send(
                            user_id=event.obj.peer_id,
                            random_id=get_random_id(),
                            message='Если захочешь ещё поиграть-просто напиши мне "!города"'+'.'
                        )


                    elif flaggorod1 is True:
                        flaggorod2 = False
                        flaggorod3 = False
                        flaggorod5 = False
                        f1 = open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'r')
                        chet = 0
                        for i in f1:
                            chet += 1
                            if str(event.obj.text) == i[:-1:]:
                                flaggorod3 = True
                        f1.close()

                        if chet != 0:
                            for linenum, line in enumerate(open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'r')):
                                if linenum == chet - 1:
                                    poslgorod = (line.strip())
                            if poslgorod[-1] == 'ь' or poslgorod[-1] == 'ы' or poslgorod[-1] == 'ъ' or poslgorod[
                                -1] == 'a':
                                if event.obj.text[0].lower() == poslgorod[-2]:
                                    # print('изменена буква')
                                    flaggorod5 = True
                            if event.obj.text[0].lower() == poslgorod[-1]:
                                flaggorod5 = True

                        else:
                            flaggorod5 = True

                        f = open('resurses/cities.txt', 'r')
                        for i in f:
                            if event.obj.text == i[:-1:].lower():
                                flaggorod2 = True
                        f.close()
                        f = open('resurses/cityman.txt', 'r')
                        for i in f:
                            if event.obj.text == i[:-1:].lower():
                                flaggorod2 = True
                        f.close()
                        if flaggorod2 is True and flaggorod3 is not True and flaggorod5 is True:
                            f1 = open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'a')
                            f1.write(str(event.obj.text + '\n'))
                            f1.close()
                            letter = str(event.obj.text[-1])
                            if letter == 'ь' or letter == 'ы' or letter == 'ъ':
                                letter = str(event.obj.text[-2])
                            flgorod = False
                            try:
                                while flgorod is False:
                                    # flaggorod31=False
                                    randgorod = random.randint(0, 10960)
                                    for linenum, line in enumerate(open('resurses/cityman.txt', 'r')):
                                        if linenum == randgorod:
                                            gorod = (line.strip())
                                    f1 = open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'r')
                                    if gorod[-1] == '\n':
                                        gorod = gorod[:-1:]

                                    for i in f1:
                                        if gorod[0].lower() == letter:
                                            if gorod.lower() == i[:-1:]:
                                                flaggorod4 = True
                                            else:
                                                flgorod = True

                                f1.close()
                                f1 = open('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt', 'a')
                                f1.write(gorod.lower() + '\n')
                                f1.close()
                                ranom = random.randint(0, 4)
                                if ranom == 0 or ranom == 4:
                                    print('попал в описание')
                                    try:
                                        dlina = len(gorod)
                                        if gorod[-1] == 'ь' or gorod[-1] == 'ы' or gorod[-1] == 'ъ':
                                            posllet = gorod[-2].upper()
                                        else:
                                            posllet = gorod[-1].upper()
                                        for linenum, line in enumerate(open('resurses/city2.txt', 'r')):
                                            if line[:dlina:] == gorod:
                                                link = line.split('|')
                                            
                                                if link[1].find('(') != -1 and link[1].find(')') != -1:
                                                    e1 = link[1].find('(')
                                                    e2 = link[1].find(')')
                                                    text1 = link[1][:e1:] + link[1][e2 + 1::]
                                                    text = text1.split('.')
                                                else:
                                                    text = link[1].split('.')
                                                # print(text)
                                                ranom2 = random.randint(1, len(text) - 1)
                                                if ranom2 > 3:
                                                    ranom2 = 3
                                                gorod += '\nКстати, во что я знаю про этот город\n'+'.'
                                                for r1 in range(0, ranom2):
                                                    gorod += text[r1] + '\n'
                                                sluchay = random.randint(0, 4)
                                                print("сформировал описание")
                                                if sluchay == 0:
                                                    variants = ['Неплохой вариант, ' + first_name + '!', 'Окей, пойдёт.',
                                                                'Хороший город, ты молодец, ' + first_name + '!',
                                                                'Здорово, но я всё равно умнее тебя.']
                                                    vk.messages.send(
                                                        user_id=event.obj.peer_id,
                                                        random_id=get_random_id(),
                                                        message=variants[random.randint(0, 3)]
                                                    )
                                                vk.messages.send(
                                                    user_id=event.obj.peer_id,
                                                    random_id=get_random_id(),
                                                    message=gorod
                                                )
                                                vk.messages.send(
                                                    user_id=event.obj.peer_id,
                                                    random_id=get_random_id(),
                                                    message='Тебе на букву ' + posllet+'.'
                                                )
                                                print("отправил описание")
                                    except:
                                        print("с описанием проблемы, отправил просто город")
                                        vk.messages.send(
                                            user_id=event.obj.peer_id,
                                            random_id=get_random_id(),
                                            message=gorod
                                        )
                                if ranom == 1 or ranom == 3:
                                    print("попал в картинку")
                                    try:
                                        if gorod[-1] == 'ь' or gorod[-1] == 'ы' or gorod[-1] == 'ъ':
                                            posllet = gorod[-2].upper()
                                        else:
                                            posllet = gorod[-1].upper()
                                        '''
                                        response = requests.get(
                                            'https://ru.depositphotos.com/search/город&' + gorod.lower() + '&фото.html')
                                        parsed_body = html.fromstring(response.text)
                                        # Парсим ссылки с картинками
                                        images = parsed_body.xpath('//img/@src')
                                        images = [urllib.parse.urljoin(response.url, url) for url in images]
                                        image_url = images[random.randint(0, len(images))]
                                        '''

                                        response = google_images_download.googleimagesdownload()
                                        arguments = {"keywords": 'город '+event.obj.text.lower(), "size": 'medium', "limit": random.randint(1, 10), "no_download": True,
                                                     "print_urls": True}
                                        paths = response.download(arguments)
                                        file_url=open('file_url.txt','r')
                                        #print('файл успешно открыт')
                                        gh=0
                                        for line in file_url:
                                            #print(line)
                                            if gh==0:
                                                image_url=line
                                            gh+=1
                                        #print(image_url)
                                        file_url.close()
                                        image_url = image_url
                                        image = session.get(image_url, stream=True)
                                        photo = upload.photo_messages(photos=image.raw)[0]
                                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                                           )
                                        print("загрузил картинку")

                                        vk.messages.send(
                                            user_id=event.obj.peer_id,
                                            random_id=get_random_id(),
                                            attachment=','.join(attachments),
                                            message=gorod + '\nВот, кстати, фото города '+event.obj.text.capitalize()+', который ты предложил.'
                                        )
                                        vk.messages.send(
                                            user_id=event.obj.peer_id,
                                            random_id=get_random_id(),
                                            message='Тебе на букву ' + posllet+'.'
                                        )
                                        print("отправил картинку")
                                    except:
                                        print("с картинкой проблемы, отправил чистый город")
                                        vk.messages.send(
                                            user_id=event.obj.peer_id,
                                            random_id=get_random_id(),
                                            message=gorod
                                        )

                                if ranom == 2:
                                    print("попал просто в город")
                                    vk.messages.send(
                                        user_id=event.obj.peer_id,
                                        random_id=get_random_id(),
                                        message=gorod
                                    )
                            except:
                                vk.messages.send(
                                    user_id=event.obj.peer_id,
                                    random_id=get_random_id(),
                                    message='ты меня победил, я больше не знаю городов.'
                                )

                                f = open('resurses/goroda1.txt', 'r')
                                r = ''
                                for line in f:
                                    if line[:-1:] == str(event.obj.peer_id):
                                        r = r
                                    else:
                                        r += line + '\n'
                                f.close()
                                f = open('resurses/goroda1.txt', 'w')
                                f.write(r)
                                f.close()
                                os.remove('resurses/goroda_files/'+str(event.obj.peer_id) + '.txt')


                        elif flaggorod2 is True and flaggorod3 is True:
                            print("попал в повторение")
                            spisok1 = ['Либо я тебя неправильно понял, либо такой город уже был.',
                                       'В нашей игре уже был такой город.', 'Ты повторяешься, ' + first_name+'.']
                            ran = random.randint(0, 2)
                            vk.messages.send(
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message=spisok1[ran]
                            )
                        elif flaggorod2 is True and flaggorod5 is False:
                            print("попал в неправильную букву")
                            vk.messages.send(
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message='У твоего города неправильная первая буква.'
                            )
                        else:
                            print("попал в отсутствие")
                            spisok2 = ["Я не нашел такого города в своей базе.", "Извини, но такого города нет.",
                                       "Может ты и прав, но я такого города не знаю."]
                            ran = random.randint(0, 2)
                            vk.messages.send(
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message=spisok2[ran]
                            )

                    else:
                        anssplit=open('resurses/baza3.txt','r')
                        for line in anssplit:
                            #print(event.obj.text,line.split('\\')[0])
                            if line.split('\\')[0]==event.obj.text:
                                response=line.split('\\')[1]
                                break
                            else:
                                response=None
                        anssplit.close()
                        anssplit=open('resurses/baza3.txt','r')
                        if response==None:
                            #print(11)
                            for line in anssplit:
                                for red in range (0,len(event.obj.text.split(' '))-1):
                                    if line.split('\\')[0].find(event.obj.text.split(' ')[red])!=-1:
                                        #print(event.obj.text.split(' ')[red],line.split('\\')[0])
                                        response=line.split('\\')[1]
                                        break
                                    else:
                                        response=None

                                if response!=None:
                                    break
                        anssplit.close()
                        if response:
                            vk.messages.send(
                                user_id=event.obj.peer_id,
                                random_id=get_random_id(),
                                message=response
                            )
                        else:
                            xy=['ху','хуи','хуя']
                            t=random.randint(0,2)
                            t2=random.randint(3,4)
                            if len(event.obj.text.split(' '))==1 and random.randint(0,2)==2:
                                vk.messages.send(
                                    user_id=event.obj.peer_id,
                                    random_id=get_random_id(),
                                    message=xy[t]+event.obj.text[-(t2)::]
                                )
                            else:
                                vk.messages.send(
                                    user_id=event.obj.peer_id,
                                    random_id=get_random_id(),
                                    message='Я тупой как тапок, ' + first_name+'.'
                                )

    except Exception as err:
        vk.messages.send(
            user_id=195310233,
            random_id=get_random_id(),
            message='Возникла ошибка ' + str(err) + ' в главном цикле bot_herobot_ls.'
        )
        mainfunc()
mainfunc()
