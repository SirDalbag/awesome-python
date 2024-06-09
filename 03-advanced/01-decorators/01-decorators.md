# Декораторы в Python

Декораторы в Python — это мощный инструмент для модификации поведения функций или методов. Они позволяют оборачивать одну функцию в другую, добавляя к ней дополнительные возможности без изменения ее кода.

## Основы декораторов

Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает новую функцию с измененным поведением.

```python
def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции.")
        func()
        print("Что-то происходит после вызова функции.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Декораторы с аргументами

Если функция, которую мы хотим обернуть, принимает аргументы, нужно чтобы обертка могла принимать и передавать эти аргументы.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что-то происходит перед вызовом функции.")
        result = func(*args, **kwargs)
        print("Что-то происходит после вызова функции.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

## Декораторы с аргументами для декоратора

Иногда декоратору нужны собственные аргументы. В этом случае мы создаем декоратор, который возвращает декоратор.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

## Декораторы методов

Декораторы могут использоваться и для методов классов. Важно помнить, что метод получает первый аргумент `self`, который нужно учитывать.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что-то происходит перед вызовом метода.")
        result = func(*args, **kwargs)
        print("Что-то происходит после вызова метода.")
        return result
    return wrapper

class MyClass:
    @my_decorator
    def say_hello(self, name):
        print(f"Hello, {name}!")

obj = MyClass()
obj.say_hello("Alice")
```

## Несколько декораторов

Можно применять несколько декораторов к одной функции. Они будут выполняться в порядке, обратном их объявлению.

```python
def decorator1(func):
    def wrapper():
        print("Декоратор 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Декоратор 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
```

## Пример комплексного использования декораторов

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} заняла {end_time - start_time} секунд.")
        return result
    return wrapper

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result
    return wrapper

@timer
@debug
def waste_time(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

waste_time(1000)
```