from typing import Self, Any

from src.category import Category
from src.product import Product


class ProductIterator:
    """Класс для итерирования по списку продуктов в категории."""

    def __init__(self: Self, category_object: Category) -> None:
        self.category = category_object
        self.current = 0

    def __iter__(self: Self) -> Self:
        self.current = 0
        return self

    def __next__(self: Self) -> StopIteration | Product | Any:
        if self.current >= len(self.category.products):
            raise StopIteration
        else:
            current_product = self.category.products[self.current]
            self.current += 1
            return current_product


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    product1 = Product("Молоко", "Молоко коровье 3%", 500.00, 5)
    product2 = Product("Хлеб", "Хлеб белый стандартный", 100.0, 3)
    product3 = Product("Яйца", "Яйца 1С", 500.0, 2)

    category2 = Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[product1, product2, product3],
    )

    # Создадим экземпляр класса ProductIterator.
    pi = ProductIterator(category2)

    for product in pi:
        print(product)
