from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S2", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 4", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note7", "+79345678901"))
catalog.append(Smartphone("Lenovo", "g4", "+79456789012"))
catalog.append(Smartphone("Huawey", "400", "+79567890123"))

print("Каталог смартфонов:")
print("-" * 30)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

print("-" * 30)
print(f"Всего телефонов в каталоге: {len(catalog)}")
