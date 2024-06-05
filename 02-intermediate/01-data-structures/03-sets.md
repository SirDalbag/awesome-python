# Множества

Множества — это неупорядоченные коллекции уникальных элементов в Python. Множества позволяют хранить только уникальные элементы и предоставляют быстрые операции по проверке принадлежности и выполнению математических операций, таких как объединение, пересечение и разность.

## Создание множеств

```python
# Создание пустого множества
empty_set = set()

# Создание множества с элементами
fruits = {"apple", "banana", "cherry"}
```

## Добавление и удаление элементов

```python
# Добавление элемента
fruits.add("orange")
print(fruits)  # Ожидаемый вывод: {'apple', 'banana', 'cherry', 'orange'}

# Удаление элемента
fruits.remove("banana")
print(fruits)  # Ожидаемый вывод: {'apple', 'cherry', 'orange'}
```

## Операции с множествами

```python
# Объединение множеств
more_fruits = {"kiwi", "mango"}
all_fruits = fruits | more_fruits
print(all_fruits)  # Ожидаемый вывод: {'apple', 'cherry', 'orange', 'kiwi', 'mango'}

# Пересечение множеств
common_fruits = fruits & more_fruits
print(common_fruits)  # Ожидаемый вывод: set()

# Разность множеств
unique_fruits = fruits - more_fruits
print(unique_fruits)  # Ожидаемый вывод: {'apple', 'cherry', 'orange'}
```