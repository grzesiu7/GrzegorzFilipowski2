# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:58:30 2023

@author: grzeg
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property - Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {super().__str__()}, Plot Size: {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()}, Floor: {self.floor}"

# Tworzenie obiektów
house_obj = House(area=150, rooms=4, price=300000, address="ul. Kwiatowa 5", plot=500)
flat_obj = Flat(area=80, rooms=2, price=150000, address="ul. Słoneczna 10", floor=2)

# Wyświetlanie obiektów
print(house_obj)
print(flat_obj)