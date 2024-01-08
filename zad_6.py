# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:28:34 2023

@author: student
"""


def process_lists(list1, list2):
    merged_list = list(set(list1 + list2))
    cubed_list = [x**3 for x in merged_list]
    return cubed_list


# Przykład użycia funkcji
list1 = [6, 3, 3, 1]
list2 = [3, 2, 5, 9]
result = process_lists(list1, list2)
print(result)
