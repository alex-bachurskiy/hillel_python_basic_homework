# ДЗ 3.3. Розділити один список на два списки
# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.

first_list = [25, 13, 0, 5]
second_list = [9, 5, 17, 1, 50]
third_list = []

if len(first_list) % 2 == 0:
    first_result = [first_list[:len(first_list)//2], first_list[len(first_list)//2:]]
else:
    first_result = [first_list[:(len(first_list)+1)//2], first_list[(len(first_list)+1)//2:]]

if len(second_list) % 2 == 0:
    second_result = [second_list[:len(second_list)//2], second_list[len(second_list)//2:]]
else:
    second_result = [second_list[:(len(second_list)+1)//2], second_list[(len(second_list)+1)//2:]]

if len(third_list) % 2 == 0:
    third_result = [third_list[:len(third_list)//2], third_list[len(third_list)//2:]]
else:
    third_result = [third_list[:(len(third_list)+1)//2], third_list[(len(third_list)+1)//2:]]

print('Було:', first_list, 'Стало:', first_result)
print('Було:', second_list, 'Стало:', second_result)
print('Було:', third_list, 'Стало:', third_result)
