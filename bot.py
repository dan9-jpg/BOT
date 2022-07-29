import types
import telebot
from telebot import types
bot = telebot.TeleBot('5316533192:AAGclQIAUZmCd-Vbdfqy0pgk7pK8c9y9zOI')
@bot.message_handler(commands=['start'])
def start (message):
	mess=f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
	bot.send_message(message.chat.id, mess, parse_mode='html')
	
@bot.message_handler(commands=['website'])
def website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://my.mail.ru/mail/t.verbickii"))

	bot.send_message(message.chat.id,'Перейдите на сайт!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	website = types.KeyboardButton('Веб сайт')
	start = types.KeyboardButton('Start')
	markup.add(website,start)
	bot.send_message(message.chat.id,"SUKA", reply_markup=markup)

@bot.message_handler(content_types={'text'})
def get_user_text(message):
	if message.text =='Hello':
		bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
	elif message.text == 'id':
		bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
	elif message.text == 'photo':
		photo=open('TARAS.png ', 'rb')
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, "ТРАХАТЬ")
	else:
		bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(non_stop=True)
