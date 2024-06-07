# Чтение файлов в Python

В Python чтение файлов является простой и мощной операцией.

## Открытие файла

Чтобы начать работу с файлом, сначала его нужно открыть с помощью функции open(). Она принимает имя файла и режим открытия.

```python
file = open('example.txt', 'r')
```

## Чтение всего содержимого файла

* `read()`: читает все содержимое файла как строку.

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## Чтение файла построчно

* `readline()`: читает одну строку файла за раз.

```python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # end='' чтобы избежать добавления двойного перевода строки
        line = file.readline()
```

* `readlines()`: читает все строки файла и возвращает их списком.

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
``` 

## Чтение файла с использованием цикла

Файл можно читать непосредственно в цикле `for`, что является простым и удобным способом.

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

## Чтение частей файла

Иногда нужно прочитать только часть файла. Метод `read(size)` позволяет это сделать, где `size` — количество символов для чтения.

```python
with open('example.txt', 'r') as file:
    content = file.read(10)  # Читает первые 10 символов файла
    print(content)
```

## Обработка ошибок при чтении файлов

При чтении файлов могут возникать ошибки, такие как отсутствие файла. Эти ошибки можно обрабатывать с помощью конструкции `try...except`.

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading file.")
```

## Пример комплексного чтения файла

```python
filename = 'example.txt'

try:
    with open(filename, 'r') as file:
        print("Чтение всего файла:")
        print(file.read())
        
    with open(filename, 'r') as file:
        print("\nЧтение построчно с помощью readline():")
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
    
    with open(filename, 'r') as file:
        print("\n\nЧтение построчно с помощью readlines():")
        lines = file.readlines()
        for line in lines:
            print(line, end='')
    
    with open(filename, 'r') as file:
        print("\n\nЧтение построчно в цикле for:")
        for line in file:
            print(line, end='')
    
    with open(filename, 'r') as file:
        print("\n\nЧтение части файла (первые 10 символов):")
        print(file.read(10))
        
except FileNotFoundError:
    print(f"Файл {filename} не найден.")
except IOError:
    print(f"Ошибка при чтении файла {filename}.")
```