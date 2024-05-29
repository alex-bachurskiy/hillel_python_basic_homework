# ДЗ 8.2. Паліандром
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
print("Test1: OK")
assert is_palindrome('aurora') == False, 'Test2'
print("Test2: OK")
