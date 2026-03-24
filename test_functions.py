import pytest
from functions import calculate_sum, count_words, is_number, unique


# Проверка на тип данных
# Проверка что n не равна 0
# Проверка что n не отрицательное
# Проверка что n отработал если не целое число
# Проверка если n 1
# Проверка если n 3

def test_calculate_sum_incorrect_type():
    with pytest.raises(TypeError):
        calculate_sum('Hello')

def test_zero_number():
    assert calculate_sum(0) is None, 'Должно быть больше 0'

def test_n_not_negative():
    assert calculate_sum(-1) is None, "Должно быть не отрицательное"

def test_n_type_float():
    assert calculate_sum(5.2) == 16.12,  "Должно быть 16,12"

def test_n_equal_one():
    assert calculate_sum(1) == 1, "Должно быть 1"

def test_n_equal_three():
    assert calculate_sum(3) == 6, 'Должно быть 6'

# 2
# Проверка на тип данных
# Проверка пустая строка
# Проверка на строку из 3 слов
# Проверка на строку из 1 слова
# Проверка из слов пердлогов точек и запятых посередине
# Проверка на капс локе
# проверка на предлоги



def test_count_words_incorrect_tupe():
    with pytest.raises(TypeError):
        count_words(1)

def test_empty_string():
    assert count_words('') is None, 'Если пустая строка None'

def test_line_of_3_words():
    assert count_words('привет пока нормально')  == 3, 'Результат 3'

def test_line_of_1_words():
    assert count_words('привет') == 1, 'Результат 1'

def test_mixed_offer():
    assert count_words('привет на, пока. в? где! кто тут ') == 5, 'Результат 5'

def test_text_upper():
    assert count_words('ПРИВЕТ МИР') == 2, 'Рузультат 2'

def test_preposition():
    assert count_words('в на до за из') == 0, 'Результат 0'

# 3

# Проверка на тип данных
# Проверка на только цифры
# Проверка на буквы
# Проверка на буквы и цыфры
# Проверка на цифры через пробелы запятые
# проверка на отрицательные цифры
# проверка на капслоке буквы и цыфры

def test_is_number_incorrect_type():
    with pytest.raises(TypeError):
        is_number(1)

def test_is_number_is_digits():
    assert is_number('123')  == True, 'answer True'

def test_is_number_to_letters():
    assert is_number('abc')  == False, 'answer False'

def test_is_number_to_mixed():
    assert is_number('a1b2c3') == False, 'answer False'

def test_is_number_to_spaces_and_commas():
    assert is_number('1 2 , 4, 5') == False, 'answer False'

def test_is_numbers_negative_digits():
    assert is_number('-1-3-4') == False, 'answer False'

def test_is_number_upper_letters_and_digits():
    assert is_number('A2B3C7') == False, 'answer False'


#4

# Проверка на тип данных
# Проверка чо список состоит из цифр
# Проверка что список состоит из целых чисел
# Проверка что список состоит только из чисел
# проверка из числа 1
# проверка по повторяющиеся  1 1 1
# проверка из отрицательных чисел

def test_unique_incorrect_type():
    with pytest.raises(TypeError):
        unique('hai')

def test_unique_only_digits():
    assert unique([1,2,3]) == [1,2,3], 'Result [1,2,3]'

def test_unique_only_integers():
    assert unique([1, 1.2, 3]) == None, 'Answer None'

def test_unique_mixed_type():
    assert unique(['1,d,2,h']) == None, 'Answer None'

def test_empty_list():
    assert unique([]) == None, 'Answer None'

def test_one_digit():
    assert unique([1]) == [1], 'Result [1]'

def test_repetitive_1():
    assert unique([1,1,1,1]) == [1], 'Result [1]'

def test_negative_digits():
    assert unique([-1, -2, 4, -5, -5]) == [-1, -2, 4, -5], 'Result [-1, -2, 4, -5]'

















