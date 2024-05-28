# ДЗ 8.3. Унікальне число
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та
# повертати його. Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде
# кілька унікальних чисел, перевіряти не потрібно.

def find_unique_value(some_list):
    for num in some_list:
        if some_list.count(num) == 1:
            return num


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
print("Test1: ОК")
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
print("Test2: ОК")
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("Test3: ОК")
