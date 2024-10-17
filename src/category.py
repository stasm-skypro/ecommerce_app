from typing import Any, Self


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
        self.product_count += len(self.__products)

    def __str__(self: Self) -> str:
        # Название категории, количество продуктов: 200 шт.
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    # Реализуем метод для добавления товаров
    def add_product(self, products: list | Any) -> None:
        """Метод добавляет продукт в список продуктов."""
        self.__products.append(products)
        self.product_count += 1

    # Реализуем геттер
    @property
    def products(self) -> list:
        """Метод возвращает список продуктов."""
        products_list = []
        for product in self.__products:
            products_list.append(f"{str(product)}")  # Строковое представление продукта реализовано в классе Product

        return products_list


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    from product import Product

    print("Инициализация категории с пустым списком продуктов")
    category0 = Category(
        name="Пылесосы",
        description="Техника для дома",
    )
    print(category0.name)
    print(category0.description)
    print(category0.products)
    print(category0.category_count)
    print(category0.product_count)
    print()

    print("Инициализация категории 1")
    category1 = Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[
            Product("Молоко", "Молоко коровье 3%", 500.00, 5),
            Product("Хлеб", "Хлеб белый стандартный", 100.00, 3),
            Product("Яйца", "Яйца 1С", 500.00, 2),
        ],
    )
    print(category1.name)
    print(category1.description)
    print(category1.category_count)
    print(category1.product_count)
    print()

    print("Добавление продукта в список продуктов")
    category1.add_product(Product("Молоко", "Молоко коровье 3%", 500.00, 1))
    print(category1.description)
    print(category1.category_count)
    print(category1.product_count)
    print()

    print("Проверка работы геттера")
    print(category1.products)
    print()

    print("Проверка строкового представления экземпляра класса")
    print(category1)
    print()

    print("Инициализация категории 2")
    category2 = Category(
        name="Одежда",
        description="Товары широкого потребления",
        products=[
            Product("Шорты", "Шорты мужские, размер 50", 5000.00, 2),
        ],
    )
    print(category2.name)
    print(category2.description)
    print(category2.category_count)
    print(category2.product_count)
    print()

    print("Проверка работы геттера для категории 1")
    print(category1.products)
    print()

    print("Проверка строкового представления экземпляра класса категории 1")
    print(category1)
    print()

    print("Проверка работы геттера для категории 2")
    print(category2.products)
    print()

    print("Проверка строкового представления экземпляра класса категории 2")
    print(category2)
    print()
