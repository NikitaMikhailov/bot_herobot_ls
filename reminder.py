#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime, requests, vk_api, calendar
from vk_api.utils import get_random_id

# сделать проверку при переходе на завтра в последний день месяца !!done
# сделать проверку на правильную дату !!done
# исправить регистр в  напоминании  !!done
# добавить возможность указывать время с точкой и без минут
# добавить напоминания на год вперед !!done и на какой-то конкретный год
# добавить написание месяца словом

f=open('token.txt','r')
token=f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений


# file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "w", encoding="utf8")
# file_zametki.close()
 
format_command = "Формат команды:\n'напомни мне\n+\nутром/днем/вечером\nв hh:mm\nзавтра в hh:mm\nзавтра утром/днем/вечером\nday.month\nday.month в hh:mm\n+\nтекст напоминания.'\nПросмотреть список напоминаний: 'напомни мне все'"
uncorrect_comand = "Команда напоминания некорректна"

def sent_message(text, user_id):
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=text
    )

def refactor_time_start(time_start):
    tm_st = time_start.split(':')
    if len(tm_st) < 2:
        return time_start.split('.')
    else:
        return tm_st

def correct_date(date_start):
    if int(date_start.split('.')[1]) < 1 or int(date_start.split('.')[1]) > 12 or int(
            date_start.split('.')[0]) < 1 or int(date_start.split('.')[0]) > \
            calendar.monthrange(datetime.datetime.now().year, int(date_start.split('.')[1]))[1]:
        text = 'Дата задана некорректно'
        sent_message(text, event.obj.peer_id)
        return False
    if int(date_start.split('.')[1]) <= datetime.datetime.now().month and int(
            date_start.split('.')[0]) < datetime.datetime.now().day or int(
        date_start.split('.')[1]) < datetime.datetime.now().month:
        text = 'Указанная дата меньше текущей, напоминание сработает только на следующий год'
        sent_message(text, event.obj.peer_id)
        return True
    return True


