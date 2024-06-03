# Лямбда-функции

Лямбда-функции — это анонимные функции, которые определяются с помощью ключевого слова `lambda`.

## Пример лямбда-функции

```python
add = lambda a, b: a + b
print(add(3, 5))  # Ожидаемый вывод: 8
```

## Лямбда-функции в качестве аргументов

Лямбда-функции часто используются в качестве аргументов для других функций, таких как `map`, `filter` и `sorted`.

* Использование с функцией `map`

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Ожидаемый вывод: [1, 4, 9, 16]
```

* Использование с функцией `filter`

```python
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Ожидаемый вывод: [2, 4]
```

* Использование с функцией `sorted`

```python
points = [(1, 2), (3, 1), (5, 4)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Ожидаемый вывод: [(3, 1), (1, 2), (5, 4)]
```

