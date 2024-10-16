import re
from typing import Self, Any

from src.category import Category


class Product:
    """Класс для создания экземпляров товаров."""

    name: str
    description: str
    __price: float
    quantity: int
    total_price: float

    def __init__(self, name: str, description: str, price: float, quantity: int, total_price: float = 0) -> None:
        """Конструктор класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self: Self) -> str:
        """Строковое представление экземпляра класса."""
        # Название продукта, 80 руб. Остаток: 15 шт.
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self: Self, other) -> float | Any:
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, params: dict, category: Category):
        """Метод добавляет новый продукт категорию category."""
        new_product = Product(**params)

        for product in category.products:
            if new_product.name in product:
                new_product.price = max(new_product.price, float(product.split(", ")[1].split()[0]))
                new_product.quantity += int(product.split(" ")[-2])
                category.product_count += 1

        return new_product

    # Геттер для цены продукта
    @property
    def price(self) -> float:
        """Метод возвращает цену продукта"""
        return self.__price

    #  Сеттер для цены продукта
    @price.setter
    def price(self, price: float) -> None:
        """Метод устанавливает цену продукта."""
        # Если цена меньше или равна 0, то выводим предупреждение.
        if price <= 0:
            print(f"Вы ввели цену {price}.")
            print("Цена не должна быть нулевая или отрицательная.")
        # Иначе
        else:
            # Если новая цена больше прежней, автоматически принимаем новую цену.
            if price > self.__price:
                self.__price = price
                print(f"Новая цена продукта - {self.__price}.")
            elif price == self.__price:
                print(f"Цена продукта не изменилась - {self.__price}.")
            # Если новая цена меньше, чем уже имеющаяся цена для данного продукта,
            else:
                print(f"Внимание! Введённая цена {price} меньше, чем уже имеющаяся цена для данного продукта!")
                # спрашиваем подтверждение пользователя на ввод меньшей цены и вносим изменения.
                if re.match(input("Подтвердите ввод новой цены? (yes/no) >>> %: "), "yes"):
                    self.__price = price
                    print(f"Новая цена продукта - {self.__price}.")
                # Иначе оставляем прежнюю цену.
                else:
                    print(f"Цена продукта не изменилась - {self.__price}.")


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("Инициализация продукта 1")
    product1 = Product("Молоко", "Молоко коровье 3%", 500.00, 5)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print()

    print("Инициализация продукта 2")
    product2 = Product("Хлеб", "Хлеб белый стандартный", 100.0, 3)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    print()

    print("Инициализация продукта 3")
    product3 = Product("Яйца", "Яйца 1С", 500.0, 2)
    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    print()

    print("Инициализация продукта 4")
    product4 = Product("Шорты", "Шорты мужские, размер 50", 5000.0, 2)
    print(product4.name)
    print(product4.description)
    print(product4.price)
    print(product4.quantity)

    print("Инициализация категории 1 с продуктами 1, 2, 3")
    category1 = Category(
        "Продукты",
        "Продукты первой необходимости",
        [product1, product2, product3],
    )
    print()

    print("Проверка работы метода new_product")
    product31 = Product.new_product(
        {
            "name": "Яйца",
            "description": "Яйца 1С",
            "price": 500.0,
            "quantity": 1,
        },
        category1,
    )

    # print("При установке цены выше имеющейся, цена меняется на большую").
    # product4.price = 600
    # print(product4.price)
    #
    # print("При установке цены ниже имеющейся, задаётся вопрос")
    # product4.price = 400
    # print(product4.price)
    #
    # print("При установке цены 0, выводится предупреждение")
    # product4.price = 0
    # print(product4.price)
    #
    # print("При установке цены ниже 0, выводится предупреждение")
    # product4.price = -10
    # print(product4.price)

    print("Строковое представление экземпляра")
    print(product4)
    print()

    print("Вычисляем полную стоимость всех товаров на складе")
    print(product1)
    print(product2)
    print(product1 + product2)
    print()
