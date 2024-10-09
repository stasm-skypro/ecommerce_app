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
