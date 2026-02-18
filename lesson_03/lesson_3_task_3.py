from address import Address
from mailing import Mailing

mailing = Mailing(
    to_address=Address(
        "614112", "Пермь", "Карбышева", "88", "101"
    ),
    from_address=Address(
        "693005", "Южно-Сахалинск", "Спутник-2", "7", "1"
    ),
    cost=5623.8,
    track="RU123456789CN"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
