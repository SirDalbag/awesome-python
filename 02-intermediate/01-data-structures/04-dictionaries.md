# Словари

Словари — это неупорядоченные коллекции пар ключ-значение в Python. Словари позволяют быстро искать значения по ключам и предоставляют гибкость для хранения различных типов данных.

## Создание словарей

```python
# Создание пустого словаря
empty_dict = {}

# Создание словаря с элементами
person = {"name": "Alice", "age": 30, "city": "New York"}
```

## Доступ к значениям словаря

```python
# Доступ к значениям по ключам
print(person["name"])  # Ожидаемый вывод: Alice
print(person["age"])  # Ожидаемый вывод: 30
```

## Изменение и добавление элементов

```python
# Изменение значения по ключу
person["age"] = 31
print(person)  # Ожидаемый вывод: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Добавление нового элемента
person["email"] = "alice@example.com"
print(person)  # Ожидаемый вывод: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
```

## Удаление элементов

```python
# Удаление элемента по ключу
del person["city"]
print(person)  # Ожидаемый вывод: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
```

## Операции со словарями

```python
# Получение всех ключей
keys = person.keys()
print(keys)  # Ожидаемый вывод: dict_keys(['name', 'age', 'email'])

# Получение всех значений
values = person.values()
print(values)  # Ожидаемый вывод: dict_values(['Alice', 31, 'alice@example.com'])
```