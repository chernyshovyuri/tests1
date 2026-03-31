from __future__ import annotations


def calculate_sum(n: int | float) -> int | float | None:
    if not isinstance(n, (int, float)):
        raise TypeError()

    if n < 1:
        return None

    start_number = 1


    return (n * (n + start_number)) / 2



def count_words(text: str) -> int | None:
    if not isinstance(text, str):
        raise TypeError()

    if len(text) == 0:
        return None


    counter = 0

    preposition = {'в', 'без', 'до', 'для', 'за', 'из', 'к', 'на', 'над', 'о', 'об', 'обо', 'от', 'по', 'под', 'пред',
                   'при', 'про', 'с', 'у', 'через'}

    new_text: list[str] = text.split()

    for meaning in new_text:
        result = meaning.strip(', . ! ?').lower()
        if result not in preposition:
            counter += 1
    return counter




def is_number(string: str) -> bool:
    if not isinstance(string, str):
        raise TypeError()


    new_string = string.strip(', . - ! ? ')

    if new_string.isdigit():
        return True

    return False


def unique(lst: list[int]) -> list[int] | None:
    if not isinstance(lst, list):
        raise TypeError()

    if len(lst) == 0:
        return None

    for elem in lst:
        if not isinstance(elem, int):
            return None

    new_lst: list[int] = []

    for i in range (len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])

    return new_lst
















