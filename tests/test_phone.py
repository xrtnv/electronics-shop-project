from src.item import Item
from src.phone import Phone


def test_phone_creation():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2

def test_add_phone_and_item():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Смартфон", 10000, 20)
    assert phone + item == 25

def test_add_two_phones():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80_000, 5, 1)
    assert phone1 + phone2 == 10

def test_invalid_addition():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    not_an_item = "Not an Item"
    try:
        result = phone + not_an_item
    except TypeError as e:
        assert str(e) == "Unsupported operand type(s) for +: 'Phone' and 'str'"