# -- coding: utf-8 --
import telebot
import time
import random
anime = ['Посмотрете Клинок Рассекающий Демонов', 'Посмотрете Наруто', 'Посмотрете Ван пис', 'Посмотрите Хантер х Хантер', 'Посмотрите Атаку Титанов', 'Посмотрите Код геас: восставший лелуш', 'Посмотрите Ван Панчмен', 'Помотрите Ох уж этот экстрасенс Сайки Кусусо', 'Посмотрите Драгон Бол', 'Посмотрите Токийских Мстителей']
anime_logo = [['kimetsu_no_jaiba_1.jpg', 'kimetsu_no_jaiba_2.jpg'], ['Naruto_1.jpg', 'Naruto_2.jpg'], ['One_piece_1.jpg', 'One_piece_2.jpg'], ['Hunter_x_Hunter_1.jpg', 'Hunter_x_Hunter_2.jpg'], ['Atack_on_Titans_1.jpg', 'Atack_on_Titans_2.jpg'], ['Code_Geass_Risen_Lelouch_1.jpg', 'Code_Geass_Risen_Lelouch_2.jpg'], ['One_punchman_1.jpg', 'One_punchman_2.jpg'], ['Oh_that_psychic_Saiki_Kususo_1.jpg', 'Oh_that_psychic_Saiki_Kususo_2.jpg'], ['Dragon_Ball_1.jpg', 'Dragon_Ball_2.jpg'], ['Tokio_Revengers_1.jpg', 'Tokio_Revengers_2.jpg']]

token = '5352728096:AAG0r9gLdetFmi_RwQVCtHqS3LSd8PawKGA'
Bot = telebot.TeleBot(token)

@Bot.message_handler(commands=['start'])
def start(message):
    Bot.send_message(message.chat.id, 'Приветствую! Этого бота сделал Тихон')
    time.sleep(3)
    if message.chat.first_name != None and message.chat.last_name != None:
        Bot.send_message(message.chat.id, message.chat.username + ' или лучше ' + message.chat.first_name + message.chat.last_name)
    time.sleep(3)
    Bot.send_message(message.chat.id, 'К сожелению бот ещё на стадии разроботки')
    time.sleep(3)
    Bot.send_message(message.chat.id, 'Могу вам посоветовать посмотреть аниме лишь напишите /recommend')

@Bot.message_handler(commands=['recommend'])
def recommend(message):
    RAND0M = random.randint(0, 9)
    RANDOM = random.randint(0, 1)
    image = anime_logo[RAND0M] [RANDOM]
    img = open(image, 'rb')
    Bot.send_message(message.chat.id, anime[RAND0M])
    Bot.send_photo(message.chat.id, img)
    img.close()

@Bot.message_handler(content_types=['text'])
def fightback(message):
    Bot.send_message(message.chat.id, 'Если это аргумент уважения')
    time.sleep(3)
    Bot.send_message(message.chat.id, 'То спасибо')
    time.sleep(3)
    Bot.send_message(message.chat.id, 'Если издевка')
    time.sleep(3)
    Bot.send_message(message.chat.id, 'То сам такой')

Bot.polling()