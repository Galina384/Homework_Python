from address import Address


class Mailing:
    """Почтовое отправление"""

    def __init__(
        self,
        to_address: Address,
        from_address: Address,
        cost: float,
        track: str
    ):
        """
        Конструктор

        Args:
            to_address (Address): Адрес получателя
            from_address (Address): Адрес отправителя
            cost (float): Стоимость отправления
            track (str): Трек-номер
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
