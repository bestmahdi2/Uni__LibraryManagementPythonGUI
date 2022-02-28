import pytest
from sys import path
from datetime import datetime as Datetime

path.insert(1, '../')
from Code.Book import Book
from Code.Costumer import Costumer
from Code.Receipt_Bill import Receipt, Bill
from Code.Tools import BookState, Tools


class TestCostumer:
    @pytest.fixture
    def setUp(self):
        self.costumer1 = Costumer("Zahra", "Karimi", "zahrakarimi", "1234", "zahrakarimi@gmail.com", "09101234567")
        self.costumer2 = Costumer("Fateme", "Azizi", "fatemeazizi", "4321", "fatemeazizi@gmail.com", "09107654321")

        self.book1 = Book("Me Before You", "Jojo Moyes", BookState.Available)
        self.book2 = Book("Me After You", "Jojo Moyes", BookState.Available)

        self.time1 = Datetime(2020, 5, 5)
        self.time2 = Datetime(2021, 5, 5)
        self.costumer1.borrow_book(self.book1, self.time1)
        self.costumer1.extension_book(self.book1, self.time1, 1)
        self.costumer1.return_book(self.book1, self.time1, self.book1.return_time)

        self.costumer2.borrow_book(self.book2, self.time2, 14)
        self.costumer2.extension_book(self.book2, self.time2, 7)
        self.costumer2.return_book(self.book2, self.time2, Tools.add_time(self.book2.return_time, 14))

    def test_receipt_bill(self, setUp):
        self.receipt1 = Receipt(self.book1, self.costumer1, self.costumer1.returned_books[self.book1]['delay'])
        self.receipt2 = Receipt(self.book2, self.costumer2, self.costumer2.returned_books[self.book2]['delay'])

        self.bill1 = Bill(self.book1, self.costumer1, self.costumer1.returned_books[self.book1]['delay'],
                          self.costumer1.orders[-1]['bill'])
        self.bill2 = Bill(self.book2, self.costumer2, self.costumer2.returned_books[self.book2]['delay'],
                          self.costumer2.orders[-1]['bill'])

        print(self.receipt2)

        assert str(self.receipt1) == "\n".join(["*** Receipt ***", "Costumer:", "Name: Zahra Karimi",
                                                "Email: zahrakarimi@gmail.com",
                                                "\nBook:", 'Name: Me Before You', 'Author: Jojo Moyes', "\nState:",
                                                f'Borrowed Date: {self.time1.strftime("%Y/%m/%d")}',
                                                f'Extension Days: {self.costumer1.returned_books[self.book1]["extension"]}',
                                                f'Returned Date: {Datetime(2020, 5, 13).strftime("%Y/%m/%d")}',
                                                f'Delay: No'])

        assert str(self.receipt2) == "\n".join(["*** Receipt ***", "Costumer:", "Name: Fateme Azizi",
                                                "Email: fatemeazizi@gmail.com",
                                                "\nBook:", 'Name: Me After You', 'Author: Jojo Moyes', "\nState:",
                                                f'Borrowed Date: {self.time2.strftime("%Y/%m/%d")}',
                                                f'Extension Days: {self.costumer2.returned_books[self.book2]["extension"]}',
                                                f'Returned Date: {Datetime(2021, 6, 9).strftime("%Y/%m/%d")}',
                                                f'Delay: 14 days'])

        assert str(self.bill1) == "\n".join(["*** Bill ***", "Costumer:", "Name: Zahra Karimi",
                                             "Email: zahrakarimi@gmail.com",
                                             "\nBook:", 'Name: Me Before You', 'Author: Jojo Moyes', "\nState:",
                                             f'Borrowed Date: {self.time1.strftime("%Y/%m/%d")}',
                                             f'Extension Days: {self.costumer1.returned_books[self.book1]["extension"]}',
                                             f'Returned Date: {Datetime(2020, 5, 13).strftime("%Y/%m/%d")}',
                                             f'Delay: No', f'Payment: 0 $'])

        assert str(self.bill2) == "\n".join(["*** Bill ***", "Costumer:", "Name: Fateme Azizi",
                                             "Email: fatemeazizi@gmail.com",
                                             "\nBook:", 'Name: Me After You', 'Author: Jojo Moyes', "\nState:",
                                             f'Borrowed Date: {self.time2.strftime("%Y/%m/%d")}',
                                             f'Extension Days: {self.costumer2.returned_books[self.book2]["extension"]}',
                                             f'Returned Date: {Datetime(2021, 6, 9).strftime("%Y/%m/%d")}',
                                             f'Delay: 14 days', f'Payment: 49 $'])
