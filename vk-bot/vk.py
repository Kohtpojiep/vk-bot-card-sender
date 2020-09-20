import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import json
import requests #модуль для взаимодействия с сайтом
import os
import sys
import datetime

#использование файлов
import card.create_card as cc
from vktoken import group_token

#Если нет соединения с вк
def StartAgain():
    import time
    print('Bot is down...')
    time.sleep(30)
    python = sys.executable
    os.execl(python, python, *sys.argv)

#объявление глобальных переменных
vk = vk_api.VkApi(token=group_token)
try:
    vk._auth_token()
    vk.get_api()
    longpoll = VkBotLongPoll(vk, 198871990)
except:
    StartAgain()

path = os.path.abspath(__file__)
path = path[0:-5] #директория папки данного бота
card_link = path + 'card\\'
file_link = path + 'card\\avatar.jpg'
res_link = path + 'card\\out.png'

#отправка текстового сообщения
def sender(id, text):
    vk.method('messages.send',{'peer_id': id, 'message': text, 'random_id': 0})

#отправка сообщения с содержимым
def senderAttach(peer_id, text, attachment):
    vk.method('messages.send',  {'peer_id': peer_id, 'message': text,'attachment': attachment, 'random_id': 0})

#получение информации о пользователе
def getInfo(id):
    userInfo = vk.method('users.get',{'user_ids': id, 'fields': 'photo_200'})
    info = [str(userInfo[0]['photo_200']),
                str(userInfo[0]['first_name']),
                str(userInfo[0]['last_name']),
                str(userInfo[0]['id'])
                ]
    return info

#скачивание по ссылке
def download_avatar(url):
    r = requests.get(url)
    with open(file_link, "wb") as code:
        code.write(r.content)
    print(file_link)
    return file_link

#отправка фотокарточки
def send_card(user_id):
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open(res_link, 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    photo = f'photo{c["owner_id"]}_{c["id"]}'
    vk.method("messages.send", {"peer_id": user_id, "message": "Держи", "attachment": photo,"random_id": 0})

#команды доступные в личных сообщениях
def directMessage(event):
    msg = event.object.text.lower()
    from_id = event.object.from_id
    peer_id = event.object.peer_id

    if event.object.text.lower() == "привет":
        vk.method("messages.send", {"user_id": event.object.peer_id, "message": event.object.text, "random_id": 0})
        return

    if(msg.startswith(('карточка', 'карточку','картонку')) or 'сертификат' in msg):
        dataStart = '01.09.2020'
        dataEnd = '01.12.2020'
        info = getInfo(from_id)
        download_avatar(info[0])
        cc.create(info[1], info[2], info[3], dataStart, dataEnd,card_link)
        send_card(peer_id)

try:
    while True:
        #прослушивание событий, то есть новых сообщений
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id == event.object.from_id or event.object.peer_id == 2000000001:
                    directMessage(event)

except Exception as ex:
    StartAgain()