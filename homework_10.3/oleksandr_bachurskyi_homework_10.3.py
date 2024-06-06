# ДЗ 10.3. Перевірити чи є парним чи ні
# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.

def is_even(digit):
    """ Перевірка чи є парним число """
    if digit % 2 == 0:
        return True
    else:
        return False


assert is_even(2) == True, 'Test1'
print('Test1: OK')
assert is_even(5) == False, 'Test2'
print('Test2: OK')
assert is_even(0) == True, 'Test3'
print('Test3: OK')
