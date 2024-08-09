---
type:
  - сценарий
alliases: День №22. Python практикум. С нуля до автоматизатора
project: "[[Курс. Python практикум. С нуля до автоматизатора]]"
tags:
  - курс
  - пайтон
  - python
  - складчик
  - сценарий
topics: 
no: 22
is_done:
---
# 22.1 Извлечение текста из элементов
- Использование метода `text` для извлечения текста из элементов.
  - Пример: `element.text`.
  - Извлечение текста из различных типов элементов:
    - Заголовки (например, `<h1>`, `<h2>`)
    - Параграфы (`<p>`)
    - Ссылки (`<a>`)
    - Списки (`<ul>`, `<ol>`)
    - И другие текстовые элементы.

# 22.2 Извлечение атрибутов элементов
- Использование метода `get_attribute()` для извлечения значений атрибутов элементов.
  - Пример: `element.get_attribute('attribute_name')`.
  - Извлечение значений различных атрибутов:
    - "href" для ссылок
    - "src" для изображений
    - "title" 
    - "class" для классов стилей
    - "id" для идентификаторов
    - И других атрибутов.

# 22.3 Работа с таблицами
- Извлечение данных из таблиц на веб-странице.
  - Поиск таблицы с помощью метода `find_element()`.
  - Извлечение содержимого ячеек, строк и столбцов таблицы с использованием методов поиска элементов и методов для работы с коллекциями элементов.
  - Примеры извлечения данных из таблиц.

# 22.1 Извлечение текста из элементов 📝

## 2. Как работает метод `.text`? 🤔

Метод `.text` позволяет получить текстовое содержимое HTML-элементов на странице. Для этого нужно вызвать метод у объекта, представляющего элемент, текст которого необходимо извлечь. Обычно результатом будет строка, содержащая текст элемента. Встроенный метод `.text` доступен в следующих библиотеках:
* Beautiful Soup для Python 🐍
* jQuery для JavaScript ⚡️
  
### Пример использования метода `text` с Beautiful Soup:

```python
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>This is a title</title>
    </head>
    <body>
        <h1>Welcome to the website</h1>
        <p>Here is some example text!</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)  # Выводит: Welcome to the website
print(soup.p.text)   # Выводит: Here is some example text!
```

### Пример использования метода `text` с jQuery:

```javascript
const heading = $("h1").text(); // Возвращается текст "Welcome to the website"
const paragraph = $("p").text(); // Возвращается текст "Here is some example text!"
```

## 3. Извлечение текстов из различных типов элементов 💬

### 3.1 Заголовки (`<h1>`, `<h2>` и т. д.)

Текст из заголовков может быть извлечен как и из любых других текстовых элементов с помощью метода `.text`. Заголовки играют важную роль в SEO, возможность их анализа часто используется веб-скрейперами и аналитикой контента.

```python
header = soup.find("h1")
print(header.text)  # Выводит: Welcome to the website
```

### 3.2 Параграфы (`<p>`)

Если вам нужно получить контент из параграфов веб-страницы, вы также можете использовать `.text` для извлечения текста.

```python
paragraph = soup.find("p")
print(paragraph.text)  # Выводит: Here is some example text!
```

### 3.3 Ссылки (`<a>`)

Текст ссылок можно также распарсить с помощью метода `.text`.

```python
html = """
<html>
    <body>
        <a href="https://example.com">This is a link</a>
    </.body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

link = soup.find("a")
print(link.text)  # Выводит: This is a link
```

### 3.4 Списки (`<ul>`, `<ol>`)

Текст в пунктах списка также можно извлечь с помощью метода `text`. Вам может пригодиться проход по списку и выбор каждого элемента списка.

```python
html = """
<html>
    <body>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
list_items = soup.find_all("li")  # Извлекаем всех элементы из списка

for item in list_items:
    print(item.text)  
# Выводит:
# Item 1
# Item 2
# Item 3
```

### 3.5 Другие текстовые элементы 📖

Точно так же метод `.text` может извлекать текст из любых других элементов, содержащих текст. Пример:

```python
html = """
<html>
    <body>
        <button>Click me!</button>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

button = soup.find("button")
print(button.text)  # Выводит: Click me!
```

В заключение, метод `.text` – полезный держатель при извлечении данных из текстовых частей HTML-страницы. Безусловно, он может.schedulersзку при разветомится во многих виде.
# 22.2 Извлечение атрибутов элементов 🎯

Иногда при работе с веб-страницами необходимо получить значения определённых атрибутов элементов. В этой статье мы рассмотрим, как извлечь атрибуты элементов с помощью Python и библиотеки Selenium.

## Использование метода `get_attribute()` 🔍

