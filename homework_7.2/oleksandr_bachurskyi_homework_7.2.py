# ДЗ 7.2. Модифікувати рядок
# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так,
# щоб вони завжди починалися з великої літери та закінчувалися крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою
# Вхідні аргументи: string.
# Вихідні аргументи: string.
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
# pass

def correct_sentence(text):
    if text.strip() != "":
        if text[0].isupper() == False:
            text = text[0].upper() + text[1:]

        if text[-1] != '.':
            text += '.'
        return text
    else:
        return None


while True:
    input_text = input("Введіть речення: ")

    if input_text.strip() != "":
        print("Виправлене речення:", correct_sentence(input_text))
        break
    else:
        print("Введіть непорожній рядок.")
