from abc import ABC, abstractmethod
from typing import Any


class BaseOrder(ABC):
    """Абстрактный класс для классов ProductOrder и Category"""

    @abstractmethod
    def add_product(self, *args: Any, **kwargs: Any) -> None:
        pass
