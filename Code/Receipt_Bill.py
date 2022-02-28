from sys import path

path.insert(1, '../')
from Code.Person import Person
from Code.Lending import Lending


class Receipt:
    """
        This is a class for representing a receipt.

        Attributes:
            book (Lending): The book
            costumer (Person): The costumer whose receipt is for.
            delay (int): The delay of returning book.
    """

    def __init__(self, book: Lending, costumer: Person, delay: int = 0) -> None:
        """
            Constructor function,

            Parameters:
                book (Lending): The book
                costumer (Person): The costumer whose receipt is for.
                delay (int): The delay of returning book.
        """

        self.book = book
        self.costumer = costumer
        self.delay = delay

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        self._book = book

    @property
    def costumer(self):
        return self._costumer

    @costumer.setter
    def costumer(self, costumer):
        self._costumer = costumer

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, delay):
        self._delay = delay

    def __str__(self) -> str:
        """
            function for string returning of class,
        """

        text = ["*** Receipt ***", "Costumer:", f"Name: {self.costumer.first_name} {self.costumer.last_name}",
                f"Email: {self.costumer.email}", "\nBook:", f'Name: {self.book.name}', f'Author: {self.book.author}',
                "\nState:",
                f'Borrowed Date: {self.costumer.returned_books[self.book]["borrowed_time"].strftime("%Y/%m/%d")}',
                f'Extension Days: {self.costumer.returned_books[self.book]["extension"]}',
                f'Returned Date: {self.costumer.returned_books[self.book]["returned_time"].strftime("%Y/%m/%d")}',
                f'Delay: {str(self.delay) + " days" if self.delay else "No"}']

        return "\n".join(text)


class Bill:
    """
        This is a class for representing a bill.

        Attributes:
            book (Lending): The book
            costumer (Person): The costumer whose receipt is for.
            delay (int): The delay of returning book.
            cost (int): The cost of returning book.
    """

    def __init__(self, book: Lending, costumer: Person, delay: int, cost: int) -> None:
        """
            Constructor function,

            Parameters:
                book (Lending): The book
                costumer (Person): The costumer whose receipt is for.
                delay (int): The delay of returning book.
                cost (int): The cost of returning book.
        """

        self.book = book
        self.costumer = costumer
        self.delay = delay
        self.cost = cost

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        self._book = book

    @property
    def costumer(self):
        return self._costumer

    @costumer.setter
    def costumer(self, costumer):
        self._costumer = costumer

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, delay):
        self._delay = delay

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    def __str__(self) -> str:
        """
            function for string returning of class,
        """

        text = ["*** Bill ***", "Costumer:", f"Name: {self.costumer.first_name} {self.costumer.last_name}",
                f"Email: {self.costumer.email}", "\nBook:", f'Name: {self.book.name}',
                f'Author: {self.book.author}', "\nState:",
                f'Borrowed Date: {self.costumer.returned_books[self.book]["borrowed_time"].strftime("%Y/%m/%d")}',
                f'Extension Days: {self.costumer.returned_books[self.book]["extension"]}',
                f'Returned Date: {self.costumer.returned_books[self.book]["returned_time"].strftime("%Y/%m/%d")}',
                f'Delay: {str(self.delay) + " days" if self.delay else "No"}', f'Payment: {self.cost} $']

        return "\n".join(text)
