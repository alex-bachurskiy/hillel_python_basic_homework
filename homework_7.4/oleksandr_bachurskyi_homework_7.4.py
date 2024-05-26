# ДЗ 7.4. Пошук спільних елементів
# Напишіть функцію common_elements, яка згенерує два списки елементів з
# генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
# def common_elements():
# pass

def common_elements():

    multiples_of_3 = []
    for i in range(1, 101):
        if i % 3 == 0:
            multiples_of_3.append(i)
    print("Список чисел кратних 3: ", multiples_of_3)

    multiples_of_5 = []
    for i in range(1, 101):
        if i % 5 == 0:
            multiples_of_5.append(i)
    print("Список чисел кратних 5: ", multiples_of_5)

    set_of_multiples_of_3 = set(multiples_of_3)
    set_of_multiples_of_5 = set(multiples_of_5)

    common_elements_set = set_of_multiples_of_3.intersection(set_of_multiples_of_5)

    return common_elements_set


print("Перетин чисел із двох списків: ", common_elements())
