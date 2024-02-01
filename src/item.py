import os
from csv import DictReader

from src.error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.__name = name[:10]
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new__name: str):
        if len(new__name) > 10:
            new__name = new__name[0:10]
        self.__name = new__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError(
                "Unsupported operand type(s) for +: '{}' and '{}'".format(type(self).__name__, type(other).__name__))
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара, округленная до 2 десятичных знаков.
        """

        total_price = self.price * self.quantity
        return round(total_price, 2)

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара и возвращает новую цену после применения скидки.

        """

        if not isinstance(self.pay_rate, (float, int)):
            raise ValueError("Pay rate must be a number.")

        if not 0 <= self.pay_rate <= 1:
            raise ValueError("Pay rate must be a valid percentage between 0 and 1.")

        self.price = round(self.price * self.pay_rate, 2)

    @classmethod
    def instantiate_from_csv(cls, path: str = "../tests/test_path.csv"):
        """
        Инициализирует экземпляры класса из CSV-файла
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Отсутствует файл {path}")
        with open(path, 'r') as file:
            csv_reader = DictReader(file)
            Item.all = []
            for row in csv_reader:
                if None in row or '' in row:
                    raise InstantiateCSVError(f"Файл {path} поврежден")
                if None in row.values() or ' ' in row.values():
                    raise InstantiateCSVError(f"Файл {path} поврежден")
                __name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(__name, price, quantity)


    @staticmethod
    def string_to_number(string):
        try:
            if "." in string:
                string = string.split('.')[0]
            return int(string)
        except ValueError:
            return None
