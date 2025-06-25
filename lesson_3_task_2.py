from smartphone import Smartphone
catalog = [
    Smartphone("Nokia", "3310", "+7911-111-11-11"),
    Smartphone("Motorola", "RAZR", "+7911-222-22-22"),
    Smartphone("Sony Ericsson", "K500i", "+7911-333-33-33"),
    Smartphone("Siemens", "SX1", "+7911-444-44-44"),
    Smartphone("LG", "Chocolate", "+7911-555-55-55")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")