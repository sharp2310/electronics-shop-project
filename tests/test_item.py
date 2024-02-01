"""Здесь надо написать тесты с использованием pytest для модуля item."""
from config import DICT_DIR
from src.item import Item


def test_calculate_total_price():
    obj1 = Item('Телевизор', 50000.0, 10)
    assert obj1.calculate_total_price() == 500000.0

    obj2 = Item('Холодильник', 40000.0, 5)
    Item.pay_rate = 0.8
    obj2.apply_discount()
    assert obj2.calculate_total_price() == 160000.0

    obj3 = Item("Смартфон", 10000, 20)
    obj4 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    obj3.apply_discount()
    assert obj3.price == 8_000.0
    assert obj4.price == 20_000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv(DICT_DIR)
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    item1.name = 'Телефон'
    assert item2.name == 'Телефон'

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'

    item2.name = 'СуперСмартфон'
    assert item2.name == 'СуперСмарт'


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item2 = Item("Смартфон", 10000, 20)


def test_add():
    assert item2 + phone1 == 25
    assert phone1 + phone1 == 10


def test_number_of_sim():
    phone1.number_of_sim = 5
    assert phone1.number_of_sim == 5


def test_exc_number_of_sim():
    phone1.number_of_sim = 0
    assert phone1.number_of_sim() == 0


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("item.csv")


def test_instantiate_csv_error():
    """
    Тест будет работать только в том случае, если добавить файл
    в котором будут не соответствовать данные для метода
    """
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("item.csv")