from src.category import Category


class Product:
    """Класс для создания экземпляров товаров."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор класса Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, params: dict, category):
        new_product = Product(**params)

        for product in category.products:
            if new_product.name in product:
                new_product.price = max(new_product.price, float(product.split(", ")[1].split()[0]))
                category.product_count += 1

        return new_product


if __name__ == "__main__":
    product1 = Product("Молоко", "Молоко коровье 3%", 500.00, 5)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    product2 = Product("Хлеб", "Хлеб белый стандартный", 100.0, 3)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    product3 = Product("Яйца", "Яйца 1С", 500.0, 2)
    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
