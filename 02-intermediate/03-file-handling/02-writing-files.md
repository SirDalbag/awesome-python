# Запись файлов в Python

Запись файлов в Python — это важный аспект работы с данными, который позволяет сохранять информацию в текстовые и двоичные файлы.

## Открытие файла для записи

Для записи данных в файл используется функция `open()`, принимающая имя файла и режим открытия. Режимы записи включают:

* `'w'`: запись (удаляет содержимое файла, если он существует, или создает новый файл).
* `'a'`: добавление (добавляет данные в конец файла).
* `'x'`: создание нового файла (если файл уже существует, возникает ошибка).

## Запись строк в файл

* `write()`: записывает строку в файл.

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
```

## Запись нескольких строк

* `writelines()`: записывает список строк в файл.

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

## Добавление данных в файл

Используйте режим `'a'` для добавления данных в конец файла.

```python
with open('example.txt', 'a') as file:
    file.write("Appending a new line.\n")
```

## Запись двоичных данных

Для записи двоичных данных используйте режим `'wb'`.

```python
data = bytes([104, 101, 108, 108, 111])  # 'hello' в байтах
with open('example.bin', 'wb') as file:
    file.write(data)
```

## Обработка ошибок при записи файлов

Важно обрабатывать возможные ошибки при записи файлов с помощью конструкции `try...except`.

```python
try:
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\n")
except IOError:
    print("Error writing to file.")
```