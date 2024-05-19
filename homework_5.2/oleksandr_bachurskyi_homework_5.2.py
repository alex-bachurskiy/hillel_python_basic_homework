# ДЗ 5.2. Модифікувати калькулятор
# Модифікувати калькулятор таким чином, щоб він працював доти,
# доки користувач цього хоче. Тобто, потрібно робити запит до користувача на продовження роботи калькулятора
# після кожного обчислення - якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.

while True:
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
        print("Результат обчислення:", result)

    continue_calculation = input("Бажаєте продовжити обчислення? Якщо так, натисніть 'y', "
                                 "в іншому випадку натисніть будь-яку іншу клавішу: ")
    if continue_calculation.lower() != 'y':
        print("Програма завершила свою роботу")
        break
