from __future__ import annotations


class Temperature:

    __celsius: int

    def __init__(self, celsius: int):
        if not isinstance(celsius, int):
            raise TypeError()

        self.__celsius = celsius


    def get_value(self) -> int:
        return self.__celsius


    def to_fahrenheit(self) -> int | float:
        return (self.__celsius * 1.8) + 32


    def to_kelvin(self) -> int | float:
        return self.__celsius + 273

    def is_positive(self) -> bool:

        if self.__celsius >= 0:
            return True
        else:
            return False

    @staticmethod
    def compare(t1: int|float, t2: int | float) -> int | float:

        if t1 > t2:
            return -1
        elif t1 == t2:
            return 0

        return 1



class LibraryBook:

    __title: str
    __author: str
    __publish_year: int

    def __ini__(self, title: str, author: str, publish_year: int):
        if not isinstance(title, str):  raise TypeError()


        self.__title = title
        self.__author = author
        self.__publish_year = publish_year


    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_publish_year(self) -> int:
        return self.__publish_year











