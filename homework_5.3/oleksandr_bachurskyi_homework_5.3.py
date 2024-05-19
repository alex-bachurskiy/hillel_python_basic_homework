# ДЗ 5.3. hashtag
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

user_input = input("Введіть рядок: ")
words = user_input.split()

hashtag = ''

for word in words:
    clean_word = ''
    for symbol in word:
        if symbol not in string.punctuation:
            clean_word += symbol
    hashtag += clean_word.capitalize()

hashtag = '#' + hashtag.strip()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
