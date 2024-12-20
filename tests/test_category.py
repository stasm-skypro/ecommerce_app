import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


def test_category0_init(category0_fixture: Category) -> None:
    """Тестируем инициализацию экземпляра класса Category для случая, когда
    параметр products не передаётся (None)."""
    assert category0_fixture.products == []


def test_category1_init(category1_fixture: Category) -> None:
    """Тестируем инициализацию экземпляра класса Category."""
    assert category1_fixture.name == "Продукты"
    assert category1_fixture.description == "Товары первой необходимости"


def test_category1_product_count(category1_fixture: Category) -> None:
    """Проверяем, что в категории создано валидное количество товаров."""
    assert len(category1_fixture.products) == 3


def test_category1_count(category1_fixture: Category) -> None:
    """Проверяем, что считается валидное количество категорий."""
    assert category1_fixture.category_count == 4  # это 4-я по счёту созданная категория товаров


def test_category1_count2(category2_fixture: Category) -> None:
    """Проверяем, что считается валидное количество категорий."""
    assert category2_fixture.category_count == 5  # это 5-я по счёту созданная категория товаров


def test_add_single_product(category1_fixture: Category, product2_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется один продукт."""
    category1_fixture.add_product(product2_fixture)
    assert category1_fixture.products == [
        "Молоко, 500.0 руб. Остаток: 5 шт.",
        "Хлеб, 100.0 руб. Остаток: 3 шт.",
        "Яйца, 500.0 руб. Остаток: 2 шт.",
        "Хлеб, 100.0 руб. Остаток: 3 шт.",
    ]
    assert category1_fixture.product_count == 4


def test_add_product_to_existing_list(product1_fixture: Product, product2_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов и продукт в конструктор."""
    test_category = Category(name="Продукты", description="Товары первой необходимости", products=[product1_fixture])
    test_category.add_product(product2_fixture)
    assert test_category.products == ["Молоко, 500.0 руб. Остаток: 5 шт.", "Хлеб, 100.0 руб. Остаток: 3 шт."]


def test_add_product_to_existing_list2(smartphone_fixture1: Smartphone, smartphone_fixture2: Smartphone) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов и продукт в конструктор."""
    test_category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения \
                             дополнительных функций для удобства жизни",
        products=[smartphone_fixture1],
    )
    test_category.add_product(smartphone_fixture2)
    assert test_category.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
    ]


def test_add_product_if_invalid_arg(product1_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется не экземпляр класса Product."""
    test_category = Category(name="Продукты", description="Товары первой необходимости", products=[product1_fixture])
    with pytest.raises(TypeError):
        test_category.add_product("Not product")


def test_category_getter() -> None:
    """Проверяем работу геттера когда есть список продуктов."""
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
    assert str(category1_fixture) == "Продукты, количество продуктов: 3 шт."


def test_get_average_product_price(
    product1_fixture: Product, product2_fixture: Product, product3_fixture: Product
) -> None:
    """Тест на вычисление средней цены в категории."""
    test_category = Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[
            product1_fixture,
            product2_fixture,
            product3_fixture,
        ],
    )
    assert test_category.get_average_product_price() == 366.67
