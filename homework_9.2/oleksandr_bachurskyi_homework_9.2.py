# ДЗ 9.2. Різниця між числами
# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим (максимум) і найменшим (мінімум) елементом.
# Ваша функція difference має вміти працювати з невизначеною кількістю аргументів.
# Якщо аргументів немає, то функція повертає 0 (нуль).
# Якщо з 3-м тестом будуть проблеми, використовуйте функцію округлення round(x, 2),
# де х це число, яке потрібно округлити.
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).

def difference(*args):
    if not args:
        return 0
    else:
        min_val = min(args)
        max_val = max(args)
        return round(max_val - min_val, 2)


assert difference(1, 2, 3) == 2, 'Test1'
print("Test1: ОК")
assert difference(5, -5) == 10, 'Test2'
print("Test2: ОК")
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
print("Test3: ОК")
assert difference() == 0, 'Test4'
print("Test4: ОК")
