"""Здесь надо написать тесты с использованием pytest для модуля item."""
from config import DICT_DIR
from src.item import Item


def test_calculate_total_price():
    obj1 = Item('помидорка', 15.0, 20)
    assert obj1.calculate_total_price() == 300

    obj2 = Item('луковичок', 20.0, 1)
    Item.pay_rate = 0.8
    obj2.apply_discount()
    assert obj2.calculate_total_price() == 16.0

    obj3 = Item("Смартфон", 10000, 20)
    obj4 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    obj3.apply_discount()
    assert obj3.price == 8_000.0
    assert obj4.price == 20_000.0


