import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.order import Order
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def category0_fixture() -> Category:
    """Фикстура для тестирования инициализации экземпляров класса Category с пустым списком продуктов."""
    return Category(
        name="Пылесосы",
        description="Техника для дома",
    )


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


@pytest.fixture
def params_fixture() -> dict:
    """Фикстура для метода new_product класса Product."""
    return {
        "name": "Яйца",
        "description": "Яйца 1С",
        "price": 500.0,
        "quantity": 1,
    }


@pytest.fixture
def product_iterator(category1_fixture: Category) -> ProductIterator:
    """Фикстура для тестирования инициализации и работы класса ProductIterator."""
    return ProductIterator(category1_fixture)


@pytest.fixture
def smartphone_fixture1() -> Smartphone:
    """
    Фикстура для тестирования инициализации экземпляра класса SmartPhone
    """
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_fixture2() -> Smartphone:
    """
    Фикстура для тестирования инициализации экземпляра класса SmartPhone
    """
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_params_fixture() -> dict:
    """Фикстура для создания нового экземпляра методом new_product."""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": 95.5,
        "model": "S23 Ultra",
        "memory": 256,
        "color": "Серый",
    }


@pytest.fixture
def grass_fixture1() -> LawnGrass:
    """
    Фикстура для проверки инициализации экземпляра класса LawnGrass
    """
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_fixture2() -> LawnGrass:
    """
    Фикстура для проверки инициализации экземпляра класса LawnGrass
    """
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def grass_params_fixture() -> dict:
    """Фикстура для создания нового экземпляра методом new_product."""
    return {
        "name": "Газонная трава",
        "description": "Элитная трава для газона",
        "price": 500.0,
        "quantity": 20,
        "country": "Россия",
        "germination_period": "7 дней",
        "color": "Зеленый",
    }


@pytest.fixture
def order0_fixture() -> Order:
    """Фикстура для инициализации заказа с пустым списком заказов."""
    return Order("Заказ", "Заказ непоймичего", [])


@pytest.fixture
def order1_fixture() -> Order:
    """Фикстура для инициализации заказа1."""
    return Order(
        "Заказ1",
        "Заказ в интернет-магазине",
        [
            Smartphone(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                1,
                95.5,
                "S23 Ultra",
                256,
                "Серый",
            )
        ],
    )


@pytest.fixture
def order2_fixture(grass_fixture1: LawnGrass) -> Order:
    """Фикстура для инициализации заказа2."""
    return Order(
        "Заказ2",
        "Заказ в интернет-магазине",
        [LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 1, "Россия", "7 дней", "Зеленый")],
    )
