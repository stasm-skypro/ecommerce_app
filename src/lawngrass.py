from src.product import Product


class LawnGrass(Product):
    """
    Класс для создания экземпляров класса LawnGrass
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
        total_price: float = 0,
    ) -> None:
        """
        Конструктор класса LawnGrass
        """
        super().__init__(name, description, price, quantity, total_price)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print("grass1")
    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)
    print()

    print("grass2")
    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)
    print()

    print("new_product")
    params = {
        "name": "Газонная трава",
        "description": "Элитная трава для газона",
        "price": 500.0,
        "quantity": 20,
        "country": "Россия",
        "germination_period": "7 дней",
        "color": "Зеленый",
    }
    new_grass_product = LawnGrass.new_product(params)
    print(new_grass_product)
