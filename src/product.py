from typing import Any, Self

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.project_exceptions import ProductZeroPriceException, ProductZeroQuantityException
from src.user_interraction import use_case_product_price_setter


class Product(BaseProduct, PrintMixin):
    """Класс для создания экземпляров товаров."""

    name: str
    description: str
    __price: float
    quantity: int
    total_price: float
    products_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int, total_price: float = 0) -> None:
        """Конструктор класса Product."""
        self.name = name
        self.description = description
        # Делаем проверку, что товар с отрицательной или нулевой ценой не может быть инициализирован
        if price > 0:
            self.__price = price
        else:
            raise ProductZeroPriceException("Товар с нулевой или отрицательной ценой не может быть инициализирован!")
        # Делаем проверку, что товар с нулевым количеством не может быть инициализирован
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ProductZeroQuantityException("Товар с нулевым количеством не может быть инициализирован!")
        self.total_price = total_price
        # ссылка на  __init__ из родительского класса PrintMixin; так сработает потому, что в
        # родительском классе BaseProduct нет метода __init__
        super().__init__()
        Product.products_list.append(self)

    def __str__(self) -> str:
        """Строковое представление экземпляра класса."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self: Self, other: Any) -> float | Any:
        # Проверяем, что складываются товары только из одинаковых классов продуктов
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, params: dict) -> Any:
        """Метод добавляет новый продукт категорию category."""
        new_product = cls(**params)

        if cls.products_list:
            for product in cls.products_list:
                if new_product.name == product.name:
                    new_product.price = max(new_product.price, product.__price)
                    new_product.quantity += product.quantity
                    break

        cls.products_list.append(new_product)

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
        selected_price = use_case_product_price_setter(price, self.__price)
        self.__price = selected_price


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

    # В случае если товар уже существует, необходимо сложить количество в наличии старого товара и нового.
    # При конфликте цен выбрать ту, которая является более высокой.
    print("Проверка работы метода new_product")
    print("Товар перед добавлением нового:")
    print(product3)
    product31 = Product.new_product(
        {
            "name": "Яйца",
            "description": "Яйца 1С",
            "price": 500.0,
            "quantity": 1,
        }
    )
    print(product31)
    print()

    print("При установке цены выше имеющейся, цена меняется на большую")
    product4.price = 6000.0
    print(product4.price)
    print()

    print("При установке цены ниже имеющейся, задаётся вопрос")
    product4.price = 4000.0
    print(product4.price)
    print()

    print("При установке цены 0, выводится предупреждение")
    product4.price = 0.0
    print(product4.price)
    print()

    print("При установке цены ниже 0, выводится предупреждение")
    product4.price = -10
    print(product4.price)
    print()

    print("Строковое представление экземпляра")
    print(product4)
    print()

    print("Вычисляем полную стоимость всех товаров на складе")
    print(product1)
    print(product2)
    print(product1 + product2)
    print()

    print("Проверяем, что товар с нулевой или отрицательной ценой не может быть создан")
    try:
        product5 = Product("Мыло", "Мыло хозяйственное", -50.0, 1)
    except Exception as e:
        print(f"Сработало  исключение {e} при попытке инициализации продукта с нулевой/отрицательной ценой")
    print()

    print("Проверяем, что Товар с нулевым или отрицательным количеством не может быть создан")
    try:
        product6 = Product("Мыло", "Мыло хозяйственное", 50.0, 0)
    except Exception as e:
        print(f"Сработало  исключение {e} при попытке инициализации продукта с нулевым количеством")
    print()

    print("Проверяем, что Товар с нулевым или отрицательным количеством не может быть добавлен")
    print("Товар перед добавлением нового:")
    print(product3)
    try:
        product32 = Product.new_product(
            {
                "name": "Яйца",
                "description": "Яйца 1С",
                "price": 500.0,
                "quantity": 0,
            }
        )
    except Exception as e:
        print(f"Сработало  исключение {e} при попытке добавления продукта с нулевым количеством")
    print()
