# ДЗ 6.3. Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.

user_number = int(input("Введіть ціле число: "))

while user_number > 9:
    result = 1

    while user_number > 0:
        digit = user_number % 10
        result *= digit
        user_number //= 10
    user_number = result

print("Результат множення всіх цифр: ", user_number)
