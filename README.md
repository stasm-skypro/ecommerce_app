## Домашняя работа к модулю 4
## Проект E-commerce
### (15.1 Магические методы)
### Решаемые задачи
На данном этапе работы готовим ядро интернет-магазина.

### 1.
Для класса Product добавить строковое отображение в следующем виде:
Название продукта, 80 руб. Остаток: 15 шт.
В предыдущей домашке вы делали геттер для класса Category для вывода списка товаров, теперь каждый продукт имеет 
реализованное строковое отображение. Вы можете вернуться к этому геттеру и оптимизировать его работу, просто 
преобразовав объект продукта в строку.

<code>Название категории, количество продуктов: 200 шт.</code>

### 2.
Для удобства работы с продуктами реализовать возможность их складывать. Логика сложения должна работать так, чтобы 
в итоге у вас получалась полная стоимость всех товаров на складе.

<code>Например, для товара a с ценой 100 рублей и количеством на складе 10 и товара b с ценой 200 рублей и количеством 
на складе 2 результатом выполнения операции a + b должно стать значение, полученное из 100 × 10 + 200 × 2 = 1400.</code>

### 3.
Напишите тесты для новой функциональности. При этом убедитесь что тесты, которые были написаны ранее, выполняются без 
ошибок.

###_Дополнительное задание
Создайте новый вспомогательный класс, с помощью которого можно перебирать товары одной категории, например в цикле for. 
Для этого новый класс должен принимать на вход объект класса категории и производить итерацию по товарам, которые 
хранятся в данной категории. То есть метод выполнения следующего шага итерации должен возвращать очередной товар 
категории._


### Пример работы функции main
Клонируем репозиторий:

        git@github.com:stasm-skypro/sky-pro-ecommerce_app.git


Переходим в папку с проектом, устанавливаем необходимые зависимости через poetry, используя файл pyproject.toml.
Находим модуль **main14_2.py** и запускаем его.

### Документация и ссылки.
Полное описание задания и ТЗ к функциям находятся по [ссылке](https://my.sky.pro/student-cabinet/stream-lesson/135689/homework-requirements).

### Лицензия.
Скрипты из данного модуля распространяются в познавательных целях, интеллектуальной ценности не имеют и предназначены для свободного копирования кем угодно.
