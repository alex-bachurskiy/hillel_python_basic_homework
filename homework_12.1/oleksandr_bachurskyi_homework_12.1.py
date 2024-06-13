# ДЗ 12.1. Очистити текст від html-тегів
# Ваше завдання написати функцію, яка прочитає заданий файл,
# очистить текст від html-тегів і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу, куди потрібно записати
# очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу, який може вийти на виході з
# очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.

import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)

    cleaned_text = re.sub(r'(\n\s*|\s*\n)', '\n', cleaned_text)

    cleaned_text = cleaned_text.strip()

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)


delete_html_tags('draft_oleksandr_bachurskyi_hw_12.1.html',
                 'cleaned_oleksandr_bachurskyi_hw_12.1.txt')
