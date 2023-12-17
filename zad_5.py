# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:26:26 2023

@author: student
"""

def does_list_contain_value(input_list, value):
    return value in input_list

# Przykład użycia funkcji
my_list = [11, 22, 7, 2, 5, 1]
value_to_check = 5
result = does_list_contain_value(my_list, value_to_check)
print(result)
