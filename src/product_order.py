from src.product import Product
from src.base_order import BaseOrder
from src.smartphone import Smartphone


class ProductOrder(BaseOrder):
    """Класс заказов"""

    name: str
    description: str
    __orders: list
    order_count: int = 0

    def __init__(self, name: str, description: str, orders: list | None = None) -> None:
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__orders = orders if orders else []
        self.order_count += len(self.__orders)

    def add_product(self, product: Product) -> None:
        """Метод добавляет продукт в список заказов."""
        if isinstance(product, Product):
            self.__orders.append(product)
            self.order_count += 1
        else:
            raise TypeError

    def __str__(self) -> str:
        # Название категории, количество продуктов: 200 шт.
        return f"{self.name}, количество продуктов: {self.order_count} шт."

    # Реализуем геттер
    @property
    def orders(self) -> list:
        """Метод возвращает список продуктов в заказе."""
        products_list = []
        for product in self.__orders:
            products_list.append(f"{str(product)}")  # Строковое представление продукта реализовано в классе Product

        return products_list


if __name__ == "__main__":
    print("Инициализация заказа с пустым списков продуктов")
    order = ProductOrder("Заказ", "Заказ непоймичего", [])
    print(order.name)
    print(order.description)
    print(order.orders)
    print(order)
    print()

    print("Инициализация заказа 1")
    order1 = ProductOrder(
        "Заказ1",
        "Заказ в интернет-магазине",
        [
            Smartphone(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                1,
                95.5,
                "S23 Ultra",
                256,
                "Серый",
            )
        ],
    )
    print(order1.orders)
    print(order1)
    print()

    print("Добавление продукта в список заказов")
    order1.add_product(
        Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            1,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )
    )
    print(order1.orders)
    print(order1)
    print()