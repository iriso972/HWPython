from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "3-я ул.Строителей", " 25", "12")
from_addr = Address("322223", "Санкт-Петербург", " 3-я ул.Строителей", "25", "12")

mailing = Mailing(to_addr, from_addr, 386, "AC1231231232")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}"
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},"
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
