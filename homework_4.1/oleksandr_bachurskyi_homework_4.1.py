# ДЗ 4.1. Перемістити всі нулі до кінця списку
# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

user_list = [0, 13, 1, 0, 0, 21, 0, 3, 9, 4, 15]

if user_list.count(0) == 0:
    print("В цьому списку немає нулів!")
else:
    print("Початковий список: ", user_list)

    for number in user_list:
        if number == 0:
            user_list.remove(0)
            user_list.append(0)
    print("Кінцевий результат:", user_list)
