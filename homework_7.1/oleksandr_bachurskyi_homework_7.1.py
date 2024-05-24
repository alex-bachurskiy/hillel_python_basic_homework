# ДЗ 7.1. Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.
# Замініть pass на Ваше рішення.
# def say_hi(name, age):
# pass

# Функція "say_hi"
def say_hi(name, age):
    if age == 1:
        years = "рік"
    elif 2 <= age <= 4:
        years = "роки"
    else:
        years = "років"

    greeting = f"Привіт. Мене звати {name} і мені {age} {years}"
    return greeting


# Функція "say_hi" на практиці
while True:
    user_name = input("Введіть ваше ім'я: ")

    if user_name.isalpha():
        break
    else:
        print("Ви ввели некоректне ім'я! Будь ласка, введіть ваше ім'я ще раз:")

while True:
    user_age_input = input("Введіть ваш вік: ")
    if user_age_input.isdigit():
        user_age = int(user_age_input)
        if user_age > 0:
            break
    print("Введіть коректне ціле число, більше нуля!")

print(say_hi(user_name, user_age))
