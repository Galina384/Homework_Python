class Smartphone:
    def __init__(self, brand, model, phone_number):
        """
        Конструктор класса Smartphone

        Args:
            brand (str): Марка телефона
            model (str): Модель телефона
            phone_number (str): Абонентский номер (в формате +79...)
        """
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
