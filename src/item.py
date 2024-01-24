import csv
import re
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self._name

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            new_name = new_name[0:10]
        self._name = new_name

    def __add__(self, other):
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
    def instantiate_from_csv(cls, path: str):
        """
        Инициализирует экземпляры класса из CSV-файла
        """
        with open(path, 'r') as file:
            csv_reader = csv.DictReader(file)
            Item.all = []
            for row in csv_reader:
                _name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(_name, price, quantity)

    @staticmethod
    def string_to_number(string):
        try:
            if "." in string:
                string = string.split('.')[0]
            return int(string)
        except ValueError:
            return None
