import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_grass_init() -> None:
    """
    Тестируем инициализацию экземпляра класса LawnGrass
    """
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass1.name == "Газонная трава"


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


def test_add_method_with_incorrect_instance2(grass_fixture1, product1_fixture) -> None:
    """
    Тестируем работу метода __add__ класса Product с невалидными аргументами
    :param grass_fixture1: экземпляр класса LawnGrass подкласса Product
    :param product1_fixture: экземпляр класса Product
    :return: None
    """
    with pytest.raises(TypeError):
        grass_fixture1 + product1_fixture
