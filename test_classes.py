import pytest
from classes import Temperature

@pytest.fixture
def temperature_1():
    return Temperature(20)

@pytest.fixture
def temperature_2():
    return Temperature(30)

def test_incorrect_type():
    with pytest.raises(TypeError):
        Temperature('hello')

def test_empties_temperatures():
    with pytest.raises(ValueError):
        Temperature('')

def test_translation_to_fahrenheit(temperature_1):
    assert temperature_1.to_fahrenheit() == 68, 'result 68'


def test_translation_to_kelvin(temperature_2):
    assert temperature_2.to_kelvin() == 303, 'result 303'

def test_positive_value(temperature_1):
    assert temperature_1.is_positive() == True, 'result true'


def test_positive_value_1():
    temp = Temperature(-10)
    assert temp.is_positive() == False, 'result False'

def test_zero_value(temperature_1):
    assert temperature_1.is_positive() == True, 'result True'

def test_zero_value1():
    temp = Temperature(0)
    assert temp.is_positive() == True, 'result True'

def test_static_method_returns_minus_one():
    temp = Temperature.compare(20, 10)
    assert temp == -1, 'result -1'

def test_static_method_returns_zero():
    temp = Temperature.compare(20, 20)
    assert temp == 0, 'result 0'

def test_static_method_returns_plus_one():
    temp = Temperature.compare(20, 30)
    assert temp == 1, 'result 1'








