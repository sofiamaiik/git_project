# Завдання 1 Маємо два текстові файли. З’ясуйте, чи співпадають їхні рядки. Якщо ні, то виведіть із кожного файлу рядок, який не співпадає.
def compare_files(text1, text2):
    try:
        with open(text1, 'r', encoding='utf-8') as t1, open(text2, 'r', encoding='utf-8') as t2:
            lines1 = t1.readlines()
            lines2 = t2.readlines()
        for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
            if line1.strip() != line2.strip():
                print(f"Рядок {i} не співпадає:")
                print(f"  Файл 1: {line1.strip()}")
                print(f"  Файл 2: {line2.strip()}")
        if len(lines1) > len(lines2):
            print("Додаткові рядки у файлі 1:")
            for line in lines1[len(lines2):]:
                print(f"  {line.strip()}")
        elif len(lines2) > len(lines1):
            print("Додаткові рядки у файлі 2:")
            for line in lines2[len(lines1):]:
                print(f"  {line.strip()}")

    except FileNotFoundError as e:
        print(f"Помилка: файл не знайдено — {e.filename}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")


compare_files('text1.txt', 'text2.txt')


# Завдання 2 Маємо текстовий файл. Створіть новий файл і запишіть до
# нього наступну статистику за вихідним файлом: ■ кількість символів; ■ кількість рядків; ■ кількість голосних літер; ■ кількість приголосних літер; ■ кількість цифр.
def analyze_file(text1, text3):
    try:
        with open(text1, 'r', encoding='utf-8') as file:
            content = file.read()
        num_chars = len(content)
        num_lines = content.count('\n') + 1
        vowels = 'аеєиіїоуюяАЕЄИІЇОУЮЯaeiouyAEIOUY'
        consonants = (
            'бвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        )
        num_vowels = sum(1 for char in content if char in vowels)
        num_consonants = sum(1 for char in content if char in consonants)
        num_digits = sum(1 for char in content if char.isdigit())
        with open(text3, 'w', encoding='utf-8') as out_file:
            out_file.write(f"Кількість символів: {num_chars}\n")
            out_file.write(f"Кількість рядків: {num_lines}\n")
            out_file.write(f"Кількість голосних літер: {num_vowels}\n")
            out_file.write(f"Кількість приголосних літер: {num_consonants}\n")
            out_file.write(f"Кількість цифр: {num_digits}\n")

        print(f"Статистика успішно збережена у файл '{text3}'.")

    except FileNotFoundError:
        print(f"Помилка: файл '{text1}' не знайдено.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")


analyze_file('text1.txt', 'text3.txt')




# Завдання 3 Маємо текстовий файл. Видаліть з нього останній рядок. Результат запишіть до іншого файлу.
def remove_last_line(text1, text4):
    try:
        with open(text1, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines_without_last = lines[:-1]
        with open(text4, 'w', encoding='utf-8') as out_file:
            out_file.writelines(lines_without_last)

        print(f"Останній рядок успішно видалено. Результат записано у файл '{text4}'.")

    except FileNotFoundError:
        print(f"Помилка: файл '{text1}' не знайдено.")
    except Exception as e:
        print(f"Несподівана помилка: {e}")


remove_last_line('text1.txt', 'text4.txt')


# Завдання 4 Маємо текстовий файл. Знайдіть довжину найдовшого рядка.
with open('text1.txt', 'r') as file:
    lines = file.readlines()
max_length = 0
for line in lines:
    max_length = max(max_length, len(line))
print(f"Довжина найдовшого рядка: {max_length}")





# Завдання 5 Маємо текстовий файл. Підрахуйте кількість заданого користувачем слова у ньому.
def count_word_in_file(filename, word):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += line.lower().split().count(word.lower())

    return count
filename = input("Введіть назву файлу: ")
word = input("Введіть слово для пошуку: ")
result = count_word_in_file(filename, word)
print(f"Кількість входжень слова '{word}' у файлі: {result}")


# Завдання 6 Маємо текстовий файл. Знайдіть і замініть у ньому задане слово. Яке слово шукати і на яке замінювати — встановлюється користувачем.
def replace_word_in_file(filename, old_word, new_word):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            updated_line = line.replace(old_word, new_word)
            file.write(updated_line)
filename = input("Введіть назву файлу: ")
old_word = input("Введіть слово, яке потрібно замінити: ")
new_word = input("Введіть слово, на яке потрібно замінити: ")
replace_word_in_file(filename, old_word, new_word)
print(f"Слово '{old_word}' було замінено на '{new_word}' у файлі '{filename}'.")



