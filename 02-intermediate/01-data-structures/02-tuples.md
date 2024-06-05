# Кортежи

Кортежи — это упорядоченные неизменяемые коллекции объектов в Python. Кортежи позволяют хранить элементы разных типов, но не позволяют изменять их после создания.

## Создание кортежей

```python
# Создание пустого кортежа
empty_tuple = ()

# Создание кортежа с элементами
fruits = ("apple", "banana", "cherry")
```

## Доступ к элементам кортежа

```python
# Доступ к элементам по индексу
print(fruits[0])  # Ожидаемый вывод: apple
print(fruits[1])  # Ожидаемый вывод: banana
```

## Операции с кортежами

```python
# Объединение кортежей
more_fruits = ("kiwi", "mango")
all_fruits = fruits + more_fruits
print(all_fruits)  # Ожидаемый вывод: ('apple', 'banana', 'cherry', 'kiwi', 'mango')

# Проверка наличия элемента
print("apple" in fruits)  # Ожидаемый вывод: True
print("banana" in fruits)  # Ожидаемый вывод: True
```