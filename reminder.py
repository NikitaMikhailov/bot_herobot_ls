#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random, requests, vk_api, os, bs4
import datetime, requests, vk_api, calendar
from vk_api.utils import get_random_id

# сделать проверку при переходе на завтра в последний день месяца !!done
# сделать проверку на правильную дату !!done


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений

#file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "w", encoding="utf8")
#file_zametki.close()


def sent_message(text, user_id):
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=text
    )


def correct_date(date_start):
    if int(date_start.split('.')[1]) < 1 or int(date_start.split('.')[1]) > 12 or int(
            date_start.split('.')[0]) < 1 or int(date_start.split('.')[0]) > \
            calendar.monthrange(datetime.datetime.now().year, int(date_start.split('.')[1]))[1]:
        text = 'Дата задана некорректно'
        sent_message(text, event.obj.peer_id)
        return False
    print(date_start)
    if int(date_start.split('.')[1]) <= datetime.datetime.now().month and int(
            date_start.split('.')[0]) < datetime.datetime.now().day or int(
        date_start.split('.')[1]) < datetime.datetime.now().month:
        text = 'Указанная дата меньше текущей'
        sent_message(text, event.obj.peer_id)
        return False
    return True


def correct_time(time_start, today_flag):
    if int(time_start.split(':')[0]) < 0 or int(time_start.split(':')[0]) > 23 or int(
            time_start.split(':')[1]) < 0 or int(time_start.split(':')[1]) > 59:
        text = 'Время задано некорректно'
        sent_message(text, event.obj.peer_id)
        return False
    if today_flag is True and datetime.time(int(time_start.split(':')[0]),
                                            int(time_start.split(':')[1])) <= datetime.time(
        datetime.datetime.now().hour, datetime.datetime.now().minute):
        text = 'Указанное время меньше текущего'
        sent_message(text, event.obj.peer_id)
        return False
    return True


for event in longpoll.listen():
    # print(event)
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_user:
        event.obj.text = event.obj.text.lower()
        if event.obj.text[:11:] == "напомни мне":
            try:
                if event.obj.text == "напомни мне":
                    text = "Я могу помочь тебе не забывать важную информацию"
                    sent_message(text, event.obj.peer_id)
                    text = "Формат команды:\n'напомни мне\n+\nв hh:mm\nзавтра в hh:mm\nзавтра утром/днем/вечером\nday.month в hh:mm\n+\nтекст напоминания.'"
                    sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:14:] == " в ":
                    time_start = event.obj.text.split(' ')[3]
                    # print(time_start)
                    if correct_time(time_start, True) is True:
                        date_start = [datetime.datetime.now().month, datetime.datetime.now().day]
                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[
                                                                         event.obj.text.find(' ', 16, -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[
                                                            event.obj.text.find(' ', 16, -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text[11:11 + len(" завтра в "):] == " завтра в ":
                    time_start = event.obj.text.split(' ')[4]
                    # print(time_start)
                    if correct_time(time_start, False) is True:
                        date_start = [datetime.datetime.now().month, int(datetime.datetime.now().day) + 1]

                        if date_start[1] > calendar.monthrange(datetime.datetime.now().year, int(date_start[0]))[1]:
                            date_start[0] += 1
                            date_start[1] = 1
                            if date_start[0] > 12:
                                date_start[0] = 1

                        time_start = time_start.split(':')
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " завтра в ") + 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " завтра утром ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " завтра днем ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " завтра вечером ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " утром ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " днем ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
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
                        file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                        file_zametki.write(str(date_start[0]) + '***#***' + str(date_start[1]) + '***#***' + time_start[
                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                            11 + len(
                                                                                                                " вечером ") - 2,
                                                                                                            -1) + 1::] + '\n')
                        file_zametki.close()
                        text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
                                                                                               11 + len(
                                                                                                   " вечером ") - 2,
                                                                                               -1) + 1::] + "' в " + \
                               time_start[0] + ':' + time_start[1] + " на сегодня создано."
                        sent_message(text, event.obj.peer_id)

                elif event.obj.text.split(' ')[2][0].isdigit():
                    date_start = event.obj.text.split(' ')[2]
                    time_start = event.obj.text.split(' ')[4]
                    if correct_time(time_start, False) is True:
                        if correct_date(date_start) is True:
                            if int(date_start.split('.')[0]) == datetime.datetime.now().day and int(date_start.split('.')[
                                1]) == datetime.datetime.now().month:
                                if correct_time(time_start, True) is False:
                                    continue
                                else:
                                    date_start = date_start.split('.')
                                    time_start = time_start.split(':')
                                    file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                                    file_zametki.write(
                                        str(date_start[1]) + '***#***' + str(date_start[0]) + '***#***' + time_start[
                                            0] + '***#***' + time_start[1] + '***#***' + event.obj.text[
                                                                                         event.obj.text.find(' ',
                                                                                                             event.obj.text.find(
                                                                                                                 ' в ') + 3,
                                                                                                             -1) + 1::] + '\n')
                                    file_zametki.close()
                                    text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
                                                                                                           event.obj.text.find(
                                                                                                               ' в ') + 3,
                                                                                                           -1) + 1::] + "' в " + \
                                           time_start[0] + ':' + time_start[1] + " на " + str(
                                        date_start[0]) + '.' + str(
                                        date_start[1]) + " создано."
                                    sent_message(text, event.obj.peer_id)
                            else:
                                date_start = date_start.split('.')
                                time_start = time_start.split(':')
                                file_zametki = open("/root/bot_herobot_chat/resurses/zametki.txt", "a", encoding="utf8")
                                file_zametki.write(
                                    str(date_start[1]) + '***#***' + str(date_start[0]) + '***#***' + time_start[
                                        0] + '***#***' + time_start[1] + '***#***' + event.obj.text[event.obj.text.find(' ',
                                                                                                                        event.obj.text.find(
                                                                                                                            ' в ') + 3,
                                                                                                                        -1) + 1::] + '\n')
                                file_zametki.close()
                                text = "Напоминание с текстом: '" + event.obj.text[event.obj.text.find(' ',
                                                                                                       event.obj.text.find(
                                                                                                           ' в ') + 3,
                                                                                                       -1) + 1::] + "' в " + \
                                       time_start[0] + ':' + time_start[1] + " на " + str(date_start[0]) + '.' + str(
                                    date_start[1]) + " создано."
                                sent_message(text, event.obj.peer_id)

                else:
                    text = "Команда напоминания некорректна"
                    sent_message(text, event.obj.peer_id)
                    text = "Формат команды:\n'напомни мне\n+\nв hh:mm\nзавтра в hh:mm\nзавтра утром/днем/вечером\nday.month в hh:mm\n+\nтекст напоминания.'"
                    sent_message(text, event.obj.peer_id)

            except:
                text = "Команда напоминания некорректна"
                sent_message(text, event.obj.peer_id)
                text = "Формат команды:\n'напомни мне\n+\nв hh:mm\nзавтра в hh:mm\nзавтра утром/днем/вечером\nday.month в hh:mm\n+\nтекст напоминания.'"
                sent_message(text, event.obj.peer_id)
