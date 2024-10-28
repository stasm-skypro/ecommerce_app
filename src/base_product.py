from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс для задания шаблона для создания класса продуктов и дочерних классов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any):
        """Абстрактный метод для создания в потомках одноимённого класс-метода"""
