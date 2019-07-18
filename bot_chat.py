from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time, datetime, bs4, random, requests, vk_api


dict = [".", ",", "!", "?", ")", "(", ":", ";", "'", ']', '[', '"']
dictan = [")", "(", ":", ";", "'", ']', '[', '"', '\\', 'n', '&', 'q', 'u', 'o', 't']
dict2 = ["пидр", "сука", "лох", "пидрила", "мудак", "дурак", "тупой", "тормоз", "дебил", "дибил","дурачок"]
dict4 = ["кушать", "пить", "есть", "поесть", "жрать"]
dict5 = ["вик", "ксюх", "ксюш", "ксень", "саш", "сань", "петь", "петя", "петро", "кать",
         "катя", "катюх", "андрей", "андрюх", "оля", "оль", "ник"]
dictandr = ['https://zabavnik.club/wp-content/uploads/mister_Bin_36_20133200.jpg',
            'http://risovach.ru/upload/2013/10/mem/chernyj-vlastelin_32124026_orig_.jpg',
            'http://risovach.ru/thumb/upload/200s400/2015/09/mem/lol_91705151_orig_.jpg?6eduj',
            'http://risovach.ru/upload/2013/06/mem/moe-lico_21925181_orig_.jpeg',
            'http://risovach.ru/upload/2013/12/mem/nelzya-prosto-tak-vzyat-i-boromir-mem_37752087_orig_.jpg',
            'http://risovach.ru/upload/2014/11/mem/tvoe-vyrazhenie-lica_67424388_orig_.jpg',
            'http://risovach.ru/upload/2014/12/mem/voenkom-polkovnik_68047393_orig_.jpg',
            'http://risovach.ru/upload/2014/05/mem/petrosyanych_51799328_orig_.jpg',
            'http://risovach.ru/thumb/upload/200s400/2013/03/mem/sudya-egorova_12558528_orig_.jpg?7cr1v',
            'http://risovach.ru/upload/2014/01/mem/mudriy-paca_40062800_orig_.jpeg',
            'http://risovach.ru/thumb/upload/200s400/2017/01/mem/tipichnyy-dolboslav_135762775_orig_.jpg?4cjzt',
            'https://imgp.golos.io/0x0/https://bm-platform.s3.eu-central-1.amazonaws.com/rJY9bkjhl-%D0%B3%D1%80%D1%83%D1%81%D1%82%D1%8C.jpg',
            'http://risovach.ru/upload/2013/05/mem/a-chto-esli_19665349_orig_.jpg',
            'http://abload.de/img/14131859331710h4puk.jpg',
            'https://ic.pics.livejournal.com/vvfidel/76941342/126686/126686_900.jpg']
