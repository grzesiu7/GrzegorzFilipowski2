# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:57:46 2023

@author: student
"""


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library: {self.city}, {self.street}, {self.zip_code}"
                f"\nOpen hours: {self.open_hours}\nPhone: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}\nHire date: "
                f"{self.hire_date}\nBirth date: {self.birth_date}\n" ) \
               (f"Address: {self.city}, "
                f"{self.street}, {self.zip_code}\nPhone: "
                f"{self.phone}")


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book: {self.author_name} {self.author_surname}\n"
                f"Published: {self.publication_date}\n") \
               f"Pages: {self.number_of_pages}\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"{book}" for book in self.books])
        return (f"Order by {self.employee.first_name} "
                f"{self.employee.last_name} "
                f"for {self.student.first_name} "
                f"{self.student.last_name}\n") \
               f"Order date: {self.order_date}\nBooks:\n{book_list}"


# Tworzenie przykładowych obiektów
library1 = (Library
            ("City1", "Street1", "12345", "9:00 AM - 5:00 PM", "123-456-789"))
library2 = (Library
            ("City2", "Street2", "67890", "10:00 AM - 6:00 PM", "987-654-321"))

employee1 = Employee(
    "Dominika", "Dzida",
    "2023-01-01", "1990-05-15", "City1", "Street1", "12345", "555-111-222")
employee2 = Employee(
    "Michał", "Latosiński",
    "2023-02-01", "1985-08-20", "City2", "Street2", "67890", "111-222-333")

student1 = Student("Grzegorz", "Filipowski")
student2 = Student("Jakub", "Jasiołek")
student3 = Student("Zuzanna", "Czyż")

book1 = Book(library1, "2022-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-01", "Author2", "Surname2", 250)
book3 = Book(library2, "2022-03-01", "Author3", "Surname3", 180)
book4 = Book(library2, "2022-04-01", "Author4", "Surname4", 300)
book5 = Book(library2, "2022-05-01", "Author5", "Surname5", 220)

order1 = Order(employee1, student1, [book1, book2, book3], "2023-03-01")
order2 = Order(employee2, student2, [book4, book5], "2023-03-02")

# Wyświetlanie zamówień
print(order1)
print("\n" + "=" * 50 + "\n")
print(order2)
