# Пользовательские исключения в Python

Создание собственных исключений позволяет вам определить и обрабатывать специфические для вашего приложения ошибки. Это делает ваш код более читаемым и управляемым.

## Создание пользовательских исключений

Чтобы создать пользовательское исключение, необходимо создать новый класс, который наследует от встроенного класса `Exception` или одного из его подклассов.

```python
class MyCustomError(Exception):
    """Класс для представления пользовательской ошибки."""
    pass
```

## Использование пользовательских исключений

После создания пользовательского исключения его можно использовать так же, как и встроенные исключения.

```python
def do_something():
    raise MyCustomError("Произошла пользовательская ошибка")

try:
    do_something()
except MyCustomError as e:
    print(f"Обработано пользовательское исключение: {e}")
```

## Добавление атрибутов к пользовательским исключениям

Вы можете добавлять атрибуты к пользовательским исключениям для передачи дополнительной информации об ошибке.

```python
class MyCustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

try:
    raise MyCustomError("Произошла ошибка", 500)
except MyCustomError as e:
    print(f"Ошибка: {e}, Код: {e.code}")
```

## Наследование пользовательских исключений

Вы можете создавать иерархии пользовательских исключений, наследуясь от других пользовательских исключений.

```python
class ApplicationError(Exception):
    """Базовый класс для всех ошибок приложения."""
    pass

class DatabaseError(ApplicationError):
    """Класс для представления ошибок базы данных."""
    pass

class ValidationError(ApplicationError):
    """Класс для представления ошибок валидации."""
    pass

try:
    raise DatabaseError("Ошибка подключения к базе данных")
except ApplicationError as e:
    print(f"Обработано исключение приложения: {e}")
```

## Пример комплексного использования пользовательских исключений

```python
class InsufficientFundsError(Exception):
    """Исключение для случая недостатка средств на счете."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Недостаточно средств: баланс {balance}, попытка снять {amount}")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Пример использования
try:
    account = Account(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)  # Недостаточно средств: баланс 100, попытка снять 150
```