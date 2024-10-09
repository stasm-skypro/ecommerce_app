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
