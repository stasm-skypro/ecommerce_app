## Домашняя работа к модулю 4

## Проект E-commerce

### (17.1. Исключения)

### Решаемые задачи

На данном этапе работы готовим ядро интернет-магазина.

-- Версия 2024.10.29 --

### Задание 1

Если пользователь создает товар (метод __init__) с нулевым количеством, вызывается исключение ValueError, которое
выдаёт сообщение: <code>Товар с нулевым количеством не может быть добавлен</code>. При этом выполнение программы
прерывается.

### Задание 2

В классе <code>Category</code> реализован новый метод, который подсчитывает средний ценник всех товаров. С помощью
исключений обработан случай, когда в категории нет товаров и сумма всех товаров будет делиться на ноль. Если такое
происходит, программа возвращает ноль.

Например:

<code>print("Проверка метода подсчёта средней цены всех товаров в категории")</code>

<code>print("Средняя цена для категории {} = {}".format(category0, category0.get_average_product_price()))</code>

<code>print("Средняя цена для категории {} = {}".format(category1, category1.get_average_product_price()))</code>

<code>print("Средняя цена для категории {} = {}".format(category2, category2.get_average_product_price()))</code>

### Задание 3

Для новой функциональности написаны тесты. При этом тесты, которые были написаны ранее, выполняются без ошибок.

### Дополнительное задание

* Создан класс исключения, который отвечает за обработку событий, когда в «Категорию» или «Заказ» добавляется товар с
  нулевым количеством. При добавлении товара с нулевым количеством вызывается исключение и выводится соответствующее
  сообщение. В случае успешного добавления товара выводится сообщение о том, что товар добавлен. И также при любом
  исходе выводится сообщение, что обработка добавления товара завершена.

**В прошлом ДЗ была поставлена задача модифицировать метод добавления товара add_product класса Category таким образом,
чтобы не добавлялись товары с нулевой или отрицательной ценой. При не было учтено, что через конструктор можно было
добавлять товары с любой ценой. Эта ошибка устранена.**

### Пример работы функции main

Клонируем репозиторий:

        git clone ssh://git@github.com:stasm-skypro/ecommerce_app.git

Переходим в папку с проектом, устанавливаем необходимые зависимости через poetry, используя файл pyproject.toml.
Находим модуль **main17_1.py** и запускаем его.
Модули **main16_2.py**, **main16_1.py**, **main15.1**, **main14_2.py** и **main14_1.py** также работают.

### Документация и ссылки.

Полное описание задания и ТЗ к функциям находятся
по [ссылке](https://my.sky.pro/student-cabinet/stream-lesson/135695/homework-requirements).

### Лицензия.

Скрипты из данного модуля распространяются в познавательных целях, интеллектуальной ценности не имеют и предназначены
для свободного копирования кем угодно.
