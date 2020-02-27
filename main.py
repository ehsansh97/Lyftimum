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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtnrealtime = types.KeyboardButton('Now')
    itembtnpostponed = types.KeyboardButton('For a specific period of time')
    markup.row(itembtnrealtime, itembtnpostponed)
    bot.send_message(m.chat.id, "Hey! Welcome to Lyftimum\nThe only service we provide you by now is to tell you how much it would cost you if you use either of the main online taxi services of Iran, TAPSI or Snapp for your travel.")
    bot.send_message(m.chat.id, "Now Please choose:", reply_markup=markup)
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🔙')
def menu(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtnrealtime = types.KeyboardButton('Now')
    itembtnpostponed = types.KeyboardButton('For a specific period of time')
    markup.row(itembtnrealtime, itembtnpostponed)
    bot.send_message(m.chat.id, "o, you're back! you don't have much choice, do you?", reply_markup=markup)

@bot.message_handler(content_types=['text'], func=lambda message: message.text == 'Now')
def realtime(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtnmenu = types.KeyboardButton('🔙')
    markup.row(itembtnmenu)
    bot.send_message(m.chat.id, "Now Please send us your origin location", reply_markup=markup)
    
@bot.message_handler(content_types=['text'], func=lambda message: message.text == 'For a specific period of time')
def postponed(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtnmenu = types.KeyboardButton('🔙')
    markup.row(itembtnmenu)
    bot.send_message(m.chat.id, "Sorry, This service is not up yet, coming soon!", reply_markup=markup)

    
@bot.message_handler(content_types=['location'])
def get_origin(m):
    global  o_longitude
    global  o_latitude
    o_longitude = m.location.longitude
    o_latitude = m.location.latitude 
    bot.send_message(m.chat.id, "Now Please send us your destination location")
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtnmenu = types.KeyboardButton('🔙')
    markup.row(itembtnmenu)
    bot.send_message(m.chat.id, 'Your desired travel would cost you:\nTAPSI: {}\nSNAPP: {}'.format(prices['TAPSI'], prices['SNAPP']), reply_markup=markup)



bot.polling()
