class Book:
    """ Базовый класс книги. """

    __name = None
    __author = None

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"РљРЅРёРіР° {self.name}. РђРІС‚РѕСЂ {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        if isinstance(pages, str): raise TypeError
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return (super().__str__() + f", количество страниц {self.pages}")


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        if isinstance(duration, float): raise TypeError
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return (super().__str__() + f", продолжительность {self.duration}")

a = PaperBook("asd", "koio", 1)
print(a.__str__())