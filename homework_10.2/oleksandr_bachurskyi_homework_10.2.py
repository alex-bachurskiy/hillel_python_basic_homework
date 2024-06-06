# ДЗ 10.2. Знайти перше слово
# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
# При розв'язанні задачі зверніть увагу на наступні моменти:
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок.

import re

def first_word(text):
    """ Пошук першого слова """
    found = re.findall(r"[a-zA-Z']+", text)
    if found:
        return found[0]
    else:
        return ""


assert first_word("Hello world") == "Hello", 'Test1'
print('Test1: OK')
assert first_word("greetings, friends") == "greetings", 'Test2'
print('Test2: OK')
assert first_word("don't touch it") == "don't", 'Test3'
print('Test3: OK')
assert first_word(".., and so on ...") == "and", 'Test4'
print('Test4: OK')
assert first_word("hi") == "hi", 'Test5'
print('Test5: OK')
assert first_word("Hello.World") == "Hello", 'Test6'
print('Test6: OK')
