import pytest
from classes import Temperature
from classes import LibraryBook

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



@pytest.fixture
def library_1():
    return LibraryBook('Буратино', 'Толстой', 1936)

def test_incorrected_type():
    with pytest.raises(TypeError):
        LibraryBook('1')

def test_rename_title(library_1):
    assert library_1.try_rename('Красная шапочка') == True

def test_failed_rename_title(library_1):
    assert library_1.try_rename('Буратино') == False

def test_get_title(library_1):
    assert library_1.get_title() == 'Буратино'

def test_is_old(library_1):
    assert library_1.is_old(current_year= 2026) == True, "result true"

def test_is_not_old_():
    buk = LibraryBook("Убийство старика на пистоном заводе от удара пустым мешком по голове", 'Неизвестен но популярен', 2012)
    assert buk.is_old(current_year= 2026) == False, "result false"

def test_show_me_age(library_1):
    assert library_1.age(current_year= 2026) == 90, 'result 90'

def test_incorrected_type1(library_1):
    with pytest.raises(TypeError):
        library_1.age('g')

def test_age_zero(library_1):
    with pytest.raises(ValueError):
        library_1.age(current_year= 0)

def test_age_comparison_years(library_1):
    with pytest.raises(ValueError):
        library_1.age(current_year= 1920)

def test_incorrected_is_old(library_1):
    with pytest.raises(TypeError):
        library_1.is_old(current_year= 'hello')

def test_rename_empty_value(library_1):
    assert library_1.try_rename(new_title= '') == False, 'result false'











