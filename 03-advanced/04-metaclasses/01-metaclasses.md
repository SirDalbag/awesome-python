# Метаклассы в Python

Метаклассы в Python — это "классы для классов". Они позволяют управлять созданием и поведением классов. Метаклассы могут изменять процесс создания классов, добавлять дополнительные методы или свойства, а также выполнять проверки и модификации.

## Основы метаклассов

В Python всё является объектом, включая классы. Классы создаются с помощью метаклассов. Стандартный метакласс — это `type`.

```python
class MyClass:
    pass

# Проверка метакласса
print(type(MyClass))  # <class 'type'>
```

## Создание метаклассов

Метаклассы создаются путем наследования от `type` и переопределения специальных методов, таких как `__new__` и `__init__`.

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Создание класса {name}")
        return super().__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        print(f"Инициализация класса {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
```

## Переопределение `__new__` и `__init__` в метаклассах

* `__new__`: используется для создания нового класса. Он вызывается перед `__init__`.
* `__init__`: используется для инициализации класса после его создания.

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['class_name'] = name
        return super().__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        cls.created = True
        super().__init__(name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.class_name)  # MyClass
print(MyClass.created)     # True
```

## Использование метаклассов

1) **Валидация классов**: Проверка наличия обязательных методов или свойств.
2) **Автоматическое добавление методов или свойств**: Динамическое добавление функциональности к классам.
3) **Реализация шаблонов проектирования**: Внедрение определенных паттернов на уровне классов.

### Пример валидации классов:

```python
class InterfaceMeta(type):
    def __new__(cls, name, bases, dct):
        if 'my_method' not in dct:
            raise TypeError(f"Класс {name} должен реализовать метод 'my_method'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InterfaceMeta):
    def my_method(self):
        pass

class AnotherClass(metaclass=InterfaceMeta):
    pass  # Ошибка: TypeError: Класс AnotherClass должен реализовать метод 'my_method'
```

## Пример комплексного использования метаклассов

```python
class AutoMethodMeta(type):
    def __new__(cls, name, bases, dct):
        dct['auto_method'] = lambda self: f"Метод добавлен автоматически в {name}"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AutoMethodMeta):
    pass

obj = MyClass()
print(obj.auto_method())  # Метод добавлен автоматически в MyClass
```