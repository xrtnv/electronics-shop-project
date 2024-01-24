import pytest

from src.keyboard import LangMixin, Keyboard


def test_init():
    keyboard = Keyboard("Keyboard", 50.0, 10)
    assert keyboard.name == "Keyboard"
    assert keyboard.price == 50.0
    assert keyboard.quantity == 10
    assert keyboard.language == "EN"

    keyboard = Keyboard("Keyboard", 50.0, 10)
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"

    keyboard = Keyboard("Keyboard", 50.0, 10)
    assert keyboard.calculate_total_price() == 500.0

    with pytest.raises(ValueError):
        Keyboard("", 50.0, 10)

    with pytest.raises(ValueError):
        Keyboard("Keyboard", 50.0, -10)

    with pytest.raises(ValueError):
        Keyboard("Keyboard", -50.0, 10)