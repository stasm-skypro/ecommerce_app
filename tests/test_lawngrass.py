import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_grass_init() -> None:
    """
    Тестируем инициализацию экземпляра класса LawnGrass
    """
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_method_with_correct_instance(grass_fixture1: LawnGrass, grass_fixture2: LawnGrass) -> None:
    """
    Тестируем работу метода __add__ класса Product с валидными аргументами
    :param grass_fixture1: экземпляр класса LawnGrass подкласса Product
    :param grass_fixture2: экземпляр класса LawnGrass подкласса Product
    :return: None
    """
    assert grass_fixture1 + grass_fixture2 == 16750.0


def test_add_method_with_incorrect_instance(grass_fixture1: LawnGrass, smartphone_fixture1: Smartphone) -> None:
    """
    Тестируем работу метода __add__ класса Product с невалидными аргументами
    :param grass_fixture1: экземпляр класса LawnGrass подкласса Product
    :param smartphone_fixture1: экземпляр класса Smartphone подкласса Product
    :return: None
    """
    with pytest.raises(TypeError):
        grass_fixture1 + smartphone_fixture1


def test_add_method_with_incorrect_instance2(grass_fixture1: LawnGrass, product1_fixture: LawnGrass) -> None:
    """
    Тестируем работу метода __add__ класса Product с невалидными аргументами
    :param grass_fixture1: экземпляр класса LawnGrass подкласса Product
    :param product1_fixture: экземпляр класса Product
    :return: None
    """
    with pytest.raises(TypeError):
        grass_fixture1 + product1_fixture


def test_str_method(grass_fixture1: LawnGrass) -> None:
    """Тестируем строковое представление."""
    assert str(grass_fixture1) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_new_product(grass_params_fixture: dict) -> None:
    """Тестируем класс-метод new_product."""
    new_grass = LawnGrass.new_product(grass_params_fixture)
    assert new_grass.name == "Газонная трава"
    assert new_grass.description == "Элитная трава для газона"
    assert new_grass.price == 500.0
    assert new_grass.quantity == 40
    assert new_grass.country == "Россия"
    assert new_grass.germination_period == "7 дней"
    assert new_grass.color == "Зеленый"
