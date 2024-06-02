"""
Задача 1: Проверка числа
 - проверяет число положительное, отрицательное или равно нулю
 - проверяет число четное или нечетное
"""

n = int(input())
if n > 0:
    print("Число положительное")
elif n < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

if n % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

"""
Задача 2: Максимальное из трех чисел
 - найти наибольшее число из трех чисел
"""

a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(f"Наибольшее число: {a}")
elif b >= a and b >= c:
    print(f"Наибольшее число: {b}")
else:
    print(f"Наибольшее число: {c}")

"""
Задача 3: Сумма чисел
 - вывести сумму всех чисел от 1 до 100
"""

sum = 0
for i in range(1, 101):
    sum += i
print(f"Сумма чисел от 1 до 100: {sum}")

"""
Задача 4: Факториал числа
 - вывести факториал числа
"""

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Факториал числа {n}: {fact}")