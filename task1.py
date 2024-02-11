class Cars:
    def __init__(self, name: str, country: str, year_of_release: int):
        """
            Создание и подготовка к работе обекта "автомобиль"
            :param name: имя автомобиля
            :param country: страна произведения
            :param year_of_release: год выпуска
        """
        self._name = name
        self.country = country
        self._year_of_release = year_of_release

    @property
    def name(self):
        return self._name

    @property
    def year_of_release(self):
        return self._year_of_release

    @year_of_release.setter
    def year_of_release(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError
        elif new_year <= 0:
            raise ValueError
        else:
            self._year_of_release = new_year

    def __str__(self):
        """
        Функция печатает характеристики автомобиля
        :return: строки характеристик автомобиля
        """
        return f"Автомобиль - {self.name}; Страна производителя -{self.country}; год выпуска - {self.year_of_release}"

    def __repr__(self):
        """
        Функция печатает характеристики автомобиля
        :return: класс(...)
        """
        return f"{self.__class__.__name__}(name = {self.name!r}, country = {self.country!r}"\
            f"year_of_release = {self.year_of_release})"


class Truck(Cars):
    """Автомобиль: грузовой автомобиль"""
    def __init__(self, name: str, country: str, year_of_release: int, weight: float, height: float):
        """
            Создание и подготовка к работе обекта "грузовой автомобиль"
            :param name: имя автомобиля
            :param country: страна произведения
            :param year_of_release: год выпуска
            :param weight: вес грузового автомобиля
            :param height: высота грузового автомобиля

        """

        super().__init__(name, country, year_of_release)
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if not isinstance(new_weight, float):
            raise TypeError
        elif new_weight <= 0:
            raise ValueError
        else:
            self._weight = new_weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, float):
            raise TypeError
        elif new_height <= 0:
            raise ValueError
        else:
            self._height = new_height

    def __str__(self):
        """
        Функция печатает характеристики автомобиля
        :return: строки характеристик автомобиля
        """

        return f"{super().__str__()} Вес - {self._weight} Высота - {self._height}"

    def __repr__(self):
        """
        Функция печатает характеристики автомобиля
        :return: строки характеристик автомобиля
        """

        return f"{self.__class__.__name__}(name = {self.name!r}, country = {self.country!r}"\
            f"year_of_release = {self.year_of_release}, weight = {self.weight}, height = {self.height})"


if __name__ == "__main__":
    # Write your solution here
    pass
