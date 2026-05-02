import telebot
from telebot import types # Tugmachalar uchun
from transliterate import to_cyrillic, to_latin

TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

# 1. /start buyrug'i (Naruto uslubida)
@bot.message_handler(commands=['start'])
def start_shinobi(message):
    user = message.from_user.first_name
    text = f"Konnichiwa, {user}-san! 🌀\n\nMen **Ren Fuji** tomonidan Sumire uchun yaratilgan maxsus botman! www\n"
    text += "Matningizni yuboring, men uni Kirill yoki Lotinga o'girib beraman. Dattebayo!"
    
    # Rasm yuborish (agar xohlasang biron Naruto rasmi linkini qo'yishing mumkin)
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# 2. Asosiy transliteratsiya funksiyasi
@bot.message_handler(func=lambda msg: True)
def handle_translit(message):
    original_text = message.text
    
    if original_text.isascii():
        converted_text = to_cyrillic(original_text)
        from_lang, to_lang = "Lotin", "Kirill"
    else:
        converted_text = to_latin(original_text)
        from_lang, to_lang = "Kirill", "Lotin"

    # Javobni chiroyli ramkaga olamiz
    response = f"✨ **Natija ({from_lang} ➡️ {to_lang}):**\n\n`{converted_text}`\n\n---"
    response += "\nSumire, kodingiz muvaffaqiyatli ishladi! www"

    # Tugmacha qo'shish (nusxa olish qulay bo'lishi uchun)
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Yana bitta! ⚡", callback_data="again")
    markup.add(btn)

    bot.reply_to(message, response, parse_mode="Markdown", reply_markup=markup)

print("Ren Fuji boti Sumireni kutmoqda... (Running)")
bot.polling()