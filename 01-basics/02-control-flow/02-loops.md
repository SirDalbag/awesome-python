# Циклы

Циклы позволяют выполнять блок кода несколько раз. В Python для этого используются конструкции `for` и `while`.

## Цикл for

Цикл `for` используется для итерации по последовательности (например, списку, кортежу, строке или диапазону чисел).

```python
# Итерация по списку
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Итерация по диапазону чисел
for i in range(5): # range(start, stop, step)
    print(i)
```

## Цикл while

Цикл `while` выполняет блок кода до тех пор, пока условие истинно.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Вложенные циклы

Циклы могут быть вложены друг в друга для выполнения более сложных итераций.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

## Операторы break и continue

* Оператор `break` используется для выхода из цикла досрочно.
* Оператор `continue` пропускает оставшуюся часть кода в текущей итерации и переходит к следующей итерации.

```python
# Пример использования break
for i in range(10):
    if i == 5:
        break
    print(i)

# Пример использования continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

## Цикл for с else

Цикл `for` может иметь необязательный блок `else`, который выполняется, если цикл завершился без вызова оператора `break`.

```python
for i in range(5):
    print(i)
else:
    print("Цикл завершился без вызова break")
```