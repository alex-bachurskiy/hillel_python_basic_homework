# ДЗ 6.2. Конвертер із числа в дату
# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години, хвилини і
# секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів,
# годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)

while True:
    user_seconds = int(input("Введіть, будь ласка, кількість секунд у діапазоні від 0 до 8639999: "))

    if 0 <= user_seconds < 8640000:
        break
    else:
        print("Це число не входить в діапазон допустимих значень!")

days = user_seconds // (24 * 60 * 60)
user_seconds %= (24 * 60 * 60)
hours = user_seconds // (60 * 60)
user_seconds %= (60 * 60)
minutes = user_seconds // 60
user_seconds %= 60

print(f"{days} {'день' if days == 1 else 'днів'}, "
      f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(user_seconds).zfill(2)}")
