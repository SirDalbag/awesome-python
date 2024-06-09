# Менеджеры контекста в Python

Менеджеры контекста в Python предоставляют удобный способ управления ресурсами, такими как файлы, сетевые соединения и блокировки. Они обеспечивают автоматическое выполнение кода для настройки и освобождения ресурсов.

## Основы менеджеров контекста

Менеджеры контекста используются с инструкцией `with`, которая гарантирует, что специальные методы менеджера контекста будут вызваны в начале и в конце блока кода.

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
```

## Специальные методы `__enter__` и `__exit__`

```python
class MyContextManager:
    def __enter__(self):
        print("Начало контекста")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Конец контекста")

with MyContextManager():
    print("Внутри блока контекста")
```

## Обработка исключений в менеджерах контекста

Метод `__exit__` принимает три аргумента: тип исключения, значение исключения и трассировку. Это позволяет вам обрабатывать исключения внутри менеджера контекста.

```python
class MyContextManager:
    def __enter__(self):
        print("Начало контекста")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Произошло исключение: {exc_value}")
        print("Конец контекста")
        return True  # Подавление исключения

with MyContextManager():
    print("Внутри блока контекста")
    raise ValueError("Ошибка внутри контекста")
```

## Менеджеры контекста с библиотекой `contextlib`

Библиотека `contextlib` предоставляет утилиты для упрощения создания менеджеров контекста, включая декораторы и функции.

* `contextlib.contextmanager`: Этот декоратор позволяет создавать менеджеры контекста с использованием генераторов.

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Начало контекста")
    yield
    print("Конец контекста")

with my_context():
    print("Внутри блока контекста")
```

* `contextlib.closing`: Этот менеджер контекста автоматически закрывает объект после завершения блока `with`.

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://example.com')) as page:
    for line in page:
        print(line)
```

## Пример комплексного использования менеджеров контекста

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(resource):
    try:
        resource.open()
        yield resource
    finally:
        resource.close()

class Resource:
    def open(self):
        print("Ресурс открыт")
    
    def close(self):
        print("Ресурс закрыт")

resource = Resource()

with managed_resource(resource):
    print("Работа с ресурсом")
```