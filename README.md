## Домашняя работа к модулю 4
## Проект E-commerce
### (15.1 Магические методы)
### Решаемые задачи
На данном этапе работы готовим ядро интернет-магазина.

-- Версия 24.10.16 --

### 1.
Для класса Product добавлено строковое отображение в следующем виде:

<code>Название продукта, 80 руб. Остаток: 15 шт.</code>

В геттере для класса Category для вывода списка товаров, теперь каждый продукт имеет реализованное строковое 
отображение. Работа геттера оптимизирована - объект продукта преобразовывается в строку.

<code>Название категории, количество продуктов: 200 шт.</code>

### 2.
Для удобства работы с продуктами реализована возможность их складывать. Логика сложения должна работает так, что 
в итоге получается полная стоимость всех товаров на складе.

<code>Например, для товара a с ценой 100 рублей и количеством на складе 10 и товара b с ценой 200 рублей и количеством 
на складе 2 результатом выполнения операции a + b должно стать значение, полученное из 100 × 10 + 200 × 2 = 1400.</code>

### 3.
Для новой функциональности написаны тесты. При этом тесты, которые были написаны ранее, выполняются без 
ошибок.

### _Дополнительно_
_Создан новый вспомогательный класс ProductIterator, с помощью которого можно перебирать товары одной категории, 
например в цикле for. Новый класс принимает на вход объект класса категории и производит итерацию по товарам, которые 
хранятся в данной категории. То есть метод выполнения следующего шага итерации должен возвращает очередной товар 
категории._


### Пример работы функции main
Клонируем репозиторий:

        git clone ssh://git@github.com:stasm-skypro/ecommerce_app.git


Переходим в папку с проектом, устанавливаем необходимые зависимости через poetry, используя файл pyproject.toml.
Находим модуль **main15_1.py** и запускаем его.
Модули **main14_2.py** и **main14_1.py** также работают.

### Документация и ссылки.
Полное описание задания и ТЗ к функциям находятся по [ссылке](https://my.sky.pro/student-cabinet/stream-lesson/135691/homework-requirements).

### Лицензия.
Скрипты из данного модуля распространяются в познавательных целях, интеллектуальной ценности не имеют и предназначены для свободного копирования кем угодно.
