# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:23:02 2023

@author: student
"""

def is_even(number):
    return number % 2 == 0

# Przykład użycia funkcji
num = 8
is_even_result = is_even(num)

if is_even_result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")