"""
Задача 1: Простая функция.
 - написать функцию, которая принимает два числа и возвращает их произведение.
"""

def multiply(a, b):
    return a * b

"""
Задача 2: Функция с параметрами по умолчанию.
 - написать функцию, которая принимает имя и возвращает приветствие.
 - если имя не передано, использовать "John" по умолчанию.
"""

def hello(name="John"):
    return "Hello, " + name

"""
Задача 3: Произвольное количество аргументов.
 - написать функцию, которая принимает любое количество чисел и возвращает их сумму.
"""

def sum(*args):
    return sum(args)

"""
Задача 4: Лямбда-функции
 - использовать лямбда-функцию в комбинации с функцией map, чтобы получить список квадратов чисел от 1 до 10.
"""

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, n))
print(squares)