class ZeroProductQuantityException(Exception):
    """Пользовательский класс исключения товара с нулевым количеством"""

    def __init__(self, msg: str = None) -> None:
        """Инициализатор экземпляра класса"""
        super().__init__(msg)
