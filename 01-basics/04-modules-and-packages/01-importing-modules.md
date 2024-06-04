# Модули

Модули в Python — это файлы с расширением `.py`, содержащие код Python. Модули позволяют организовать код и использовать его повторно в разных частях программы.

## Создание модуля

Создайте файл с расширением `.py`, например, `mymodule.py`, и добавьте в него функции или переменные.

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

## Импортирование модуля

Вы можете импортировать модуль в другой файл с помощью ключевого слова `import`.

```python
# main.py
import mymodule

message = mymodule.greet("Alice")
print(message)  # Ожидаемый вывод: Hello, Alice!
```

## Импортирование конкретных элементов модуля

Вы можете импортировать конкретные функции или переменные из модуля.

```python
# main.py
from mymodule import greet

message = greet("Bob")
print(message)  # Ожидаемый вывод: Hello, Bob!
```

## Импортирование с псевдонимом

Вы можете использовать псевдонимы для импортируемых модулей или функций, чтобы упростить код.

```python
# main.py
import mymodule as mm

message = mm.greet("Charlie")
print(message)  # Ожидаемый вывод: Hello, Charlie!
```