dict7 = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
dict8 = {'овен':'aries','телец':'taurus' ,'близнецы':'gemini' ,'рак':'cancer' ,'лев':'leo' ,'дева':'virgo' ,'весы':'libra' ,'скорпион':'scorpio' ,'стрелец':'sagittarius','козерог':'capricorn' ,'водолей':'aquarius' ,'рыбы':'pisces'}
kolresp = 0
attachments = []
chand = 0
flagtime = False
fltm1 = False
fltm2 = False
flaggoroscop=False


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('Шутка', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Факт', color=VkKeyboardColor.PRIMARY)
#keyboard.add_line()
#keyboard.add_button('Отстань', color=VkKeyboardColor.NEGATIVE)
#keyboard.add_button('Вернись', color=VkKeyboardColor.POSITIVE)
'''
for i in range(2,10):
    vk.messages.send(
        chat_id=i,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message="Обновление подъехало, открой клавиатуру"
    )
'''
def goroscop1():
    spisok_znakov=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
    for i in range (0,12):
        filegor=open('/home/NikMik/bot/goroskop/'+spisok_znakov[i]+'.txt','w')
        filegor.write(((bs4.BeautifulSoup(requests.get("http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html").text,"html.parser").find('div', 'col-12')).getText().lstrip()))
        filegor.close()

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


def wheather(city):
    for i in range(len(city)):
        if city[i] == ' ':
            city = city[:i:] + '-' + city[i + 1::]
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")
    try:
        p3 = b.select('.temperature .p2')
        p3_1 = str(b.select('.p2')[6])[str(b.select('.p2')[6]).find("data-tooltip=")+14:str(b.select('.p2')[6]).rfind(' ">'):]
        weather1 = p3[0].getText()
        wind1=p3_1
        if len(wind1)<4:
            wind1="Ветра нет"
        #print(weather1,wind1)
        p4 = b.select('.temperature .p4')
        p4_1 = str(b.select('.p4')[6])[str(b.select('.p4')[6]).find("data-tooltip=")+14:str(b.select('.p4')[6]).rfind(' ">'):]
        weather2 = p4[0].getText()
        wind2=p4_1
        if len(wind2)<4:
            wind2="Ветра нет"
        #print(weather2,wind2)
        p5 = b.select('.temperature .p6')
        p5_1 = str(b.select('.p6')[6])[str(b.select('.p6')[6]).find("data-tooltip=")+14:str(b.select('.p6')[6]).rfind(' ">'):]
        weather3 = p5[0].getText()
        wind3=p5_1
        if len(wind3)<4:
            wind3="Ветра нет"
        #print(weather3,wind3)
        p6 = b.select('.temperature .p8')
        p6_1 = str(b.select('.p8')[6])[str(b.select('.p8')[6]).find("data-tooltip=")+14:str(b.select('.p8')[6]).rfind(' ">'):]
        weather4 = p6[0].getText()
        wind4=p6_1
        if len(wind4)<4:
            wind4="Ветра нет"
        #print(weather4,wind4)
        result = ''
        result = result + ('Ночью : ' + weather1+', Ветер: '+wind1) + '\n'
        result = result + ('Утром : ' + weather2+', Ветер: '+wind2) + '\n'
        result = result + ('Днём : ' + weather3+', Ветер: '+wind3) + '\n'
        result = result + ('Вечером : ' + weather4+', Ветер: '+wind4) + 2*'\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()
        return result
    except IndexError:
        result = 'Такого города не найдено'
        return result


def mainfunc():
    attachments = []
    chand = 0
    flagtime = False
    fltm1 = False
    fltm2 = False
    #day_time=time.strftime("%d", time.localtime())
    try:
        for event in longpoll.listen():
            kolresp=0
            attachments = []
            flkv = False
            flkv2 = False
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:

                # преобразование текста сообщения
                kupi_slona=event.obj.text
                event.obj.text = event.obj.text.lower();
                evtxt = ''
                for i in range(0, len(event.obj.text)):
                    if not event.obj.text[i] in dict:
                        evtxt += event.obj.text[i]
                if evtxt == '':
                    event.obj.text = event.obj.text
                else:
                    event.obj.text = evtxt
                if event.obj.text[:24:] == 'club178949259|ботхеработ':
                    event.obj.text = event.obj.text[25::]
                    flkv = True

                if event.obj.text[:28:] == 'club178949259|@club178949259':
                    event.obj.text = event.obj.text[29::]
                    flkv2 = True




                if event.from_chat and event.obj.from_id!=-183679552:
                    fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                        event.obj.from_id) + "&fields=bdate, city&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                    first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                    last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
                    #print(fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower())
                    #print(fio.text)
                    try:
                        proverochka=fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()
                        flagbddate=True
                        bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-1:]
                        #print(bd_date)
                    except:
                        try:
                            flagbddate=True
                            bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-4:]
                            #print(bd_date)
                        except:
                            flagbddate=False
                            bd_date=None
                    '''
                    print(time.strftime("%d", time.localtime()),day_time)

                    if day_time is None:
                        day_time=time.strftime("%d", time.localtime())

                    if time.strftime("%d", time.localtime())!=day_time:
                        date_file=open('anton.txt','r')
                        k = 0
                        for line in date_file:
                            if k == 0:
                                date_anton = int(line[0]) - 1
                            k += 1
                        date_file.close()
                        date_file=open('anton.txt','w')
                        date_file.write(date_anton)
                        date_file.close()
                        day_time=time.strftime("%d", time.localtime())
                    '''
                    s=open('history_chat.txt','a')
                    s.write(last_name + ' *_* ' + first_name + ' *_* ' + str(event.obj.from_id) + ' *_* ' + str(event.chat_id) + ' *_* ' + kupi_slona + '\n')
                    s.close()

                    if time.strftime("%d", time.localtime())[0] == '0':
                        den = time.strftime("%d", time.localtime())[1::]
                    else:
                        den = time.strftime("%d", time.localtime())
                    # print(den,bd_date.split('.')[0])

                    pozdrflag = False
                    pozdr = open('pozdravlenie.txt', 'r')
                    for i in pozdr:
                        if str(event.obj.from_id) == i[:-1:]:
                            pozdrflag = True
                    pozdr.close()
                    if flagbddate==True and str(dict7[time.strftime("%B", time.localtime())]) == bd_date.split('.')[1] and den == \
                            bd_date.split('.')[0] and pozdrflag is False:
                        pozdr = open('pozdravlenie.txt', 'a')
                        pozdr.write(str(event.obj.from_id) + '\n')
                        pozdr.close()
                        image_url = 'https://pp.userapi.com/c850128/v850128497/10e229/uPpRrYrMR-4.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message="О, " + first_name + ", Поздравляю тебя с Днём Рождения! Моё железное сердце всегда радуется твоим сообщениям!"
                        )

                    flagobr = 0
                    for i in range(len(dict5)):
                        if event.obj.text.find(dict5[i]) != -1:
                            flagobr = 1

                    flag3 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        for k in dict4:
                            if k == str(event1[i]):
                                if event.obj.text.find('хочешь')!=-1 or event.obj.text.find('будем')!=-1 or event.obj.text.find('будешь')!=-1 or event.obj.text.find('пошли')!=-1 or event.obj.text.find('где')!=-1 or event.obj.text.find('го')!=-1 or event.obj.text.find('погнали')!=-1 or event.obj.text.find('куда')!=-1 or event.obj.text.find('гоу')!=-1 and k=='есть':
                                    flag3 = 1
                                    flag2 = k
                                else:
                                    if k!='есть':
                                        flag3 = 1
                                        flag2 = k

                    flag1 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        mat = open('/home/NikMik/bot/matsp1.txt', 'r')
                        for k in mat:
                            if str(event1[i]) == k[:-1:]:
                                flag1 = 1
                        mat.close()

                    flag10 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        if str(event1[i]) == 'лень' or str(event1[i]) == 'лениво' or str(event1[i]) == 'учиться' or str(
                                event1[i]) == 'ботать':
                            flag10 = 1

                    flag = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(dict2)):
                        for k in range(0, len(event1)):
                            if event1[k] == dict2[i]:
                                flag = 1
                                flag2 = i

                    if event.obj.from_id == 13069991:
                        f = open('andr.txt', 'r')
                        k = 0
                        for line in f:
                            if k == 0:
                                chand = int(line[0]) + 1
                            k += 1
                        f.close()
                        if chand == 16:
                            chand = 0
                        f = open('andr.txt', 'w')
                        f.write(str(chand))
                        f.close()
                    if event.obj.from_id == 13069991 and chand == 15 and flagtime != True:
                        a = random.randint(0, 9)
                        image_url = dictandr[a]
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                           )
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message='У меня есть для тебя картинка, ' + first_name
                        )



                    if flag1 == 1 and event.obj.text.find('бот отъебись') == -1:
                        f1 = open('mat.txt', 'a')
                        f1.write(str(event.obj.from_id))
                        f1.write('\n')
                        f1.close()
                        f1 = open('mat.txt', 'r')
                        chmat = 0
                        for line in f1:
                            if line == str(event.obj.from_id) + '\n':
                                chmat += 1
                        try:
                            vk.messages.send(
                                user_id=event.obj.from_id,
                                random_id=get_random_id(),
                                message='Это твоё ' + str(chmat) + ' грязное словечко в чате, я всё вижу, ' + first_name
                            )
                            f1.close()
                        except vk_api.exceptions.VkApiError:
                            vk.messages.send(
                                user_id=195310233,
                                random_id=get_random_id(),
                                message='Возникла ошибка в доступе к личным сообщениям, id пользователя ' + str(
                                    event.obj.from_id) + ' имя пользователя ' + first_name + ' ' + last_name
                            )
                            f1.close()

                    elif event.obj.text == 'бот что ты умеешь':
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Привет! В Беседах мне доступны следующие функции:\n1) Бот, погода\n2) Бот, погода в городе ...\n3) Бот, погода на завтра в городе ...\n4) Бот, погода на завтра\n5) Бот, анекдот\n6) Бот, цитату\n7)Бот, кинь кубик ...\n8)Бот, гороскоп\n9)Купи слона\n10) Бот, мысль\n11) Бот, шутка\n12) Бот, факт\nОстальное время я буду просто болтать с вами и реагировать на некоторые контекстные фразы'
                        )

                    elif event.obj.text == 'бот отъебись' and event.chat_id==1:
                        fltm1 = False
                        stoptime2 = time.time()
                        flagtime = True
                        fltm2 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На один час)'
                        )

                    elif event.obj.text == 'бот отстань'  and event.chat_id==1 or event.obj.text == 'отстань' and flkv == True or event.obj.text == 'отстань' and flkv2 == True:
                        fltm2 = False
                        stoptime1 = time.time()
                        flagtime = True
                        fltm1 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На 10 минут)'
                        )

                    elif event.obj.text == 'бот вернись'  and event.chat_id==1 or event.obj.text == 'вернись' and flkv == True or event.obj.text == 'вернись' and flkv2 == True:
                        flagtime = False
                        fltm1 = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )

                    if fltm1 is True and flagtime is True and time.time() - stoptime1 >= 600:

                        flagtime = False
                        fltm1 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )

                    if fltm2 is True and flagtime is True and time.time() - stoptime2 >= 3600:

                        flagtime = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )




                    elif flag == 1 and flagobr == 0 and flagtime != True:
                        vk.messages.send(  # Отправляем сообщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Сам такой, ' + dict2[flag2] + ', ' + last_name
                        )


                    elif event.obj.text == 'бот антон':
                        aa = datetime.date.today()
                        bb = datetime.date(2020,7,4)
                        cc=bb-aa
                        dateAnton=(str(cc).split(',')[0].split(' ')[0])
                        if dateAnton[-1]=='1' or dateAnton[-1]=='0':
                            date_day='день.'
                        if dateAnton[-1]=='2' or dateAnton[-1]=='3' or dateAnton[-1]=='4':
                            date_day='дня.'
                        if dateAnton[-1]=='5' or dateAnton[-1]=='6' or dateAnton[-1]=='7' or dateAnton[-1]=='8' or dateAnton[-1]=='9':
                            date_day='дней.'
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Антон вернётся к нам через '+str(dateAnton)+' '+date_day
                        )

                    elif event.obj.text == 'бот шутку' or event.obj.text == 'шутка' and flkv == True or event.obj.text == 'шутка' and flkv2 == True:
                        cit = random.randint(0, 5329)
                        for linenum, line in enumerate(open('jokes_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == 'бот мысль' or event.obj.text == 'мысль' and flkv == True or event.obj.text == 'мысль' and flkv2 == True:
                        cit = random.randint(0, 1355)
                        for linenum, line in enumerate(open('quotes_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == 'бот факт' or event.obj.text == 'факт' and flkv == True or event.obj.text == 'факт' and flkv2 == True:
                        cit = random.randint(0, 764)
                        for linenum, line in enumerate(open('facts_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == 'бот цитату' or event.obj.text == 'цитата' and flkv == True or event.obj.text == 'цитата' and flkv2 == True:
                        cit = random.randint(0, 1391)
                        for linenum, line in enumerate(open('twtrr.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == 'бот гороскоп' or event.obj.text == 'гороскоп' and flkv == True or event.obj.text == 'гороскоп' and flkv2 == True:
                        if flagbddate==True:
                            bd_date = bd_date.split('.')
                            zodiak = goroscop(bd_date)
                            f=open('/home/NikMik/bot/goroskop/'+zodiak+'.txt','r')
                            goroskp=f.read()
                            f.close()
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=goroskp
                            )
                        else:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='У тебя нет даты Рождения ВК'
                            )

                    elif event.obj.text == 'бот анекдот' or event.obj.text == 'анекдот' and flkv == True or event.obj.text == 'анекдот' and flkv2 == True:
                        anes = random.randint(0, 130200)
                        for linenum, line in enumerate(open('anec.txt', 'r')):
                            if linenum == anes:
                                anecdot = (line.strip()).replace('#', '\n')
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=anecdot
                        )

                    elif flag3 == 1 and flagobr == 0 and flagtime != True:
                        image_url = 'https://pp.userapi.com/c851020/v851020736/cb17f/BgYwz2bShuc.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                           )
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message='Кто сказал ' + flag2 + '?'
                        )

                    elif event.obj.text.find('бот погода на завтра в городе') != -1:
                        # print(datetime.date.today()+datetime.timedelta(days=1))
                        city = event.obj.text[30::] + "/" + str(datetime.date.today() + datetime.timedelta(days=1))
                        result = wheather(city)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('бот погода в городе') != -1 and event.obj.text.find('на завтра') != -1:
                        # print(datetime.date.today()+datetime.timedelta(days=1))
                        city = event.obj.text[20:-10:] + "/" + str(datetime.date.today() + datetime.timedelta(days=1))
                        # print(city)
                        result = wheather(city)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('бот погода на завтра') != -1:
                        # print(datetime.date.today()+datetime.timedelta(days=1))
                        try:
                            city = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower() + "/" + str(datetime.date.today() + datetime.timedelta(days=1))
                        except:
                            city = "москва" + "/" + str(datetime.date.today() + datetime.timedelta(days=1))
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                            )
                        result = wheather(city)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('бот погода в городе') != -1:
                        city = event.obj.text[20::]
                        result = wheather(city)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('бот погода') != -1 or event.obj.text.find(
                            'погода') != -1 and flkv == True or event.obj.text.find('погода') != -1 and flkv2 == True:
                        try:
                            city = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()
                        except:
                            city = 'москва'
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                            )
                        result = wheather(city)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('купи слона') != -1:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Все говорят ' + kupi_slona + ', а ты купи слона'
                        )

                    elif event.obj.text.find('бот кинь кубик') != -1:
                        kub = event.obj.text[15::]
                        try:
                            vypalo = random.randint(1, int(kub))
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='Выпало число ' + str(vypalo)
                            )
                        except:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='С твоим числом что-то не так'
                            )

                    elif event.obj.text == 'ну и ладно' and flagtime != True:
                        image_url = 'https://pp.userapi.com/c851120/v851120719/d26d3/-orcQNPA2gI.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                           )
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message=''
                        )

                    elif event.obj.text.split(' ')[-1] == "нет" and flagtime != True:  # Если написали в Беседе
                        # print("чат", event.obj.text, event.chat_id)
                        k = ["Пидора ответ!", "Программиста ответ!", "Петика ответ!"]
                        a = random.randint(0, 2)
                        if random.randint(0, 1) == 1 and event.obj.from_id == 51556033:
                            a = 2
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=k[a]
                        )

                    elif flagtime != True and event.obj.text[-3::] == "300" or flagtime != True and event.obj.text[
                                                                                                    -6::] == "триста":  # Если написали в Беседе
                        # print("чат", event.obj.text, event.chat_id)
                        k = ["Отсоси у программиста!", "Отсоси у тракториста!", "Отвези домой таксиста!",
                             "Сам тащи рюкзак туриста", "Лизни подмышку пианиста"]
                        a = random.randint(0, 4)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=k[a]
                        )

                    elif event.obj.text.split(' ')[-1] == "бот" and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Херабот!'
                        )

                    elif flag10 == 1 and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Пиздуй учиться, ' + first_name + '!'
                        )

                    elif flagtime != True and event.obj.text.split(' ')[-1] == "чо" or flagtime != True and \
                            event.obj.text.split(' ')[-1] == "че" or flagtime != True and event.obj.text.split(' ')[
                        -1] == "чё":
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Йух через плечо!'
                        )

                    elif event.obj.text.split(' ')[-1] == "да" and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Сковорода!'
                        )



                    '''
                    else:

                        request = apiai.ApiAI('5223c3ee5b95429c8794b01faef6d4e5').text_request()
                        request.lang = 'ru'  # На каком языке будет послан запрос
                        request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
                        request.query = event.obj.text  # Посылаем запрос к ИИ с сообщением от юзера
                        # print(request.getresponse().read().decode('utf-8'))
                        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
                        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ

                        anssplit=open('baza3.txt','r')
                        for line in anssplit:
                            #print(event.obj.text,line.split('\\')[0])
                            if line.split('\\')[0]==event.obj.text:
                                response=line.split('\\')[1]
                                break
                            else:
                                response=None
                        anssplit.close()
                        anssplit=open('baza3.txt','r')
                        if response==None:
                            #print(11)
                            for line in anssplit:
                                for red in range (0,len(event.obj.text.split(' '))-1):
                                    if line.split('\\')[0].find(event.obj.text.split(' ')[red])!=-1:
                                        for green in range (0,len(event.obj.text.split(' '))-1):
                                            if line.split('\\')[0].find(event.obj.text.split(' ')[green])!=-1 and red!=green:
                                        #print(event.obj.text.split(' ')[red],line.split('\\')[0])
                                                response=line.split('\\')[1]
                                                break
                                            else:
                                                response=None

                                if response!=None:
                                    break
                        if response==None and random.randint(0,2)==2 and event.obj.text.isalpha() and len(event.obj.text)>6 and len(event.obj.text.split(' '))==1 and flagobr == 0 and flagtime != True:
                            xy=['ху','хуи','хуя','хуе']
                            t=random.randint(0,3)
                            t2=random.randint(3,4)
                            if len(event.obj.text.split(' '))==1 and kolresp >= random.randint(0, 5) and flagobr == 0 and flagtime != True:
                                vk.messages.send(
                                    chat_id=event.chat_id,
                                    random_id=get_random_id(),
                                    message=xy[t]+event.obj.text[-(t2)::]
                                )
                        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
                        if response and kolresp >= random.randint(0, 10) and flagobr == 0 and flagtime != True:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=response
                            )
                            kolresp = 0
                    kolresp += 1
                    '''
    except Exception as err:
        try:
            print(err,type(err))
            if str(err.find("Errno 2"))!=-1:
                vk.messages.send(
                    user_id=195310233,
                    random_id=get_random_id(),
                    message='Возникла ошибка ' + str(err) + ' в главном цикле программы сообщений бесед, цикл перезапущен\nНа сообщении пользователя: '+first_name+' '+last_name+'\nC текстом сообщения: '+event.obj.text
                )
            goroscop1()
            mainfunc()
        except:
            print(err)

            vk.messages.send(
                user_id=195310233,
                random_id=get_random_id(),
                message='Возникла ошибка ' + str(err) + ' в главном цикле программы сообщений бесед, цикл перезапущен\nОшибка без участия пользователя.'
            )
            goroscop1()
            mainfunc()


mainfunc()


'''
                    elif event.obj.text == 'бот время':
                        hour = (time.strftime('%H', time.localtime()))
                        hour = int(hour)
                        tm1 = (time.strftime("Сегодня %B %d, %Y;", time.localtime()))
                        tm2 = (time.strftime(":%M", time.localtime()))
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=tm1 + ' ' + str(hour + 3) + tm2
                        )
'''