import telebot
from ServiceRequest import get_price
from telebot import types
from Event import Event
from DataHandler import DataHandler

bot = telebot.TeleBot('1086688835:AAFZ2XwOcVdd1MC_d2KJCv4UoIHGnsmni4I')

o_longitude = None
o_latitude = None
d_longitude = None
d_latitude = None

@bot.message_handler(commands=['start'])
def command_start(m):
    bot.send_message(m.chat.id, "Hola\nbienvenido a Lyftimum\nPor favor envíenos su ubicación de origen")
    
@bot.message_handler(content_types=['location'])
def get_origin(m):
    global  o_longitude
    global  o_latitude
    o_longitude = m.location.longitude
    o_latitude = m.location.latitude 
    bot.send_message(m.chat.id, "Ahora, por favor envíe su ubicación de destino")
    bot.register_next_step_handler(m, get_destination)

def get_destination(m):
    global d_longitude
    global d_latitude
    d_longitude = m.location.longitude
    d_latitude = m.location.latitude
    coordinates = {"o_longitude" :o_longitude,
                "o_latitude":o_latitude, 
                "d_longitude":d_longitude, 
                "d_latitude":d_latitude}
    prices = get_price(coordinates)
    sevent = Event(m.chat.id, o_latitude, o_longitude, d_latitude, d_longitude, prices)
    data_handler = DataHandler()
    data_handler.add_event(sevent)
    
    bot.send_message(m.chat.id, 'Aquí están tus precios deseados:\nTAPSI:{}\nSNAPP:{}'.format(prices['TAPSI'], prices['SNAPP']))



bot.polling()