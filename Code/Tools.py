from sys import path
from fpdf import FPDF
from enum import Enum
from typing import Union
from datetime import timedelta, datetime as Datetime

##====== while testing ======##

# from Code.Receipt_Bill import Bill, Receipt

##====== while running ======## 

from Receipt_Bill import Bill, Receipt


class CommandState(Enum):
    """
       Enum class for CommandState.
    """

    SameBorrowReturn = "Borrowing date and returning date are the same !"
    BorrowedBefore = "User's trying to borrow a book which already has been borrowed !"
    Done = "Done !"
    MaximumBorrow = "User passed the limit of maximum borrowing !"
    MaximumReserved = "User passed the limit of maximum reserving !"
    NoMoreExtension = "User already used the extension week !"
    ExtensionLimitReached = "User passed the limit of maximum extension days !"
    Bill = "User have a bill to pay !"


class BookState(Enum):
    """
       Enum class for BookState.
    """

    Available = "Available"
    Borrowed = "Borrowed"


class Tools:
    """
       This is a class for helping other classes to use same functions.
    """

    @staticmethod
    def add_time(time: Datetime, days: int) -> Datetime:
        """
        The function to add given days to given datetime.

        Parameters:
            time (Datetime): The time need to be changed.
            days (int): The days need to added to given time.

        Returns:
            Datetime: a Datetime object of added date
        """

        return time + timedelta(days=days)

    @staticmethod
    def find_delay(allowed_date: Datetime, returned_date: Datetime) -> int:
        """
        The function to find delay of two given dates.

        Parameters:
            allowed_date (Datetime): The first date.
            allowed_date (Datetime): The second date.

        Returns:
            days: The days between two dates.
        """

        time = returned_date - allowed_date
        if time.days <= 0:
            return 0
        return time.days

    @staticmethod
    def find_bill(delay: int):
        """
        The function to find bill cost by delay days.

        Parameters:
            delay (int): The delayed days.

        Returns:
            bill: The cost of delayed days.
        """

        if delay <= 0:
            return 0

        elif delay <= 7:
            return 2 * delay

        else:
            return (2 * 7) + (5 * (delay - 7))

    @staticmethod
    def create_pdf(entry: Union[Bill, Receipt]):
        """
        The function to make a new pdf by given entry.

        Parameters:
            entry (Union[Bill, Receipt]): The entry need to be pdf.
        """

        # create pdf, add a page
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", "B", size=25)

        if isinstance(entry, Receipt):  # if it's a receipt
            mode = "Receipt"
            pdf.cell(200, 15, txt="Receipt", ln=1, align='C')
            pdf.set_font("Arial", size=15)

            text = "\n".join(["\nCustomer:", f"Name: {entry.costumer.first_name} {entry.costumer.last_name}",
                              f"Email: {entry.costumer.email}", "\nBook:", f'Name: {entry.book.name}',
                              f'Author: {entry.book.author}', "\nState:",
                              f'Borrowed Date: {entry.costumer.returned_books[entry.book]["borrowed_time"].strftime("%Y/%m/%d")}',
                              f'Extension Days: {entry.costumer.returned_books[entry.book]["extension"]}',
                              f'Returned Date: {entry.costumer.returned_books[entry.book]["returned_time"].strftime("%Y/%m/%d")}',
                              f'Delay: {str(entry.delay) + " days" if entry.delay else "No"}'])

        else:  # if it's a bill
            mode = "Bill"
            pdf.cell(200, 10, txt="Bill", ln=1, align='C')

            text = "\n".join(["\nCustomer:", f"Name: {entry.costumer.first_name} {entry.costumer.last_name}",
                              f"Email: {entry.costumer.email}", "\nBook:", f'Name: {entry.book.name}',
                              f'Author: {entry.book.author}', "\nState:",
                              f'Borrowed Date: {entry.costumer.returned_books[entry.book]["borrowed_time"].strftime("%Y/%m/%d")}',
                              f'Extension Days: {entry.costumer.returned_books[entry.book]["extension"]}',
                              f'Returned Date: {entry.costumer.returned_books[entry.book]["returned_time"].strftime("%Y/%m/%d")}',
                              f'Delay: {str(entry.delay) + " days" if entry.delay else "No"}',
                              f'Payment: {entry.cost} $'])

        for row in text.split('\n'):
            if row in ['Customer:', 'State:', 'Book:']:
                pdf.set_font("Arial", "B", size=17)
                pdf.cell(200, 10, txt=row, ln=1, align='L')
            else:
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt=row, ln=1, align='L')

        # save the pdf
        pdf.output(
            f'{mode}_{entry.costumer.first_name}-{entry.costumer.last_name}[{Datetime.now().strftime("%H.%M.%S")}].pdf')
