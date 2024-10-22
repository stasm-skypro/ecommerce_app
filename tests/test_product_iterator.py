import pytest

from src.product_iterator import ProductIterator


def test_product_iterator(product_iterator: ProductIterator) -> None:
    """Тестируем работу итератора класса ProductIterator."""
    assert product_iterator.current == 0
    assert next(product_iterator) == "Молоко, 500.0 руб. Остаток: 5 шт."
    assert next(product_iterator) == "Хлеб, 100.0 руб. Остаток: 3 шт."
    assert next(product_iterator) == "Яйца, 500.0 руб. Остаток: 2 шт."

    with pytest.raises(StopIteration):
        next(product_iterator)
