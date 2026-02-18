class Address:
    """Адрес"""

    def __init__(self, index, city, street, house, apartment):
        """
        Конструктор

        Args:
            index (str): Почтовый индекс
            city (str): Город
            street (str): Улица
            house (str): Номер дома
            apartment (str): Номер квартиры
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
