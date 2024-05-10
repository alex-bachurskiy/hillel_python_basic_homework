# ДЗ 3.1. Найпростіший калькулятор
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами,
# а програма, виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

first_number = float(input("Введіть перше число: "))
math_operations = input("Введіть знак математичної дії: ")
second_number = float(input("Введіть друге число: "))

result = None

if math_operations != '+' and \
        math_operations != '-' and \
        math_operations != '*' and \
        math_operations != '/' and \
        math_operations != '**' and \
        math_operations != '//' and \
        math_operations != '%':
    print("Такої математичної операції немає!")
else:
    if math_operations == '+':
        result = first_number + second_number
    elif math_operations == '-':
        result = first_number - second_number
    elif math_operations == '*':
        result = first_number * second_number
    elif math_operations == '/':
        if second_number == 0:
            print("На нуль ділити неможна!")
        else:
            result = first_number / second_number
    elif math_operations == '**':
        result = first_number ** second_number
    elif math_operations == '//':
        result = first_number // second_number
    elif math_operations == '%':
        result = first_number % second_number

if result != None:
    print("Результат обчислення: ", result)
