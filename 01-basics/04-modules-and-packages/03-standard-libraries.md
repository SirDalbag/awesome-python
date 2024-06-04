# Использование стандартных библиотек

Python поставляется с множеством стандартных библиотек, которые предоставляют множество полезных функций и модулей. 
Вы можете использовать эти библиотеки, чтобы избежать написания кода с нуля для распространенных задач.

## Примеры использования стандартных библиотек

### Модуль math

Модуль `math` предоставляет математические функции.

```python
import math

print(math.sqrt(16))  # Ожидаемый вывод: 4.0
print(math.factorial(5))  # Ожидаемый вывод: 120
```

### Модуль datetime

Модуль `datetime` предоставляет функции для работы с датами и временем.

```python
import datetime

now = datetime.datetime.now()
print(now)  # Ожидаемый вывод: текущая дата и время

new_year = datetime.datetime(2024, 1, 1)
print(new_year)  # Ожидаемый вывод: 2024-01-01 00:00:00
```

### Модуль os

Модуль `os` предоставляет функции для взаимодействия с операционной системой.

```python
import os

print(os.name)  # Ожидаемый вывод: имя операционной системы (например, 'user')
print(os.getcwd())  # Ожидаемый вывод: текущий рабочий каталог
```

### Модуль json

Модуль `json` используется для работы с данными в формате `JSON (JavaScript Object Notation)`.

```python
import json

# Преобразование Python объекта в JSON строку
data = {'name': 'Alice', 'age': 30}
json_data = json.dumps(data)
print(json_data)  # Ожидаемый вывод: {"name": "Alice", "age": 30}

# Преобразование JSON строки в Python объект
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
print(data)  # Ожидаемый вывод: {'name': 'Bob', 'age': 25}
```

### Модуль random

Модуль `random` предоставляет функции для генерации случайных чисел.

```python
import random

# Генерация случайного числа от 1 до 10
print(random.randint(1, 10))

# Генерация случайного числа с плавающей точкой от 0 до 1
print(random.random())

# Выбор случайного элемента из списка
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))
```

### Модуль re

Модуль `re` предоставляет функции для работы с регулярными выражениями.

```python
import re

# Поиск всех вхождений шаблона в строке
pattern = r'\d+'
string = 'There are 123 apples and 45 bananas'
matches = re.findall(pattern, string)
print(matches)  # Ожидаемый вывод: ['123', '45']

# Замена всех вхождений шаблона в строке
new_string = re.sub(r'\d+', 'many', string)
print(new_string)  # Ожидаемый вывод: There are many apples and many bananas
```

### Модуль collections

Модуль `collections` предоставляет специализированные контейнерные типы данных, такие как `Counter`, `deque`, `defaultdict`, `OrderedDict`, и `namedtuple`.

```python
from collections import Counter

# Подсчет частоты элементов в списке
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
counter = Counter(fruits)
print(counter)  # Ожидаемый вывод: Counter({'banana': 3, 'apple': 2, 'cherry': 1})
```

### Модуль itertools

Модуль `itertools` предоставляет функции для создания итераторов для эффективного перебора данных.

```python
import itertools

# Создание декартова произведения
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']
product = list(itertools.product(colors, sizes))
print(product) # Ожидаемый вывод: [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```