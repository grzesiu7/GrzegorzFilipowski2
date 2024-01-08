# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:28:04 2023

@author: grzeg
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50
    
Student1 = Student("Tomek",[10,20,30])
Student2 = Student("Basia",[30,90,80])    

wynik1 = Student1.is_passed()       
print(f"Czy {Student1.name} zdał/a {wynik1}")

wynik2 = Student2.is_passed()       
print(f"Czy {Student2.name} zdał/a {wynik2}")                
                 