import pytest

from src.product import Product


def test_product1_init(product1_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product1_fixture.name == "Молоко"
    assert product1_fixture.description == "Молоко коровье 3%"
    assert product1_fixture.price == 500.00


def test_product2_init(product2_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product2_fixture.name == "Хлеб"
    assert product2_fixture.description == "Хлеб белый стандартный"
    assert product2_fixture.price == 100.00


def test_product3_init(product3_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product3_fixture.name == "Яйца"
    assert product3_fixture.description == "Яйца 1С"
    assert product3_fixture.price == 500.00


def test_product4_init(product4_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product4_fixture.name == "Шорты"
    assert product4_fixture.description == "Шорты мужские, размер 50"
    assert product4_fixture.price == 5000.00


def test_product1_count(product1_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product1_fixture.quantity == 5


def test_product2_count(product2_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product2_fixture.quantity == 3


def test_product3_count(product3_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product3_fixture.quantity == 2


def test_product4_count(product4_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product4_fixture.quantity == 2


# Тест для класс-метода new_product
class Category:
    """Класс для создания категорий товаров."""

    def __init__(self) -> None:
        self.products = []
        self.product_count = 0


@pytest.fixture
def category() -> Category:
    """Определяем фикстуру для класса Category."""
    cat = Category()
    cat.products = ["Пиво Hoegaarden, 100.0 руб.", "Пиво Heineken, 150.0 руб."]
    return cat


def test_new_product(category) -> None:
    """Тестируем класс-метод new_product."""
    params = {
        "name": "Пиво Hoegaarden",
        "description": "Пиво и слабоалкогольные напитки",
        "price": 120.0,
        "quantity": 10
    }

    new_product = Product.new_product(params, category)

    assert new_product.name == "Пиво Hoegaarden"
    assert new_product.description == "Пиво и слабоалкогольные напитки"
    assert new_product.price == 120.0  # Цена не изменится, так как 120.0 < 150.0
    assert new_product.quantity == 10
    assert category.product_count == 1  # Увеличится на 1, так как продукт с таким именем уже есть


def test_new_product_new_entry(category):
    params = {
        "name": "Пармезан",
        "description": "Натуральные сыры",
        "price": 200.0,
        "quantity": 5
    }

    new_product = Product.new_product(params, category)

    assert new_product.name == "Пармезан"
    assert new_product.description == "Натуральные сыры"
    assert new_product.price == 200.0  # Цена останется такой же, так как это новый продукт
    assert new_product.quantity == 5
    assert category.product_count == 0  # Не увеличится, так как это новый продукт
