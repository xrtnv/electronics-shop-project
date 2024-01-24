import csv

import pytest
from src.item import Item


def test_valid_parameters_no_errors():
    item = Item("Item 1", 100, 1)
    assert item.name == "Item 1"
    assert item.price == 100
    assert item.quantity == 1
    assert item in Item.all


def test_calculate_total_price():
    item = Item("Item 2", 50, 2)
    total_price = item.calculate_total_price()
    assert total_price == 100


def test_apply_discount_valid_discount():
    item = Item("Item 3", 100, 1)
    item.pay_rate = 0.1
    item.apply_discount()
    assert item.price == 10


def test_empty_name_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("", 100, 1)


def test_negative_quantity_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("Item 4", 100, -1)


def test_zero_or_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        item = Item("Item 5", -100, 1)


def test_instantiate_from_csv():
    csv_path = "test.csv"
    csv_data = [
        {"name": "Item 1", "price": "10.99", "quantity": "5"},
        {"name": "Item 2", "price": "5.99", "quantity": "10"},
        {"name": "Item 3", "price": "2.99", "quantity": "3"}
    ]
    with open(csv_path, 'w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
        writer.writeheader()
        writer.writerows(csv_data)

    # Act
    Item.instantiate_from_csv(csv_path)

    # Assert
    assert len(Item.all) == 3
    assert Item.all[0].name == "Item 1"
    assert Item.all[0].price == 10
    assert Item.all[0].quantity == 5
    assert Item.all[1].name == "Item 2"
    assert Item.all[1].price == 5
    assert Item.all[1].quantity == 10
    assert Item.all[2].name == "Item 3"
    assert Item.all[2].price == 2
    assert Item.all[2].quantity == 3

def test_returns_none_when_given_string_with_non_digit_characters():
    item = Item('1',1,1)
    string = "12a34"
    result = item.string_to_number(string)
    assert result is None
    string = ""
    result = item.string_to_number(string)
    assert result is None
    string = "123"
    result = item.string_to_number(string)
    assert result is 123
    string = "1.23"
    result = item.string_to_number(string)
    assert result is 1

def test_repr():
    item = Item("Item 1", 10.0, 5)
    assert repr(item) == f"Item('{item.name}', {item.price}, {item.quantity})"

    item = Item("aaaaaaaaaaaaaaa", 10.0, 5)
    assert repr(item) == "Item('aaaaaaaaaa', 10.0, 5)"

def test_str():
    item = Item("Phone", 1000, 10)
    assert str(item) == "Phone"

    item = Item("Smartphone1234567890", 1000, 10)
    assert str(item) == "Smartphone"

    with pytest.raises(ValueError) as e:
        item = Item("", 1000, 10)
    assert str(e.value) == "Name cannot be empty."

    with pytest.raises(ValueError) as e:
        item = Item("Phone", 1000, -10)
    assert str(e.value) == "Quantity must be a non-negative integer."

