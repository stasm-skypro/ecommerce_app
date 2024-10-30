import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_with_product(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяем, что при создании экземпляра класса Product происходит вывод в консоль."""
    # Создаём экземпляр класса через конструктор
    Product("Молоко", "Молоко коровье 3%", 500.00, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Молоко, Молоко коровье 3%, 500.0, 5)"

    # Создаём экземпляр класса через метод new_product
    Product.new_product(
        {
            "name": "Яйца",
            "description": "Яйца 1С",
            "price": 500.0,
            "quantity": 1,
        }
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Product(Яйца, Яйца 1С, 500.0, 1)\n"
        "Цена продукта не изменилась. Оставляем цену - 500.0."
    )


def test_print_mixin_with_smartphone(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяем, что при создании экземпляра класса Product происходит вывод в консоль."""
    # Создаём экземпляр дочернего класса Smartphone через конструктор
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    # Создаём экземпляр класса через метод new_product
    Smartphone.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 1,
            "efficiency": 95.5,
            "model": "S23 Ultra",
            "memory": 256,
            "color": "Серый",
        }
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 1)\n"
        "Цена продукта не изменилась. Оставляем цену - 180000.0."
    )


def test_print_mixin_with_lawngrass(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяем, что при создании экземпляра класса Product происходит вывод в консоль."""
    # Создаём экземпляр дочернего класса Smartphone через конструктор
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"

    # Создаём экземпляр класса через метод new_product
    LawnGrass.new_product(
        {
            "name": "Газонная трава",
            "description": "Элитная трава для газона",
            "price": 500.0,
            "quantity": 20,
            "country": "Россия",
            "germination_period": "7 дней",
            "color": "Зеленый",
        }
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n"
        "Цена продукта не изменилась. Оставляем цену - 500.0."
    )
