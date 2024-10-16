import pytest

from src.category import Category
from src.product_iterator import ProductIterator
from tests.conftest import product2_fixture


def test_category0_init(category0_fixture: Category) -> None:
    """Тестируем инициализацию экземпляра класса Category для случая, когда
    параметр products не передаётся (None)."""
    assert category0_fixture.products == []


def test_category1_init(category1_fixture: Category) -> None:
    """Тестируем инициализацию экземпляра класса Category."""
    assert category1_fixture.name == "Продукты"
    assert category1_fixture.description == "Товары первой необходимости"


def test_category2_init(category2_fixture: Category) -> None:
    """Тестируем инициализацию экземпляра класса Category."""
    assert category2_fixture.name == "Одежда"
    assert category2_fixture.description == "Товары широкого потребления"


def test_category1_count(category1_fixture: Category) -> None:
    """Проверяем, что в категории создано валидное количество товаров."""
    assert len(category1_fixture.products) == 3


def test_category2_count(category2_fixture: Category) -> None:
    """Проверяем, что в категории создано валидное количество товаров."""
    assert len(category2_fixture.products) == 1


def test_add_single_product() -> None:
    """Проверяем работу метода add_product для случая, когда добавляется один продукт."""
    category = Category(name="Спортивные товары", description="Товары для занятий спортом")
    category.add_product("Лыжи")
    assert category._Category__products == ["Лыжи"]
    assert category.product_count == 9


def test_add_multiple_products() -> None:
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов."""
    category = Category(name="Спортивные товары", description="Товары для занятий спортом")
    products = ["Лыжи", "Коньки"]
    category.add_product(products)
    assert category._Category__products == [products]
    assert category.product_count == 9  # product_count увеличивается на 1 за каждую добавку


def test_add_product_to_existing_list(category1_fixture, product2_fixture) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов и продукт в конструктор."""
    category1_fixture.add_product(product2_fixture)
    assert category1_fixture.products == ['Молоко, 500.0 руб. Остаток: 5 шт.', 'Хлеб, 100.0 руб. Остаток: 3 шт.', 'Яйца, 500.0 руб. Остаток: 2 шт.', 'Хлеб, 100.0 руб. Остаток: 3 шт.']


def test_products_property() -> None:
    """Проверяем работу геттера когда есть список продуктов."""
    from src.product import Product

    product1 = Product(name="Ноутбук", description="Компьютеры", price=80000, quantity=15)
    product2 = Product(name="Смартфон", description="Телефоны", price=60000, quantity=10)
    category = Category(
        name="Электроника", description="Электроника и устройства для дома", products=[product1, product2]
    )
    expected_result = ["Ноутбук, 80000 руб. Остаток: 15 шт.", "Смартфон, 60000 руб. Остаток: 10 шт."]
    assert category.products == expected_result


def test_products_property_empty() -> None:
    """Проверяем работу геттера когда список продуктов пустой."""
    category = Category(name="Книги", description="Книги всех жанров")
    assert category.products == []


def test_category_str(category1_fixture: Category) -> None:
    """Тест для проверки метода __str__ класса Category."""
    assert str(category1_fixture) == "Продукты, количество продуктов: 14 шт."


def test_product_iterator(product_iterator: ProductIterator) -> None:
    """Тестируем работу итератора класса ProductIterator."""
    assert product_iterator.current == 0
    assert next(product_iterator) == "Молоко, 500.0 руб. Остаток: 5 шт."
    assert next(product_iterator) == "Хлеб, 100.0 руб. Остаток: 3 шт."
    assert next(product_iterator) == "Яйца, 500.0 руб. Остаток: 2 шт."

    with pytest.raises(StopIteration):
        next(product_iterator)
