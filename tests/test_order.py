import pytest

from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product


def test_order0_init(order0_fixture: Order) -> None:
    """Тестируем инициализацию экземпляра класса Category."""
    assert order0_fixture.name == "Заказ"
    assert order0_fixture.description == "Заказ непоймичего"
    assert order0_fixture.orders == []


def test_order1_init(order1_fixture: Order) -> None:
    """Тестируем инициализацию экземпляра класса Category."""
    assert order1_fixture.name == "Заказ1"
    assert order1_fixture.description == "Заказ в интернет-магазине"
    assert order1_fixture.orders == ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 1 шт."]


def test_order_str(order1_fixture: Order) -> None:
    """Тест для проверки метода __str__ класса Category."""
    assert str(order1_fixture) == "Заказ1, количество продуктов: 1 шт."


def test_order1_product_count(order1_fixture: Order) -> None:
    """Проверяем, что в заказе создано валидное количество товаров."""
    assert len(order1_fixture.orders) == 1


def test_add_single_product(order1_fixture: Order, grass_fixture1: LawnGrass) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется один продукт."""
    order1_fixture.add_product(grass_fixture1)
    assert order1_fixture.orders == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 1 шт.",
        "Газонная трава, 500.0 руб. Остаток: 20 шт.",
    ]
    assert order1_fixture.order_count == 2


def test_add_product_if_invalid_arg(product1_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется не экземпляр класса Product."""
    test_order = Order(name="Продукты", description="Товары первой необходимости", orders=[product1_fixture])
    with pytest.raises(TypeError):
        test_order.add_product("Not product")


def test_get_average_product_price(
    product1_fixture: Product, product2_fixture: Product, product3_fixture: Product
) -> None:
    """Тест на вычисление средней цены в категории."""
    test_order = Order(
        name="Продукты",
        description="Товары первой необходимости",
        orders=[
            product1_fixture,
            product2_fixture,
            product3_fixture,
        ],
    )
    assert test_order.get_average_product_price() == 366.67
