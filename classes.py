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
        if not isinstance(author, str): raise TypeError()
        if not isinstance(publish_year, int): raise TypeError()


        self.__title = title
        self.__author = author
        self.__publish_year = publish_year


    def get_title(self) -> str:
        return self.__title


    def get_author(self) -> str:
        return self.__author


    def get_publish_year(self) -> int:
        return self.__publish_year


    def __str__(self) -> str:
        return f'Title:{self.__title}\nAuthor:{self.__author}\nPublish Year:{self.__publish_year}'


    def try_rename(self, new_title: str) -> bool:

        if new_title == self.__title:
            return False

        if new_title == '':
            return False

        self.__title = new_title

        return True


    def is_old(self, current_year: int) -> bool:
        if not isinstance(current_year, int):
            raise TypeError()

        if current_year == 0:
            raise ValueError()

        result = current_year - self.get_publish_year()

        if result > 50:
            return True

        return False

    def age(self, current_year: int) -> int | float:
        if not isinstance(current_year, int):
            raise TypeError()

        if current_year == 0:
            raise ValueError()

        if self.__publish_year > current_year:
            raise ValueError()

        result = current_year - self.get_publish_year()

        return result
























