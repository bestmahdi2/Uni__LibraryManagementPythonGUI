import pytest
from sys import path
from hashlib import md5
from datetime import datetime as Datetime

path.insert(1, '../')
from Code.Book import Book
from Code.Costumer import Costumer
from Code.Officer import Officer
from Code.Tools import BookState, CommandState, Tools


class TestOfficer:
    @pytest.fixture
    def setUp(self):
        self.book1 = Book("Me Before you", "Jojo Moyes", BookState.Available)
        self.book2 = Book("Me After you", "Jojo Moyes", BookState.Borrowed)

        self.officer1 = Officer("zahra", "Karimi", "ZAHRAkarimi", "1234", "zahrakarimi@Gmail.Com", "09101234567")
        self.officer2 = Officer("Fateme", "azizi", "fatemeazizi", "4321", "Fatemeazizi#gmail.com", "+5369745")

        self.officer = Officer("Ali", "Mohammadi", "alimohammadi", '1234', 'alimohammadi@gmail.com', "0910765431")

    def test_names(self, setUp):
        assert self.officer1.first_name == "Zahra"
        assert self.officer1.last_name == "Karimi"

        assert self.officer2.first_name == "Fateme"
        assert self.officer2.last_name == "Azizi"

    def test_credintial(self, setUp):
        assert self.officer1.username == "zahrakarimi"
        assert self.officer1.password == md5("1234".encode()).hexdigest()
        assert self.officer1.email == "zahrakarimi@gmail.com"
        assert self.officer1.phone == "+989101234567"

        assert self.officer2.username == "fatemeazizi"
        assert self.officer2.password == md5("4321".encode()).hexdigest()
        assert self.officer2.email == "---"
        assert self.officer2.phone == "---"

    def test_books_status(self, setUp):
        assert self.officer1.books_status([self.book1, self.book2]) == {'Available Books': [self.book1],
         'Borrowed Books': [self.book2]}
