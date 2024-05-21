# ДЗ 6.1. Діапазон букв
# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з усім набором потрібних букв

import string

input_letters = input("Введіть дві літери через дефіс (наприклад, a-z): ")

first_letter, second_letter = input_letters.split('-')

start_index = string.ascii_letters.index(first_letter)
end_index = string.ascii_letters.index(second_letter)

result = string.ascii_letters[start_index:end_index + 1]

print("Символи між введеними літерами:", result)
