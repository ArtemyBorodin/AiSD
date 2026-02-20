a = [1, 2, 3]
s = 0
for i in a:
    s += i
avg1 = s / len(a)

b = [4, 5, 6]
s2 = 0
for i in b:
    s2 += i
avg2 = s2 / len(b)

c = [4, 5, 8]
s3 = 0
for i in c:
    s3 += i
avg3 = s3 / len(c)

def calculate_average(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa / len(numbers)

print(calculate_average(a))
print(calculate_average(b))
print(calculate_average(c))

# 🔹 Задание 1 — Максимум и минимум в нескольких списках
numbers_a = [3, 5, 1]
numbers_b = [10, 7, 12]
numbers_c = [4, 8, 6]

def find_max_num(numbers):
    """Функция, которая находит максимальный элемент в списке

    Args:
        numbers(list): список чисел
    Returns:
        int: максимальное число
    """
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def find_min_num(numbers):
    """Функция, которая находит минимальный элемент в списке

    Args:
        numbers(list): список чисел
    Returns:
        int: минимальное число
    """
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

print(find_max_min_num(numbers_a))
print(find_max_min_num(numbers_b))
print(find_max_min_num(numbers_c))
print(find_max_min_num.__doc__)
# Что делает:
# Находит максимум и минимум в трёх списках
# Что нужно сделать:
# Создать функцию get_min_max(numbers) — возвращает кортеж (min, max) для списка.
# Использовать функцию для списков a, b, c.
# Вывести результаты.