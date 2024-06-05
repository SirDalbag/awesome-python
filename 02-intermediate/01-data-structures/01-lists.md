# Списки

Списки — это упорядоченные изменяемые коллекции объектов в Python. Списки позволяют хранить элементы разных типов и изменять их в процессе выполнения программы.

## Создание списков

```python
# Создание пустого списка
empty_list = []

# Создание списка с элементами
fruits = ["apple", "banana", "cherry"]
```

## Доступ к элементам списка

```python
# Доступ к элементам по индексу
print(fruits[0])  # Ожидаемый вывод: apple
print(fruits[1])  # Ожидаемый вывод: banana
```

## Изменение элементов списка

```python
# Изменение элемента по индексу
fruits[1] = "blueberry"
print(fruits)  # Ожидаемый вывод: ['apple', 'blueberry', 'cherry']
```

## Добавление и удаление элементов

```python
# Добавление элемента в конец списка
fruits.append("orange")
print(fruits)  # Ожидаемый вывод: ['apple', 'blueberry', 'cherry', 'orange']

# Удаление элемента по значению
fruits.remove("blueberry")
print(fruits)  # Ожидаемый вывод: ['apple', 'cherry', 'orange']
```

## Операции со списками

```python
# Объединение списков
more_fruits = ["kiwi", "mango"]
all_fruits = fruits + more_fruits
print(all_fruits)  # Ожидаемый вывод: ['apple', 'cherry', 'orange', 'kiwi', 'mango']

# Проверка наличия элемента
print("apple" in fruits)  # Ожидаемый вывод: True
print("banana" in fruits)  # Ожидаемый вывод: False
```