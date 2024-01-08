# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:04:28 2023

@author: grzeg
"""

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}\nOpen hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\nLocation: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublished on: {self.publication_date}\nPages: {self.number_of_pages}\nLibrary: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"   - {book}" for book in self.books])
        return f"Order details:\nEmployee: {self.employee}\nStudent: {self.student}\nBooks:\n{book_list}\nOrder date: {self.order_date}"


# Stworzenie instancji klas
library1 = Library("City1", "Street1", "12345", "9 AM - 5 PM", "123-456-789")
library2 = Library("City2", "Street2", "54321", "10 AM - 6 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", "111-222-333")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "City2", "Street2", "54321", "444-555-666")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-10", "City1", "Street1", "12345", "777-888-999")

book1 = Book(library1, "2020-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2021-02-01", "Author2", "Surname2", 250)
book3 = Book(library2, "2019-03-01", "Author3", "Surname3", 180)
book4 = Book(library2, "2020-04-01", "Author4", "Surname4", 300)
book5 = Book(library1, "2022-05-01", "Author5", "Surname5", 150)

order1 = Order(employee1, "Student1", [book1, book2, book3], "2022-06-01")
order2 = Order(employee2, "Student2", [book4, book5], "2022-06-02")

# Wyświetlenie zamówień
print(order1)
print("\n" + "-"*50 + "\n")
print(order2)
