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

## Методы списка

* `append(x)`: добавляет элемент `x` в конец списка.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Ожидаемый вывод: ['apple', 'banana', 'cherry']
```

* `extend(iterable)`: расширяет список, добавляя все элементы из переданного итерируемого объекта.

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "orange"])
print(fruits)  # Ожидаемый вывод: ['apple', 'banana', 'cherry', 'orange']
```

* `insert(i, x)`: вставляет элемент `x` на позицию `i`, а все последующие элементы сдвигаются вправо.

```python
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Ожидаемый вывод: ['apple', 'cherry', 'banana']
```

* `remove(x)`: удаляет первый элемент из списка, значение которого равно `x`, но если такого элемента нет, то возникает ошибка `ValueError`.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Ожидаемый вывод: ['apple', 'cherry']
```

* `pop([i])`: удаляет и возвращает элемент на позиции `i`, eсли индекс `i` не указан, удаляет и возвращает последний элемент списка.

```python
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Ожидаемый вывод: 'banana'
print(fruits)  # Ожидаемый вывод: ['apple', 'cherry']
```

* `clear()`: удаляет все элементы из списка, оставляя его пустым.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Ожидаемый вывод: []
```

* `index(x, start, end)`: возвращает индекс первого элемента, значение которого равно `x`, если элемент не найден, возникает ошибка `ValueError`. Параметры `start` и `end` указывают диапазон поиска.

```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Ожидаемый вывод: 1
```

* `count(x)`: возвращает количество элементов в списке, значение которых равно `x`.

```python
fruits = ["apple", "banana", "cherry", "apple"]
count = fruits.count("apple")
print(count)  # Ожидаемый вывод: 2
```

* `sort(key=None, reverse=False)`: сортирует элементы списка на месте. Аргумент `key` — это функция, которая будет вызвана для каждого элемента списка перед сравнением. Аргумент `reverse` определяет порядок сортировки (по умолчанию — по возрастанию).

```python
fruits = ["cherry", "banana", "apple"]
fruits.sort()
print(fruits)  # Ожидаемый вывод: ['apple', 'banana', 'cherry']
```

```python
fruits.sort(reverse=True)
print(fruits)  # Ожидаемый вывод: ['cherry', 'banana', 'apple']
```

```python
fruits.sort(key=len)
print(fruits)  # Ожидаемый вывод: ['apple', 'cherry', 'banana']
```

* `reverse()`: переворачивает элементы списка на месте.

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Ожидаемый вывод: ['cherry', 'banana', 'apple']
```

* `copy()`: возвращает поверхностную копию списка.

```python
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # Ожидаемый вывод: ['apple', 'banana', 'cherry']
```