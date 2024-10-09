import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category1_fixture() -> Category:
    """Фикстура для тестирования инициализации экземпляров класса Category."""
    return Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[
            Product("Молоко", "Молоко коровье 3%", 500.00, 5),
            Product("Хлеб", "Хлеб белый стандартный", 100.00, 3),
            Product("Яйца", "Яйца 1С", 500.00, 2),
        ],
    )


@pytest.fixture
def category2_fixture() -> Category:
    """Фикстура для тестирования инициализации экземпляров класса Category."""
    return Category(
        name="Одежда",
        description="Товары широкого потребления",
        products=[
            Product("Шорты", "Шорты мужские, размер 50", 5000.00, 2),
        ],
    )


@pytest.fixture
def product1_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Молоко", description="Молоко коровье 3%", price=500.00, quantity=5)


@pytest.fixture
def product2_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Хлеб", description="Хлеб белый стандартный", price=100.00, quantity=3)


@pytest.fixture
def product3_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Яйца", description="Яйца 1С", price=500.00, quantity=2)


@pytest.fixture
def product4_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Шорты", description="Шорты мужские, размер 50", price=5000.00, quantity=2)
