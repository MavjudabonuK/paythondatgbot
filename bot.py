import telebot
from transliterate import to_cyrillic, to_latin

# BotFather'dan olgan TOKEN'ingni shu yerga qo'y
TOKEN = 'TOKENINGIZNI_SHU_YERGA_YOZING' 
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# /start komandasi kelganda javob berish
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

# Har qanday xabar (text) kelganda uni o'girish
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message, answer)

# Botni ishga tushirish
print("Bot ishlamoqda... (Sumire uchun www)")
bot.polling()