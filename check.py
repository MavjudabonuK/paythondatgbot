from transliterate import to_cyrillic, to_latin

def transliterate_text(text):
    """Matnni lotindan kirillga va aksincha o'giruvchi funksiya"""
    if text.isascii(): # Agar matn lotin alifbosida bo'lsa
        return to_cyrillic(text)
    else: # Agar matn kirill alifbosida bo'lsa
        return to_latin(text)

# Sinab ko'ramiz
test_text = "Salom Sumire"
print(transliterate_text(test_text)) # Салом Сумире