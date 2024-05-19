# ДЗ 5.2. Модифікувати калькулятор
# Модифікувати калькулятор таким чином, щоб він працював доти,
# доки користувач цього хоче. Тобто, потрібно робити запит до користувача на продовження роботи калькулятора
# після кожного обчислення - якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.

while True:
    first_number = float(input("Введіть перше число: "))
    math_operation = input("Введіть знак математичної дії: ")
    second_number = float(input("Введіть друге число: "))

    result = None

    match math_operation:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case '/':
            if second_number == 0:
                print("На нуль ділити неможна!")
            else:
                result = first_number / second_number
        case '**':
            result = first_number ** second_number
        case '//':
            result = first_number // second_number
        case '%':
            result = first_number % second_number
        case _:
            print("Такої математичної операції немає!")

    if result != None:
        print("Результат обчислення:", result)

    continue_calculation = input("Бажаєте продовжити обчислення? Якщо так, натисніть 'y', "
                                 "в іншому випадку натисніть будь-яку іншу клавішу: ")
    if continue_calculation.lower() != 'y':
        print("Програма завершила свою роботу")
        break
