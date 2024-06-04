# Пакеты

Пакеты — это директории, содержащие несколько модулей, которые объединены по смыслу. Каждый пакет должен содержать файл `__init__.py`, который может быть пустым или содержать код инициализации пакета.

## Создание пакета

Создайте структуру директорий:

```bash
├── mypackage
│   ├── __init__.py
│   ├── modile2.py
│   ├── module2.py
```

### Пример файлов

```python
# mypackage/__init__.py
# Этот файл может быть пустым или содержать код инициализации

# mypackage/module1.py
def foo():
    return "foo from module1"

# mypackage/module2.py
def bar():
    return "bar from module2"
```

## Импортирование из пакета

Вы можете импортировать модули из пакета, используя точечную нотацию.

```python
# main.py
from mypackage import module1, module2

print(module1.foo())  # Ожидаемый вывод: foo from module1
print(module2.bar())  # Ожидаемый вывод: bar from module2
```

## Импортирование конкретных элементов из модуля пакета

Вы можете импортировать конкретные функции или переменные из модулей внутри пакета.

```python
# main.py
from mypackage.module1 import foo
from mypackage.module2 import bar

print(foo())  # Ожидаемый вывод: foo from module1
print(bar())  # Ожидаемый вывод: bar from module2
```

- [Использование стандартных библиотек](03-standard-libraries.md)