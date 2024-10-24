from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для задания шаблона для создания класса продуктов и дочерних классов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
