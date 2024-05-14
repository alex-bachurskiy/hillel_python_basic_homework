# ДЗ 4.3. Список із 3 елементів
# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

import random

random_count = random.randint(3, 10)
random_list = random.sample(range(1, 16), random_count)

print("Початковий список:", random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]

print("Новий список:", new_list)
