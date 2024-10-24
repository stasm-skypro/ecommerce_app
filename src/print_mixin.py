class PrintMixin:
    """Класс-миксин, который при создании объекта, то есть при работе метода __init__, печатает в консоль
    информацию о том, от какого класса и с какими параметрами был создан объект.
    Пример работы метода: Product('Продукт1', 'Описание продукта', 1200, 10)."""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.quantity}, {self.price})"
