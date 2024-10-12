from typing import Any


class Category:
    """Класс для создания экземпляров категорий товаров."""

    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        """Конструктор класса Category."""
        self.name = name
        self.description = description
        self.__products = products if products else []  # делаем список товаров приватным атрибутом
        Category.category_count += 1
        Category.product_count += len(self.__products)

    # Реализуем метод для добавления товаров
    def add_product(self, products: list | Any)->None:
        """Метод добавляет продукт в список продуктов."""
        self.__products.append(products)
        self.product_count += 1

    # Реализуем геттер
    @property
    def products(self) -> list:
        """Метод возвращает список продуктов."""
        # Название продукта, 80 руб. Остаток: 15 шт.
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity}")

        return products_list


if __name__ == "__main__":
    from product import Product

    category1 = Category(
        name="Пылесосы",
        description="Техника для дома",
        products=[],
    )
    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1.category_count)
    print(category1.product_count)

    category2 = Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[
            Product("Молоко", "Молоко коровье 3%", 500.00, 5),
            Product("Хлеб", "Хлеб белый стандартный", 100.00, 3),
            Product("Яйца", "Яйца 1С", 500.00, 2),
        ],
    )
    print(category2.name)
    print(category2.description)
    print(category2.category_count)
    print(category2.product_count)

    category3 = Category(
        name="Одежда",
        description="Товары широкого потребления",
        products=[
            Product("Шорты", "Шорты мужские, размер 50", 5000.00, 2),
        ],
    )
    print(category3.name)
    print(category3.description)
    print(category3.category_count)
    print(category3.product_count)


