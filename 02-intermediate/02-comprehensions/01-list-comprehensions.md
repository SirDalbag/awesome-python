# List Comprehensions

Включения списков позволяют создавать новые списки, применяя выражение к каждому элементу итерируемого объекта.

```python
[выражение for элемент in итерируемый if условие]
```

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

# Set Comprehensions

Похожи на list comprehensions, но возвращают множество, что гарантирует уникальность элементов.

```python
{выражение for элемент in итерируемый if условие}
```

```python
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

## Применение с условиями

Включения также могут включать условные выражения, что делает их еще более мощными.

```python
# Cписок, где 'small' если число < 3, иначе 'large'
sizes = ["small" if x < 3 else "large" for x in range(5)]
print(sizes)  # ['small', 'small', 'small', 'large', 'large']
```