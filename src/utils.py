import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """Функция считывает информация из json-файла.
    Args:
        path: str - относительный путь к json-файлу.
    Returns:
        список словарей в формате json.
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        json_content = json.load(file)

    return json_content


def create_objects_from_json_data(data: list) -> list:
    """Функция создаёт список объектов.
    Args:
        data: json - список словарей в формате json.
    Returns:
        Список объектов класса Products.
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    data = read_json("../data/products.json")
    categories_data = create_objects_from_json_data(data)
    for category in categories_data:
        print(category.name)
        print(category.products)
