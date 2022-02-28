from sys import path
from re import search
from hashlib import md5

path.insert(1, '../')
from Code.Tools import BookState
from Code.Lending import Lending
from Code.Person import Person
from Code.Receipt_Bill import Receipt, Bill


class Officer:
    """
        This is a class for simulating a officer.

        Attributes:
            first_name (str): The string value of first name
            last_name (str): The string value of last name
            username (str): The string value of username
            password (str): The string value of password
            email (str): The string value of email
            phone (str): The string value of phone
    """

    def __init__(self, first_name: str, last_name: str, username: str, password: str, email: str, phone: str) -> None:
        """
            Constructor function,

            Parameters:
                first_name (str): The string value of first name
                last_name (str): The string value of last name
                username (str): The string value of username
                password (str): The string value of password
                email (str): The string value of email
                phone (str): The string value of phone
        """

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    # region setter getter

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name.title()

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name.title()

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username.lower()

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        # use md5 hashing to hash the password if not hashed yet
        if len(password) == 32:
            self._password = password
        else:
            result = md5(password.encode())
            self._password = result.hexdigest()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        # check the regex of the email to be valid
        regex = '^[A-Za-z0-9._%+-]+[@][A-Za-z0-9.-]+[A-Z|a-z]{2,3}$'

        if search(regex, email):
            self._email = email.lower()

        else:
            self._email = "---"

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        # check the regex of the phone to be valid

        if phone.startswith("0"):
            self._phone = "+98" + phone[1:]

        elif phone.startswith("+98"):
            self._phone = phone

        else:
            self._phone = "---"

    # endregion

    def issue_receipt(self, book: Lending, costumer: Person, delay: int) -> Receipt:
        """
            The function to create a new receipt.

            Parameters:
                book (Lending): The book
                costumer (Person): The costumer
                delay (int): The delay days

            Returns:
                Receipt: a new object of Receipt
        """

        return Receipt(book, costumer, delay)

    def issue_bill(self, book: Lending, costumer: Person, delay: int, cost: int) -> Bill:
        """
            The function to create a new bill.

            Parameters:
                book (Lending): The book
                costumer (Person): The costumer
                delay (int): The delay days
                cost (int): The cost of delay days

            Returns:
                Bill: a new object of Bill
        """

        return Bill(book, costumer, delay, cost)

    def books_status(self, books: list) -> dict:
        """
            The function to get the books.

            Parameters:
                books (list): The list of books

            Returns:
                dict: A new designed way of books
        """

        return {'Available Books': [book for book in books if book.state == BookState.Available],
                'Borrowed Books': [book for book in books if book.state == BookState.Borrowed]}
