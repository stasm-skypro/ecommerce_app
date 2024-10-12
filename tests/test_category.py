import pytest

from src.category import Category


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

def test_add_single_product():
    """Проверяем работу метода add_product для случая, когда добавляется один продукт."""
    category = Category(name="Спортивные товары", description="Товары для занятий спортом")
    category.add_product("Лыжи")
    assert category._Category__products == ["Лыжи"]
    assert category.product_count == 9

def test_add_multiple_products():
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов."""
    category = Category(name="Спортивные товары", description="Товары для занятий спортом")
    products = ["Лыжи", "Коньки"]
    category.add_product(products)
    assert category._Category__products == [products]
    assert category.product_count == 9  # product_count увеличивается на 1 за каждую добавку

def test_add_product_to_existing_list():
    category = Category(name="Книги", description="Книги всех жанров", products=["Колобок"])
    category.add_product("Мойдодыр")
    assert category._Category__products == ["Колобок", "Мойдодыр"]
    assert category.product_count == 10


def test_products_property():
    from src.product import Product
    product1 = Product(name="Ноутбук", description="Компьютеры", price=80000, quantity=15)
    product2 = Product(name="Смартфон", description="Телефоны", price=60000, quantity=10)
    category = Category(name="Электроника", description="Электроника и устройства для дома", products=[product1, product2])

    expected_result = [
        "Ноутбук, 80000 руб. Остаток: 15",
        "Смартфон, 60000 руб. Остаток: 10"
    ]

    assert category.products == expected_result


def test_products_property_empty():
    category = Category(name="Книги", description="Книги всех жанров")
    assert category.products == []