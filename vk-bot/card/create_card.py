from PIL import Image, ImageColor, ImageDraw, ImageFont
import os


path = os.path.abspath(__file__)
directory = path[0:-14]


def create(name, surname, usr_id):
    bg = Image.open(directory + 'background.jpg', 'r') #Определяем путь к фону
    background = Image.new('RGB', (793, 559), '#ffffff') #Создаем холст для работы

    #Вставляем на холст фоновое изображение
    background.paste(bg)

    #Определяем путь и размер шрифта для текста
    smallFont=ImageFont.truetype(directory + 'Infinity.ttf', 20)
    bigFont=ImageFont.truetype(directory + 'AcquestScript.ttf', 60)
    
    #Создаем метод для надписей
    texting=ImageDraw.Draw(background)

    textLen = len(f'{name} {surname}') / 2
    x = 345 #Оффсет для текста
    #Устанавливаем ФИ получателя
    texting.text((x - (16 * textLen), 265), f'{name} {surname}', font=bigFont, fill = '#000000')

    #Устанавливаем id сертификата
    texting.text((x + 170, 100), f'№ C{usr_id}', font=smallFont, fill = '#000000')
    
    #Устанавливаем дату выдачи сертификата
    texting.text((x - 15, 440), f'{GetCurrentDate()}', font=smallFont, fill = '#000')

    #Сохраняем готовую карточку
    background.save(directory + 'out.png')

def GetCurrentDate():
    import datetime
    date = str(datetime.datetime.today().date()).split('-')
    return f'{date[2]}.{date[1]}.{date[0]}'