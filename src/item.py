import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

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
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print('Длина наименования товара превышает 10 символов.')
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        cls.all.clear()

        with open(csvfile, newline='', encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for ex in reader:
                cls(ex['name'], float(ex['price']), int(ex['quantity']))

    @staticmethod
    def string_to_number(some_num):
        return int(float(some_num))

