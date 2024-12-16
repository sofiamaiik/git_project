# Завдання 1
# Напишіть програму, яка запитує у користувача ім('я та вік. Після отримання даних програма повинна виводити привітання '
# у форматі: "Привіт, {ім')я}! Твій вік — {вік}". Обробіть виняток, що виникає при введенні некоректного віку (вік < 0 або вік > 130),
# і виведіть повідомлення про помилку.
try:
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))

    if age < 0 or age > 130:
        raise ValueError("Вік має бути в межах від 0 до 130.")

    print(f"Привіт, {name}! Твій вік — {age}")
except ValueError as e:
    print(f"Помилка: {e}")



# Завдання 2
# Реалізуйте перше завдання через функцію. Функція повинна приймати ім('я і вік як параметри і повертати відформатований рядок. Перевірка коректності отриманих даних
# повинна бути всередині функції. Створіть дві версії реалізації функції:)
#
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.
#1!!!!!!!!!!!!!!!!!!!!!!!!!
def format(name, age):
    if age < 0 or age > 130:
        raise ValueError("Вік має бути в межах від 0 до 130.")
    return f"Привіт, {name}! Твій вік — {age}"

try:
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    print(format(name, age))
except ValueError as e:
    print(f"Помилка: {e}")

#2!!!!!!!!!!!!!!!!!!!
def safe_format(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Вік має бути в межах від 0 до 130.")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as e:
        return f"Помилка: {e}"
name = input("Введіть ваше ім'я: ")
try:
    age = int(input("Введіть ваш вік: "))
    print(safe_format(name, age))
except ValueError:
    print("Помилка: введено некоректне значення віку!")




# Завдання 3
# Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних (число більше нуля) чисел.
# Числа необхідно накопичувати у списку. Після отримання всіх значень програма повинна проаналізувати дані. У разі виявлення від'ємного значення
# програма має згенерувати виняток. Якщо всі значення у списку позитивні, програма має повернути на екран суму всіх чисел списку.)
#
# Згенерований виняток має бути оброблений кодом програми.
def positive_numbers():
    try:
        numbers = []
        print("Введіть додатні числа. Для завершення введіть 'стоп'.")
        while True:
            value = input("Число: ")
            if value.lower() == "стоп":
                break
            number = float(value)
            if number <= 0:
                raise ValueError(f"Виявлено недодатнє число: {number}")
            numbers.append(number)
        print(f"Сума всіх чисел: {sum(numbers)}")

    except ValueError as e:
        print(f"Помилка: {e}")
positive_numbers()




# Завдання 4
# Реалізуйте третє завдання через функцію. Функція повинна приймати список як аргумент і повертати суму елементів списку. Перевірка коректності
# отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
#
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.
#1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def calculate_sum(numbers):
    for number in numbers:
        if number <= 0:
            raise ValueError(f"Недодатнє число в списку: {number}")
    return sum(numbers)
try:
    user_numbers = [float(input("Введіть число: ")) for _ in range(3)]
    print(f"Сума чисел: {calculate_sum(user_numbers)}")
except ValueError as e:
    print(f"Помилка: {e}")


#2!!!!!!!!!!!!!!!!!!!!!!!!!
def safe_calculate_sum(numbers):
    try:
        for number in numbers:
            if number <= 0:
                raise ValueError(f"Недодатнє число в списку: {number}")
        return sum(numbers)
    except ValueError as e:
        return f"Помилка: {e}"
user_numbers = [float(input("Введіть число: ")) for _ in range(3)]
result = safe_calculate_sum(user_numbers)
print(result)



# Завдання 5
# Напишіть програму, яка дає змогу користувачеві заповнити список із клавіатури числами. Після отримання даних відобразіть на екран меню, яке дозволяє виконати такі операції:
#
# Відображення списку;
# Отримання максимального значення у списку;
# Отримання мінімального значення у списку;
# Відображення значення елемента за індексом, введеним користувачем;
# Видалення елемента за індексом, введеним користувачем.
# Обробіть виняток, що виникає під час виходу за межі списку (користувач ввів неправильне значення для індексу елемента в списку), і виведіть повідомлення про помилку.
def main():
    try:
        print("Введіть числа для заповнення списку. Для завершення введіть 'стоп'.")
        numbers = []
        while True:
            value = input("Число: ")
            if value.lower() == "стоп":
                break
            numbers.append(float(value))
        while True:
            print("\nМеню:")
            print("1. Відобразити список")
            print("2. Отримати максимальне значення")
            print("3. Отримати мінімальне значення")
            print("4. Відобразити елемент за індексом")
            print("5. Видалити елемент за індексом")
            print("6. Вийти")

            try:
                choice = int(input("Оберіть дію (1-6): "))
                if choice == 1:
                    print(f"Список: {numbers}")
                elif choice == 2:
                    print(f"Максимальне значення: {max(numbers)}")
                elif choice == 3:
                    print(f"Мінімальне значення: {min(numbers)}")
                elif choice == 4:
                    index = int(input("Введіть індекс: "))
                    print(f"Елемент за індексом {index}: {numbers[index]}")
                elif choice == 5:
                    index = int(input("Введіть індекс для видалення: "))
                    removed = numbers.pop(index)
                    print(f"Видалено елемент: {removed}")
                elif choice == 6:
                    print("Вихід з програми.")
                    break
                else:
                    print("Помилка: Неправильний вибір. Спробуйте ще раз.")
            except ValueError:
                print("Помилка: введіть число.")
            except IndexError:
                print("Помилка: індекс виходить за межі списку.")

    except ValueError:
        print("Помилка: введено некоректне значення.")
main()



# Завдання 6
# Реалізуйте третє завдання через функції. Створіть дві версії реалізації функцій:
#
# Перша версія не обробляє винятки всередині функцій. Уся обробка знаходиться зовні;
# Друга версія обробляє винятки всередині функцій.
#1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def calculate_positive_sum(numbers):
    for number in numbers:
        if number <= 0:
            raise ValueError(f"Недодатнє число: {number}")
    return sum(numbers)
try:
    numbers = []
    print("Введіть додатні числа. Для завершення введіть 'стоп'.")
    while True:
        value = input("Число: ")
        if value.lower() == "стоп":
            break
        numbers.append(float(value))
    result = calculate_positive_sum(numbers)
    print(f"Сума всіх чисел: {result}")
except ValueError as e:
    print(f"Помилка: {e}")
except Exception:
    print("Помилка: сталося щось неочікуване!")

#2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def safe_calculate_positive_sum(numbers):
    try:
        for number in numbers:
            if number <= 0:
                raise ValueError(f"Недодатнє число: {number}")
        return f"Сума всіх чисел: {sum(numbers)}"
    except ValueError as e:
        return f"Помилка: {e}"
numbers = []
print("Введіть додатні числа. Для завершення введіть 'стоп'.")
while True:
    value = input("Число: ")
    if value.lower() == "стоп":
        break
    try:
        numbers.append(float(value))
    except ValueError:
        print("Помилка: введено нечислове значення!")
result = safe_calculate_positive_sum(numbers)
print(result)
