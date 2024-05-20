# ДЗ 5.1. Ім'я змінної
# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

import string
import keyword

while True:
    name = input("Будь ласка, введіть рядок, який ви б хотіли перевірити як можливе ім'я змінної. "
                 "Для виходу введіть 'exit': ")

    if name == "exit":
        print("Програма завершила свою роботу.")
        break

    else:
        allowed_symbols = string.ascii_letters + string.digits + "_"

        if name[0].isdigit():
            print(False)
            continue

        if any(symbol.isupper() for symbol in name):
            print(False)
            continue

        if any(symbol not in allowed_symbols for symbol in name):
            print(False)
            continue

        if name.count("_") > 1:
            print(False)
            continue

        if name in keyword.kwlist:
            print(False)
            continue

        print(True)
