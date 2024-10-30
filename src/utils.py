import json
import logging
import os
from typing import Any

from src.category import Category
from src.product import Product

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("utils")


def read_json(path: str) -> list | Any:
    """Функция считывает информация из json-файла.
    Args:
        path: str - относительный путь к json-файлу.
    Returns:
        список словарей в формате json.
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        json_content = json.load(file)
        logger.info(f"Файл {full_path} успешно прочитан")

    return json_content


def create_objects_from_json_data(data: list) -> list:
    """Функция создаёт список объектов.
    Args:
        data: json - список словарей в формате json.
    Returns:
        Список объектов класса Products.
    """
    categories = []
    for current_category in data:
        products = []
        for product in current_category["products"]:
            products.append(Product(**product))
        current_category["products"] = products
        categories.append(Category(**current_category))

    return categories


if __name__ == "__main__":
    content = read_json("../data/products.json")
    categories_data = create_objects_from_json_data(content)
    for category in categories_data:
        print(category.name)
        print(category.products)
