class ProductZeroQuantityException(Exception):
    """Пользовательский класс исключения товара с нулевым количеством"""

    def __init__(self, msg: str = "") -> None:
        """Инициализатор экземпляра класса"""
        super().__init__(msg)


class ProductZeroPriceException(Exception):
    """Пользовательский класс исключения товара с нулевой ценой"""

    def __init__(self, msg: str = "") -> None:
        """Инициализатор экземпляра класса"""
        super().__init__(msg)
