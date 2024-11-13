class Author:
    def __init__(self, name, age, country):
        self.__name = name
        self.__age = age
        self.__country = country

    def write_book(self):
        print(self.__name + " is writing a book.")

    def attend_meeting(self):
        print(self.__name + " is attending a press meeting.")

    def get_details(self):
        return "Author: " + self.__name + ", Age: " + str(self.__age) + ", Country: " + self.__country


class Book:
    def __init__(self, name, isbn, year, price, author):
        self.__name = name
        self.__isbn = isbn
        self.__year = year
        self.__price = price
        self.__author = author  # Author object

    def get_author_details(self):
        return self.__author.get_details()


# Example usage
author1 = Author("Alice Johnson", 45, "USA")
book1 = Book("Python Programming", "123-456-789", 2022, 39.99, author1)

# Retrieve author details through the book
print(book1.get_author_details())

