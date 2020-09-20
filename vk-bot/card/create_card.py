from PIL import Image, ImageColor, ImageDraw, ImageFont
import os

path = os.path.abspath(__file__)
file_link = path[0:-14] + 'outfile.png'


def create(name, surname, usr_id, dataStart, dataEnd, directory):
    img = Image.open(directory + 'avatar.jpg', 'r') #Определяем путь для аватара
    bg = Image.open(directory + 'background.png', 'r') #Определяем путь к фону
    background = Image.new('RGB', (710, 386), '#ffffff') #Создаем холст для работы
    offset = (45, 39) #Оффсет аватарки пользователя

    #Вставляем на холст фоновое изображение и аватар пользователя
    background.paste(bg)
    background.paste(img, offset)

    #Определяем путь и размер шрифта для текста
    smallFont=ImageFont.truetype(path[0:-14] + 'Infinity.ttf',16)
    bigFont=ImageFont.truetype(path[0:-14] + 'Infinity.ttf',30)
    #Создаем метод для надписей
    texting=ImageDraw.Draw(background)

    x = 295 #Оффсет для текста
    #Устанавливаем заголовок карточки
    texting.text((x + 5, 40), 'Сущность/Организация', font=bigFont, fill = '#000000')
    #Устанавливаем заголовки для полей
    texting.text((x, 85), 'Имя', font=smallFont, fill = '#000000')
    texting.text((x, 140), 'Фамилия', font=smallFont, fill = '#000000')
    texting.text((x, 197), 'Id Вк', font=smallFont, fill = '#000000')
    #Устанавливаем данные под заголовками
    texting.text((x, 104), name, font=smallFont, fill = '#000000')
    texting.text((x, 158), surname, font=smallFont, fill = '#000000')
    texting.text((x, 218), usr_id, font=smallFont, fill = '#000000')

    #Прочее(Срок действия, марки)
    texting.text((x + 170, 85), 'Начало действия', font=smallFont, fill = '#000000')
    texting.text((x + 170, 140), 'Истекает до', font=smallFont, fill = '#000000')
    texting.text((50, 355), 'Имя', font=smallFont, fill = '#000000')
    #Устанавливаем данные под заголовками
    texting.text((x + 170, 104), dataStart, font=smallFont, fill = '#000000')
    texting.text((x + 170, 158), dataEnd, font=smallFont, fill = '#000000')

    #Сохраняем готовую карточку
    background.save(directory + 'out.png')