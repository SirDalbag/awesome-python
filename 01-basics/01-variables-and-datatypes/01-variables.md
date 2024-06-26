# Переменные

Переменные в Python используются для хранения данных. Имя переменной должно быть уникальным и начинаться с буквы или символа подчеркивания.

```python
# Присваивание переменных
variable = "Hello, World!"

# Вывод переменных
print(variable)  # Hello, World!
```

### Правила именования переменных

1) Имена переменных могут содержать только буквы, цифры и символы подчеркивания.
2) Имена переменных должны начинаться с буквы (a-z, A-Z) или символа подчеркивания (_).
3) Имена переменных чувствительны к регистру (например, `myVar` и `myvar` — это разные переменные).
4) Имена переменных не могут быть ключевыми словами Python (например, `if`, `else`, `for` и т.д.).

```python
# Допустимые имена переменных
my_variable = "OK"
_variable = "OK"
variable1 = "OK"

# Недопустимые имена переменных
1variable = "ERROR"
my-variable = "ERROR"
```

### Типы переменных

Переменные в Python могут хранить данные различных типов, таких как целые числа, строки, числа с плавающей запятой и т.д. 
Тип переменной определяется автоматически при присваивании значения.

```python
a = 10 # <class 'int'>
b = 3.14 # <class 'float'>
c = "Python" # <class 'str'>
```

### Изменение значений переменных

Значение переменной можно изменить в любое время.

```python
x = 10 # <class 'int'>
x = 3.14 # <class 'float'>
x = "Python" # <class 'str'>
```

### Множественное присваивание

В Python можно присваивать значения нескольким переменным одновременно.

```python
a, b, c = 1, 2, 3
x = y = z = "Python"
```

### Константы

Константы — это переменные, значения которых не изменяются в ходе выполнения программы. 
В Python принято обозначать константы заглавными буквами.

```python
PI = 3.14159
```