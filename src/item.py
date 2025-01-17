import os
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 100:
            self.__name = new_name
        else:
            # print("Длина наименования товара превышает 10 символов.")
            raise "Длина наименования товара превышает 10 символов."

    @name.getter
    def name(self): return self.__name

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):

        cls.all.clear()

        file = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(file, 'r', encoding="windows-1251") as file:
                reader_csv = DictReader(file)
                for row in reader_csv:
                    name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                    cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(data):
        num = float(data)
        return int(num)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            return "Складывать можно только значения Item и дочерние от них"
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "файл item.csv поврежден"

    def __str__(self):
        return self.message
