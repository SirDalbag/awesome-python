# Dictionary Comprehensions

```python
{ключ: значение for переменная in итерируемый if условие}
```

```python
squares_dict = {x: x**2 for x in range(6)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```