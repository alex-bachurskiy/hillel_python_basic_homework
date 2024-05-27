# ДЗ 7.3. Пошук підрядка
# Функція second_index приймає як параметри 2 рядки.
# Вам необхідно знайти індекс другого входження шуканого рядка у рядку для пошуку.
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims".
# Якби нам треба було знайти її перше входження, то тут все просто:
# за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims",
# а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за рахунком.
# Значить індекс другого входження (і у відповідь питання) дорівнює 3.
# Рядок, який потрібно знайти, може складатися з кількох символів.
# Input: Два рядки (String).
# Output: Int or None
# Приклади:
# def second_index(text, some_str):
# pass

def second_index(text, some_str):
    first_occurrence = text.find(some_str)

    if first_occurrence == -1:
        return None

    second_occurrence = text.find(some_str, first_occurrence + 1)

    if second_occurrence == -1:
        return None

    return second_occurrence


some_text = input("Введіть будь-який текст: ")
some_string = input("Введіть будь-який рядок: ")
print("Індекс другого входження: ", second_index(some_text, some_string))
