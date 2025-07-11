class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.track} из {self.index}, {self.city}, {self.street}, {self.house}- {self.apartment} в {self.index}, {self.city}, {self.street}, {self.house}- {self.apartment}. Стоимость {self.cost} рублей."