def correct_time(time_start, today_flag):

    time_start = refactor_time_start(time_start)
    if len(time_start)>2:
        text = 'Время задано некорректно'
        sent_message(text, event.obj.peer_id)
        return False
    if int(time_start[0]) < 0 or int(time_start[0]) > 23 or int(
            time_start[1]) < 0 or int(time_start[1]) > 59:
        text = 'Время задано некорректно'
        sent_message(text, event.obj.peer_id)
        return False
    if today_flag is True and datetime.time(int(time_start[0]),
                                            int(time_start[1])) <= datetime.time(
        datetime.datetime.now().hour, datetime.datetime.now().minute):
        text = 'Указанное время меньше текущего'
        sent_message(text, event.obj.peer_id)
        return False

    return True


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_user:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()
        if event.obj.text[:11:] == "напомни мне":
            try:
                if event.obj.text == "напомни мне":
                    text = "Я могу помочь тебе не забывать важную информацию"
                    sent_message(text, event.obj.peer_id)
                    sent_message(format_command, event.obj.peer_id)
                    
                elif event.obj.text == "напомни мне все" or event.obj.text == 'напомни мне всё':
                    f = open('/root/bot_herobot_ls/resurses/zametki.txt', encoding='utf8')
                    text = 'Список твоих напоминаний\n'
                    for line in f:
                        zametka = line.split('***#***')
                        if zametka != ['\n'] and zametka[5] == str(event.obj.peer_id):
                            text += zametka[1]+'.'+zametka[0]+' на '+zametka[2]+':'+zametka[3]+' с текстом "' + zametka[4].capitalize()+'"\n'
                    if text == 'Список твоих напоминаний\n':
                        text = 'У тебя нет напоминаний'
                    sent_message(text, event.obj.peer_id)
                    f.close()
                    
                elif event.obj.text[11:14:] == " в ":
                    time_start = event.obj.text.split(' ')[3]
                    if correct_time(time_start, True) is True:
                        date_start = [datetime.datetime.now().month, datetime.datetime.now().day]

                        time_start = refactor_time_start(time_start)

                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ', 16,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[
                                                            event.obj.text.find(' ', 16, -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" завтра в "):] == " завтра в ":
                    time_start = event.obj.text.split(' ')[4]
                    if correct_time(time_start, False) is True:
                        date_start = [datetime.datetime.now().month, int(datetime.datetime.now().day) + 1]

                        if date_start[1] > calendar.monthrange(datetime.datetime.now().year, int(date_start[0]))[1]:
                            date_start[0] += 1
                            date_start[1] = 1
                            if date_start[0] > 12:
                                date_start[0] = 1

                        time_start = refactor_time_start(time_start)

                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " завтра в ") + 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " завтра в ") + 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на завтра создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" завтра утром "):] == " завтра утром ":
                    time_start = "9:00"
                    if correct_time(time_start, False) is True:
                        date_start = [datetime.datetime.now().month, int(datetime.datetime.now().day) + 1]

                        if date_start[1] > calendar.monthrange(datetime.datetime.now().year, int(date_start[0]))[1]:
                            date_start[0] += 1
                            date_start[1] = 1
                            if date_start[0] > 12:
                                date_start[0] = 1

                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " завтра утром ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " завтра утром ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на завтра создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" завтра днем "):] == " завтра днем " or event.obj.text[11:11 + len(
                        " завтра днём "):] == " завтра днём ":
                    time_start = "13:00"
                    if correct_time(time_start, False) is True:
                        date_start = [datetime.datetime.now().month, int(datetime.datetime.now().day) + 1]

                        if date_start[1] > calendar.monthrange(datetime.datetime.now().year, int(date_start[0]))[1]:
                            date_start[0] += 1
                            date_start[1] = 1
                            if date_start[0] > 12:
                                date_start[0] = 1

                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " завтра днем ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " завтра днем ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на завтра создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" завтра вечером "):] == " завтра вечером ":
                    time_start = "18:00"
                    if correct_time(time_start, False) is True:
                        date_start = [datetime.datetime.now().month, int(datetime.datetime.now().day) + 1]

                        if date_start[1] > calendar.monthrange(datetime.datetime.now().year, int(date_start[0]))[1]:
                            date_start[0] += 1
                            date_start[1] = 1
                            if date_start[0] > 12:
                                date_start[0] = 1

                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " завтра вечером ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " завтра вечером ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на завтра создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" утром "):] == " утром ":
                    time_start = "9:00"
                    if correct_time(time_start, True) is True:
                        date_start = [datetime.datetime.now().month, datetime.datetime.now().day]
                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " утром ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " утром ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" днем "):] == " днем " or event.obj.text[
                                                                           11:11 + len(" днём "):] == " днём ":
                    time_start = "13:00"
                    if correct_time(time_start, True) is True:
                        date_start = [datetime.datetime.now().month, datetime.datetime.now().day]
                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " днем ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " днем ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" вечером "):] == " вечером ":
                    time_start = "18:00"
                    if correct_time(time_start, True) is True:
                        date_start = [datetime.datetime.now().month, datetime.datetime.now().day]
                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                        11 + len(
                                                                                                            " вечером ") - 2,
                                                                                                        -1) + 1::] + '***#***' + str(
                            event.obj.peer_id) + '***#***' + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                           11 + len(
                                                                                               " вечером ") - 2,
                                                                                           -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text.split(' ')[2][0].isdigit():
                    date_start = event.obj.text.split(' ')[2]
                    if len(event.obj.text.split(' ')) < 5 or event.obj.text.split(' ')[4][0].isdigit() is False:

                        event.obj.text = event.obj.text.split(' ')
                        event.obj.text.insert(3, 'в')
                        event.obj.text.insert(4, '06:00')
                        input_text = input_text.split(' ')
                        input_text.insert(3, 'в')
                        input_text.insert(4, '06:00')

                        input_text = ' '.join(input_text)
                        event.obj.text = ' '.join(event.obj.text)

                    time_start = event.obj.text.split(' ')[4]
                    if correct_time(time_start, False) is True:
                        if correct_date(date_start) is True:
                            if int(date_start.split('.')[0]) == datetime.datetime.now().day and int(
                                    date_start.split('.')[
                                        1]) == datetime.datetime.now().month:
                                if correct_time(time_start, True) is False:
                                    continue
                                else:

                                    date_start = date_start.split('.')

                                    time_start = refactor_time_start(time_start)

                                    file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a",
                                                        encoding="utf8")
                                    file_zametki.write(
                                        str(date_start[1]) + '***#***' + str(date_start[0]) + '***#***' + time_start[
                                            0] + '***#***' + time_start[1] + '***#***' + input_text[
                                                                                         event.obj.text.find(' ',
                                                                                                             event.obj.text.find(
                                                                                                                 ' в ') + 3,
                                                                                                             -1) + 1::] + '***#***' + str(
                                            event.obj.peer_id) + '***#***' + '\n')
                                    file_zametki.close()
                                    text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                                       event.obj.text.find(
                                                                                                           ' в ') + 3,
                                                                                                       -1) + 1::] + "' в " + \
                                           time_start[0] + ':' + time_start[1] + " на " + str(
                                        date_start[0]) + '.' + str(
                                        date_start[1]) + " создано."
                                    sent_message(text, event.obj.peer_id)
                            else:
                                date_start = date_start.split('.')

                                time_start = refactor_time_start(time_start)

                                file_zametki = open("/root/bot_herobot_ls/resurses/zametki.txt", "a", encoding="utf8")
                                file_zametki.write(
                                    str(date_start[1]) + '***#***' + str(date_start[0]) + '***#***' + time_start[
                                        0] + '***#***' + time_start[1] + '***#***' + input_text[event.obj.text.find(' ',
                                                                                                                    event.obj.text.find(
                                                                                                                        ' в ') + 3,
                                                                                                                    -1) + 1::] + '***#***' + str(
                                        event.obj.peer_id) + '***#***' + '\n')
                                file_zametki.close()
                                text = "Напоминание с текстом: '" + input_text[event.obj.text.find(' ',
                                                                                                   event.obj.text.find(
                                                                                                       ' в ') + 3,
                                                                                                   -1) + 1::] + "' в " + \
                                       time_start[0] + ':' + time_start[1] + " на " + str(date_start[0]) + '.' + str(
                                    date_start[1]) + " создано."
                                sent_message(text, event.obj.peer_id)

                else:
                    sent_message(uncorrect_comand, event.obj.peer_id)
                    sent_message(format_command, event.obj.peer_id)

            except:
                sent_message(uncorrect_comand, event.obj.peer_id)
                sent_message(format_command, event.obj.peer_id)
