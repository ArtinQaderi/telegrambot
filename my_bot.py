import telebot

TOKEN = "7662406528:AAHurAZgU4mZfiqun-yDZi6xnsXuHQdcJWs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اين ربات توسط .... با پايتون ساخته شده")

bot.polling()