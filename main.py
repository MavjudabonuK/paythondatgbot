import telebot
from transliterate import to_cyrillic, to_latin

# Bot TOKEN-ni bu yerga qo'yasan (BotFather-dan olganing)
TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(token=TOKEN)

print("Bot ishga tushdi, Sumire! www")

# /start buyrug'i uchun
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.first_name
    answer = f"Assalomu alaykum, {username}! Men Kirill-Lotin botiman.\n"
    answer += "Matningizni yuboring, men uni o'girib beraman. Dattebayo! 🌀"
    bot.reply_to(message, answer)

# Matnlarni qayta ishlash uchun
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    # Agar matn kirillda bo'lsa lofinga, lotinda bo'lsa kirillga o'giradi
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    
    bot.reply_to(message, answer)

# Botni doimiy ishlatish
bot.polling()