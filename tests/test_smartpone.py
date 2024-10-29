import pytest

from src.lawngrass import LawnGrass
from src.project_exceptions import ProductZeroPriceException, ProductZeroQuantityException
from src.smartphone import Smartphone


def test_smartphone_init() -> None:
    """
    Тестируем инициализацию экземпляра класса Smartphone
    """
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_add_method_with_correct_instances(smartphone_fixture1: Smartphone, smartphone_fixture2: Smartphone) -> None:
    """
    Тестируем работу метода __add__ класса Product с валидными аргументами
    :param smartphone_fixture1: экземпляр класса Smartphone подкласса Product
    :param smartphone_fixture2: экземпляр класса Smartphone подкласса Product
    :return: None
    """
    assert smartphone_fixture1 + smartphone_fixture2 == 2580000.0


def test_add_method_with_incorrect_instance(smartphone_fixture1: Smartphone, grass_fixture1: LawnGrass) -> None:
    """
    Тестируем работу метода __add__ класса Product с невалидными аргументами
    :param smartphone_fixture1: экземпляр класса Smartphone подкласса Product
    :param grass_fixture1: экземпляр класса LownGrass подкласса Product
    :return: None
    """
    with pytest.raises(TypeError):
        smartphone_fixture1 + grass_fixture1


def test_add_method_with_incorrect_instance2(smartphone_fixture1: Smartphone, product1_fixture: Smartphone) -> None:
    """
    Тестируем работу метода __add__ класса Product с невалидными аргументами
    :param smartphone_fixture1: экземпляр класса Smartphone подкласса Product
    :param product1_fixture: экземпляр класса Product
    :return: None
    """
    with pytest.raises(TypeError):
        smartphone_fixture1 + product1_fixture


def test_str_method(smartphone_fixture1: Smartphone) -> None:
    """Тестируем строковое представление."""
    assert str(smartphone_fixture1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_new_product(smartphone_params_fixture: dict) -> None:
    """Тестируем класс-метод new_product."""
    new_smartphone = Smartphone.new_product(smartphone_params_fixture)
    assert new_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert new_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert new_smartphone.price == 180000.0
    assert new_smartphone.quantity == 10
    assert new_smartphone.efficiency == 95.5
    assert new_smartphone.model == "S23 Ultra"
    assert new_smartphone.memory == 256
    assert new_smartphone.color == "Серый"


def test_smartphone_init_with_zero_quantity() -> None:
    """Проверяем, что при попытке инициализации продукта с нулевым количеством возникнет исключение."""
    with pytest.raises(ProductZeroQuantityException):
        Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0, 95.5, "S23 Ultra", 256, "Серый"
        )


def test_smartphone_init_with_zero_price() -> None:
    """Проверяем, что при попытке инициализации продукта с нулевой ценой возникнет исключение."""
    with pytest.raises(ProductZeroPriceException):
        Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