Для того чтобы получить значение атрибута элемента, можно использовать метод `get_attribute()`. Этот метод принимает один аргумент - имя атрибута, значение которого хотим получить. Результатом будет при вызове этой функции будет значение данного атрибута элемента.

Пример использования:

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.example.com")

element = driver.find_element_by_tag_name("a")
attribute_value = element.get_attribute("attribute_name")

print(attribute_value)
```

В данном примере мы открываем страницу и ищем элемент с тегом `<a>`, после чего извлекаем значение атрибута.

## Различные атрибуты элементов 📋

### Извлечение ссылок (href) 🔗

Допустим, для элемента-ссылки нужно получить атрибут `href`. Пример:

```python
element = driver.find_element_by_tag_name("a")
href_value = element.get_attribute("href")

print(href_value)
```

### Извлечение ссылок на изображения (src) 🖼️

Для получения ссылки на изображение можно воспользоваться атрибутом `src`. Пример:

```python
element = driver.find_element_by_tag_name("img")
src_value = element.get_attribute("src")

print(src_value)
```

### Извлечение заголовков элементов (title) 📰

Иногда нужно получить заголовок элемента, заданный атрибутом `title`. Пример:

```python
element = driver.find_element_by_tag_name("whatever")
title_value = element.get_attribute("title")

print(title_value)
```

### Извлечение значений класса для стилей (class) 🎨

Для работы со стилями элементов важно получить информацию о классах. Для этого используется атрибут `class`. Пример:

```python
element = driver.find_element_by_tag_name("whatever")
class_value = element.get_attribute("class")

print(class_value)
```

### Извлечение идентификаторов элементов (id) 🔑

Иногда элементы имеют уникальные идентификаторы, которые задаются атрибутом `id`. Их можно получить следующим образом:

```python
element = driver.find_element_by_tag_name("whatever")
id_value = element.get_attribute("id")

print(id_value)
```

## Заключение 😊

Теперь вы знаете, как извлечь значения различных атрибутов элементов с использованием Python и библиотеки Selenium. Это особенно полезно при написании скриптов для автоматизации и взаимодействия с веб-страницами. Так что наслаждайтесь обработкой данных и извлекайте атрибуты! 🌟
# 22.3 Работа с таблицами на веб-странице 📊

## 2. Поиск таблицы с помощью метода `find_element()` 🎯

Для получения доступа к таблице на веб-странице необходимо использовать метод `find_element()` библиотеки Selenium, эффективно выбрав элемент таблицы, соответствующий тегу `<table>`.

Пример кода:

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://example.com/somepage-with-table')

table = driver.find_element_by_tag_name('table')
```

## 3. Извлечение содержимого ячеек, строк и столбцов таблицы🔍

### 3.1. Извлечение строк таблицы 📝

Для извлечения строк таблицы, используйте метод `find_elements_by_tag_name()`. Обратите внимание, что осуществляется поиск _элементов_ (во множественном числе), а не _элемента_ (в единственном числе).

Пример кода:

```python
rows = table.find_elements_by_tag_name('tr')
```

### 3.2. Извлечение столбцов таблицы📊

Для извлечения столбцов таблицы, выполните перебор ячеек выбранных строк таблицы с помощью метода `find_elements_by_tag_name()`. Заметьте, что здесь также поиск выполняется по всем элементам с указанным тегом (в нашем случае - `<td>`).

Пример кода:

```python
for row in rows:
    columns = row.find_elements_by_tag_name('td')
```
 
### 3.3. Извлечение содержимого ячейки таблицы 💾

Для получения содержимого ячейки таблицы используйте метод `text`:

Пример кода:

```python
cell_content = columns[0].text
```

## 4. Примеры извлечения данных из таблиц 📚

Допустим, у нас есть следующая таблица на веб-странице:

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>25</td>
  </tr>
</table>
```

### 4.1. Извлечение имён и возраста всех людей 👩👨

```python
data = []

for row in rows[1:]:  # Пропускаем первую строку с заголовками
    columns = row.find_elements_by_tag_name('td')
    
    name = columns[0].text
    age = int(columns[1].text)
    
    data.append((name, age))

print(data)
```

Вывод:

```
[('Alice', 30), ('Bob', 25)]
```

### 4.2. Извлечение имени самого старшего человека 👵

```python
max_age = -1
oldest_person = ""

for row in rows[1:]:
    columns = row.find_elements_by_tag_name('td')
    
    name = columns[0].text
    age = int(columns[1].text)
    
    if age > max_age:
        max_age = age
        oldest_person = name

print(oldest_person)
```

Вывод:

```
"Alice"
```

Теперь вы можете извлекать данные из таблиц на веб-странице с помощью Python и Selenium. Это полезный навык при разработке веб-скраперов и автоматизации рутинных задач. 🤖