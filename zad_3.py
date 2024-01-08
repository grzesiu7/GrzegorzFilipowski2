# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:18:16 2024

@author: grzeg
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} metrów kwadratowych, {self.rooms} pokoje\nPrice: {self.price} PLN\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}\nPlot size: {self.plot} metrów"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat\n{super().__str__()}\nFloor: {self.floor}"


# Stworzenie obiektu klasy House
house1 = House(area=200, rooms=5, price=300000, address="ulica1", plot=500)

# Stworzenie obiektu klasy Flat
flat1 = Flat(area=80, rooms=3, price=150000, address="ulica2", floor=2)

# Wyświetlenie obiektów
print(house1)
print("\n" + "-"*50 + "\n")
print(flat1)
