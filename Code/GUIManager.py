from re import search
from time import sleep
from hashlib import md5
from typing import Union
from sys import path, argv, exit

from PyQt5.QtCore import Qt
from sqlite3 import connect
from functools import partial
from PyQt5.QtGui import QPixmap
from datetime import datetime as Datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QTableWidget, QComboBox, QListWidget, QTextBrowser, QListWidgetItem, QMainWindow, \
    QDialog

##====== while testing ======##

# from Code.Lending import Lending

# path.insert(1, '../')
# from Code.Book import Book
# from Code.Person import Person
# from Code.Officer import Officer
# from Code.Costumer import Costumer
# from Code.Receipt_Bill import Receipt, Bill
# from Code.Tools import BookState, Tools, CommandState

##====== while running ======## 

from Lending import Lending

from Book import Book
from Person import Person
from Officer import Officer
from Costumer import Costumer
from Receipt_Bill import Receipt, Bill
from Tools import BookState, Tools, CommandState
path.insert(1, '../')

from GUI.Signin_gui import Ui_SignInWindow
from GUI.Signup_gui import Ui_SignUpWindow
from GUI.officer_gui import Ui_OfficerWindow
from GUI.costumer_gui import Ui_CostumerWindow

# Hidpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# use Hidpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class GUI(Ui_SignInWindow):
    """
       This is a class for creating the gui.
       """

    def __init__(self):
        """
            Constructor function,

            self.officers_costumers: to keep costumers and officers
            self.books: to keep books
            self.partition: to keep the partition window
            self.user: to keep the signed in user
            self.requests: to keep the requests of costumers
        """

        super().__init__()
        self.officers_costumers = {"costumer": [], "officer": []}
        self.books = []
        self.partition = None
        self.user = None
        self.requests = {}

    def setupUi(self, MainWindow):
        """CMS_UI parent class function"""

        super().setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        """CMS_UI parent class function"""

        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate

    def add_book(self, name: str, author: str, state: BookState = BookState.Available):
        """
            The function to add new a book

            Parameters:
                name (str): The string value of book's name
                author (str): The string value of book's author
                state (str): The string value of book's state
        """

        self.books.append(Book(name, author, state))

    def main(self) -> None:
        """
            Main function, read the sqlite file and set the logo for main page (sign in)
        """
        self.officers_costumers = {"costumer": [], "officer": []}
        self.books = []
        self.requests = {}

        self.officers_costumers["costumer"].append(
            Costumer("Azar", "Hajipuor", "azarhajipour", "1234", "azarhajipour@Gmail.Com", "09111234567"))

        self.officers_costumers["officer"].append(
            Officer("Mahdi", "Hajipuor", "mahdihajipour", "4321", "mahdihajipour@gmail.com", "09117654321"))

        self.user = self.officers_costumers["costumer"][0]
        self.requests[self.user] = []

        self.readSqlite()
        self.set_logo(self.label_logo, MainWindow)

    def open_sign_up(self):
        """
            Function to open the sign up window and hide the sign in windows,
            it creates a new dialog and set it to gui designed for sign_up,
            then sets the logo and connect the push button to sign_up function.
        """

        MainWindow.hide()
        self.set_error(self.label_error)
        self.empty_boxes('signin')

        self.signup_app = QtWidgets.QDialog()

        self.signup = Ui_SignUpWindow()
        self.signup.setupUi(self.signup_app)

        self.signup.pushButton_Signup.clicked.connect(self.sign_up)

        self.set_logo(self.signup.label_logo, self.signup_app)
        self.signup_app.closeEvent = self.not_main_closeEvent
        self.signup_app.show()
        self.signup_app.exec_()

    def sign_up(self):
        """
            Function to check the sign up credential and sign up a new user if they're fine,
            it change the error label if there is a problem, and if successful reached,
            it will hide this window and open the sign in window in waiting of 1 second with uses of
            the multithreading.
        """

        self.set_error(self.signup.label_error, "")

        regex = '^[A-Za-z0-9._%+-]+[@][A-Za-z0-9.-]+[A-Z|a-z]{2,3}$'
        all = [i.username for i in list(self.officers_costumers['costumer'] + self.officers_costumers['officer'])]

        username = self.signup.lineEdit_username.text().lower()
        password = self.signup.lineEdit_password.text()
        password_2 = self.signup.lineEdit_password_2.text()
        fullname = self.signup.lineEdit_full_name.text()
        email = self.signup.lineEdit_email.text()
        phone = self.signup.lineEdit_phone.text()

        if not username:
            self.set_error(self.signup.label_error, "Username is empty !")
            return

        elif username in all:
            self.set_error(self.signup.label_error, "Username is already used !")
            return

        elif not password or not password_2:
            self.set_error(self.signup.label_error, "Password is empty !")
            return

        elif not fullname:
            self.set_error(self.signup.label_error, "Name is empty !")
            return

        elif password != password_2:
            self.set_error(self.signup.label_error, "Passwords are not matching !")
            return

        elif email and not search(regex, email):
            self.set_error(self.signup.label_error, "Entered email is not valid !")
            return

        first_name = fullname.split(" ")[0]
        last_name = fullname.replace(first_name, "", 1)
        self.officers_costumers["costumer"].append(Costumer(first_name, last_name, username, password, email, phone))

        self.set_error(self.signup.label_error, "Signing up ...", 'green')
        QtWidgets.QApplication.processEvents()
        sleep(1)

        self.signup_app.close()

    def sign_in(self):
        """
            Function to check the sign in credential and sign in the new user if they're fine.
        """

        self.set_error(self.label_error, "")

        username_email = self.lineEdit_username_email.text().lower()
        # hashed password
        password = md5(self.lineEdit_password.text().encode()).hexdigest()

        if not username_email:
            self.set_error(self.label_error, "Username/Email address is empty !")
            return

        elif not self.lineEdit_password.text():
            self.set_error(self.label_error, "Password is empty !")
            return

        all = self.officers_costumers['costumer'] + self.officers_costumers['officer']

        for entrance in all:  # if user entered username
            if entrance.username == username_email and entrance.password == password:
                self.set_error(self.label_error, "Signing in ...", 'green')
                self.user = entrance
                QtWidgets.QApplication.processEvents()
                sleep(1)
                break
            # if user entered email
            elif entrance.email == username_email and entrance.password == password:
                self.set_error(self.label_error, "Signing in ...", 'green')
                self.user = entrance
                QtWidgets.QApplication.processEvents()
                sleep(1)
                break
        else:
            self.set_error(self.label_error, "Username/Email address or password incorrect !")
            return

        if self.user not in self.requests:
            self.requests[self.user] = []
        self.open_partition()

    def open_partition(self):
        """
            Function to checks if the person is officer or costumer and opens the appropriate partition window
            and sets the connection between objects and functions.
        """

        MainWindow.hide()
        self.set_error(self.label_error)
        self.empty_boxes('signin')

        partition_app = QtWidgets.QDialog()

        if self.user in self.officers_costumers['costumer']:  # if it's a costumer
            self.partition = Ui_CostumerWindow()
            self.partition.setupUi(partition_app)

            # fill the list with list of actions of the costumer
            self.fill_list(self.partition.listWidget, 'costumer')

            # fill the table of my_books with borrowed or returned books
            self.fill_table(self.partition.tableWidget_my_books, 'my_books')

            # if an item selected from table of my books, decide to show or hide "return" and "add days" buttons
            self.partition.tableWidget_my_books.itemSelectionChanged.connect(self.my_books_table_select)

            # connect the push buttons to their functions
            self.partition.pushButton_reserve.clicked.connect(partial(self.costumer_request1, 'reserve'))
            self.partition.pushButton_borrow.clicked.connect(partial(self.costumer_request1, 'borrow'))
            self.partition.pushButton_add_days.clicked.connect(partial(self.costumer_request2, 'extension'))
            self.partition.pushButton_return.clicked.connect(partial(self.costumer_request2, 'return'))

            self.partition.tabWidget.currentChanged.connect(partial(self.SwitchTab, 'costumer'))
            self.partition.listWidget.currentItemChanged.connect(
                partial(self.fill_description, self.partition.textBrowser, 'costumer'))

        else:  # if it's a officer
            self.partition = Ui_OfficerWindow()
            self.partition.setupUi(partition_app)

            # fill the list with list of actions of all costumer
            self.fill_list(self.partition.listWidget, 'officer')

            # connect the push buttons to their functions
            self.partition.pushButton_confirm.clicked.connect(partial(self.officer_confirm, True))
            self.partition.pushButton_deny.clicked.connect(partial(self.officer_confirm, False))
            self.partition.pushButton_issue_receipt.clicked.connect(partial(self.issue_rb, 'receipt'))
            self.partition.pushButton_issue_bill.clicked.connect(partial(self.issue_rb, 'bill'))

            self.partition.pushButton_create_officer.clicked.connect(self.add_officer)

            self.partition.pushButton_issue_receipt.hide()
            self.partition.pushButton_issue_bill.hide()
            self.partition.tabWidget.currentChanged.connect(partial(self.SwitchTab, 'officer'))
            self.partition.listWidget.currentItemChanged.connect(
                partial(self.fill_description, self.partition.textBrowser, 'officer'))

        # fill the books table with books
        self.fill_table(self.partition.tableWidget_books, 'books', self.partition.comboBox_books)

        self.partition.comboBox_books.currentIndexChanged.connect(
            partial(self.fill_table, self.partition.tableWidget_books, 'books', self.partition.comboBox_books))

        partition_app.closeEvent = self.not_main_closeEvent
        self.set_logo(self.partition.label_logo, partition_app)
        partition_app.show()
        partition_app.exec_()

    def set_logo(self, object: QLabel, main_window: Union[QMainWindow, QDialog]):
        """
            The function to set logo and icon of the window

            Parameters:
                object (QLabel): The label should have the logo
                main_window (Union[QMainWindow, QDialog]): The window should have the icon
        """

        # logo
        pixmap = QPixmap('logo64.png')
        object.setPixmap(pixmap)

        # icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        main_window.setWindowIcon(icon)

    def set_error(self, object: QLabel, text: str = "", color: str = "red"):
        """
            The function to set text to given error labels

            Parameters:
                object (QLabel): The label should its text be changed
                text (str): The text the label should have now
                color (str): The color of the label's text
        """

        if color == "red":
            object.setStyleSheet("background-color:#F6F8FA;color:#FC0000")

        else:
            object.setStyleSheet("background-color:#F6F8FA;color:#50C878")

        object.setText(text)

    def empty_boxes(self, window: str):
        """
            The function to clear the text in line edits

            Parameters:
                window (str): The name of partition which it's labels should be empty
        """

        if window == "signin":
            self.lineEdit_username_email.setText("")
            self.lineEdit_password.setText("")

        elif window == "officer":
            self.partition.lineEdit_username.setText("")
            self.partition.lineEdit_password.setText("")
            self.partition.lineEdit_password_2.setText("")
            self.partition.lineEdit_full_name.setText("")
            self.partition.lineEdit_email.setText("")
            self.partition.lineEdit_phone.setText("")

    def my_books_table_select(self):
        """
            The function to show or hide the 'return' and 'add days' buttons,

            if checks if the item selected is borrowed, if will show these two buttons,
            if not it will hide them.
        """

        index = self.partition.tableWidget_my_books.currentRow()
        if index > -1:
            self.partition.spinBox.setValue(int(self.partition.tableWidget_my_books.item(index, 4).text()))

            if self.partition.tableWidget_my_books.item(index, 1).text() == "Borrowed":
                self.partition.pushButton_return.show()
                self.partition.pushButton_add_days.show()

            else:
                self.partition.pushButton_return.hide()
                self.partition.pushButton_add_days.hide()

    def not_main_closeEvent(self, event):
        """ The function which any window (except sign_in) will run when it's closed. """

        MainWindow.show()

    def closeEvent(self, event) -> None:
        """This function enables when user close the main window (sing_in window)"""

        self.saveSqlite()

    def fill_table(self, table: QTableWidget, mode: str, comboBox: QComboBox = "") -> None:
        """
            The function to fill the given table with modes or comboBox.

            Parameters:
                table (QTableWidget): The table that should be filled by items
                mode (str): The mode of being filled
                comboBox (QComboBox): The combobox which uses when filling the books table
        """

        if mode == "books":
            table.setRowCount(0)

            if comboBox.currentIndex() == 0:  # if combobox is selected the 'Available'
                if hasattr(self.partition, 'pushButton_reserve') and hasattr(self.partition, 'pushButton_borrow'):
                    self.partition.pushButton_reserve.show()
                    self.partition.pushButton_borrow.show()

                books = [book for book in self.books if
                         book.state == BookState.Available and not book.reserved.first_name]

                if books:
                    x = 0
                    while x < len(books):
                        table.insertRow(x)
                        table.setItem(x, 0, QtWidgets.QTableWidgetItem(books[x].name))
                        table.setItem(x, 1, QtWidgets.QTableWidgetItem(books[x].author))
                        table.setItem(x, 2, QtWidgets.QTableWidgetItem("Available"))
                        table.setItem(x, 3,
                                      QtWidgets.QTableWidgetItem("Yes" if books[x].reserved.first_name else "No"))
                        table.setItem(x, 4, QtWidgets.QTableWidgetItem("No"))
                        table.setItem(x, 5, QtWidgets.QTableWidgetItem("---"))
                        table.setItem(x, 6, QtWidgets.QTableWidgetItem("---"))
                        x += 1

            elif comboBox.currentIndex() == 1:  # if combobox is selected the 'Borrowed'
                if hasattr(self.partition, 'pushButton_reserve') and hasattr(self.partition, 'pushButton_borrow'):
                    self.partition.pushButton_reserve.show()
                    self.partition.pushButton_borrow.hide()

                books = [book for book in self.books if book.state == BookState.Borrowed]

                if books:
                    x = 0
                    while x < len(books):
                        table.insertRow(x)
                        table.setItem(x, 0, QtWidgets.QTableWidgetItem(books[x].name))
                        table.setItem(x, 1, QtWidgets.QTableWidgetItem(books[x].author))
                        table.setItem(x, 2, QtWidgets.QTableWidgetItem("Borrowed"))
                        table.setItem(x, 3,
                                      QtWidgets.QTableWidgetItem("Yes" if books[x].reserved.first_name else "No"))
                        table.setItem(x, 4, QtWidgets.QTableWidgetItem("Yes"))
                        table.setItem(x, 5,
                                      QtWidgets.QTableWidgetItem(books[x].borrowed_time.strftime("%Y/%m/%d")))
                        table.setItem(x, 6,
                                      QtWidgets.QTableWidgetItem(books[x].return_time.strftime("%Y/%m/%d")))
                        x += 1

            else:  # if combobox is selected the 'Reserved'
                if hasattr(self.partition, 'pushButton_reserve') and hasattr(self.partition, 'pushButton_borrow'):
                    self.partition.pushButton_reserve.hide()
                    self.partition.pushButton_borrow.hide()

                books = [book for book in self.books if book.reserved.first_name]

                if books:
                    x = 0
                    while x < len(books):
                        table.insertRow(x)
                        table.setItem(x, 0, QtWidgets.QTableWidgetItem(books[x].name))
                        table.setItem(x, 1, QtWidgets.QTableWidgetItem(books[x].author))
                        table.setItem(x, 2, QtWidgets.QTableWidgetItem("Reserved"))
                        table.setItem(x, 3,
                                      QtWidgets.QTableWidgetItem("Yes" if books[x].reserved.first_name else "No"))
                        if not books[x].borrowed.first_name:
                            table.setItem(x, 4, QtWidgets.QTableWidgetItem("No"))
                            table.setItem(x, 5, QtWidgets.QTableWidgetItem("---"))
                            table.setItem(x, 6, QtWidgets.QTableWidgetItem("---"))
                        else:
                            table.setItem(x, 4, QtWidgets.QTableWidgetItem("Yes"))
                            table.setItem(x, 5, QtWidgets.QTableWidgetItem(
                                books[x].borrowed_time.strftime("%Y/%m/%d")))
                            table.setItem(x, 6,
                                          QtWidgets.QTableWidgetItem(
                                              books[x].return_time.strftime("%Y/%m/%d")))

                        x += 1

        elif mode == 'my_books':
            table.setRowCount(0)

            borrowed_books = [book for book in self.user.borrowed_books.keys()]
            returned_books = [book for book in self.user.returned_books.keys()]

            x = 0
            if borrowed_books:  # fill the table first with borrowed books,
                while x < len(borrowed_books):
                    delay = Tools.find_delay(borrowed_books[x].return_time, Datetime.now())
                    bill = Tools.find_bill(delay)

                    table.insertRow(x)
                    table.setItem(x, 0, QtWidgets.QTableWidgetItem(borrowed_books[x].name))
                    table.setItem(x, 1, QtWidgets.QTableWidgetItem("Borrowed"))
                    table.setItem(x, 2,
                                  QtWidgets.QTableWidgetItem(borrowed_books[x].borrowed_time.strftime("%Y/%m/%d")))
                    table.setItem(x, 3, QtWidgets.QTableWidgetItem(borrowed_books[x].return_time.strftime("%Y/%m/%d")))
                    table.setItem(x, 4, QtWidgets.QTableWidgetItem(
                        str(self.user.borrowed_books[borrowed_books[x]]['extension'])))
                    table.setItem(x, 5, QtWidgets.QTableWidgetItem(str(delay)))
                    table.setItem(x, 6, QtWidgets.QTableWidgetItem(str(bill)))
                    x += 1

            y = 0
            if returned_books:  # then fill the table with returned books,
                while y < len(returned_books):
                    delay = self.user.returned_books[returned_books[y]]['delay']
                    bill = Tools.find_bill(delay)

                    table.insertRow(y + x)
                    table.setItem(y + x, 0, QtWidgets.QTableWidgetItem(returned_books[y].name))
                    table.setItem(y + x, 1, QtWidgets.QTableWidgetItem("Returned"))
                    table.setItem(y + x, 2, QtWidgets.QTableWidgetItem(
                        self.user.returned_books[returned_books[y]]['borrowed_time'].strftime("%Y/%m/%d")))
                    table.setItem(y + x, 3, QtWidgets.QTableWidgetItem(
                        self.user.returned_books[returned_books[y]]['returned_time'].strftime("%Y/%m/%d")))
                    table.setItem(y + x, 4, QtWidgets.QTableWidgetItem(
                        str(self.user.returned_books[returned_books[y]]['extension'])))
                    table.setItem(y + x, 5, QtWidgets.QTableWidgetItem(str(delay)))
                    table.setItem(y + x, 6, QtWidgets.QTableWidgetItem(str(bill)))
                    y += 1

    def fill_list(self, list_: QListWidget, mode: str) -> None:
        """
            The function to fill the given list with modes.

            Parameters:
                list_ (QListWidget): The list that should be filled by items
                mode (str): The mode of being filled
        """

        # clear the list
        list_.clear()

        emoji = {"Not Accepted": "❔", "Accepted": "✅", "Denied": "❌"}  # emoji keeper

        if mode == "costumer":
            if self.requests:
                items = [
                    f'{i["request"].title()}) {i["book"].name} => {i["accepted"]}'
                    for i in self.requests[self.user]]
                for item_ in items:
                    item = QListWidgetItem(item_)

                    if item_.endswith("Not Accepted"):
                        item.setForeground(Qt.blue)

                    elif item_.endswith("Accepted"):
                        item.setForeground(Qt.darkGreen)

                    else:
                        item.setForeground(Qt.red)

                    list_.addItem(item)

        else:  # if mode is officer
            self.partition.pushButton_issue_receipt.hide()
            self.partition.pushButton_issue_bill.hide()

            self.list_ = []
            if self.requests:
                for user in self.requests.keys():
                    items = [
                        f'{emoji[i["accepted"]]} {i["request"].title()}) {i["book"].name} => {user.first_name} {user.last_name}'
                        for i in self.requests[user]]
                    list_.addItems(items)
                    self.list_ += items

    def fill_description(self, textBrowser: QTextBrowser, mode: str):
        """
            The function to fill the description of selected item in lists.

            Parameters:
                textBrowser (QTextBrowser): The text browser object to be filled with text.
                mode (str): The mode of being filled
        """

        if mode == "costumer":
            index = self.partition.listWidget.row(self.partition.listWidget.currentItem())
            info = self.requests[self.user][index]

            text = [f'{key.title()}: {info[key]}' for key in info.keys()]

            textBrowser.setText("\n".join(text).replace("Book: ", "Book:\n").title())

        else:  # if mode is officer
            index = self.partition.listWidget.row(self.partition.listWidget.currentItem())

            if index == -1:
                return

            x, user = 0, 0
            for user_ in self.requests.keys():
                x += len(self.requests[user_])
                if x > index:
                    user = user_
                    break

            index = -1
            for i in self.list_:
                if i.endswith(f'{user.first_name} {user.last_name}'):
                    index += 1

                if i == self.partition.listWidget.currentItem().text():
                    break

            info = self.requests[user][index]

            # show or hide the 'issue receipt' or 'issue bill' buttons if the selected item is returned book or not.
            if info['request'] == "return":
                self.partition.pushButton_issue_receipt.show()
                self.partition.pushButton_issue_bill.show()

            else:
                self.partition.pushButton_issue_receipt.hide()
                self.partition.pushButton_issue_bill.hide()

            text = [f'{key.title()}: {info[key]}' for key in info.keys()]

            textBrowser.setText("\n".join(text).replace("Book: ", "Book:\n").title())

    def costumer_request1(self, mode):
        """
            The function to handle request of costumer,
            in 'tableWidget_books' and modes 'reserve' and 'borrow'

            Parameters:
                mode (str): The mode of request
        """

        # remove older request if requests is more than 10
        if len(self.requests[self.user]) >= 10:
            self.requests[self.user] = self.requests[self.user][1:]
            self.set_error(self.partition.label_error_3, "Old requests removed !")

        index = self.partition.tableWidget_books.currentRow()

        if index == -1:  # if item not selected in table
            self.set_error(self.partition.label_error, "Please select a book from table !")
            return

        book = [i for i in self.books if i.name == self.partition.tableWidget_books.item(index, 0).text()][0]

        if mode == 'reserve':
            if book.reserved.first_name:
                self.set_error(self.partition.label_error, "This book is already reserved !")

            elif book.reserved.first_name is None and book.borrowed.first_name is None:
                self.set_error(self.partition.label_error, "You can borrow this book !")

            elif len(self.user.reserve) == 3:
                self.set_error(self.partition.label_error, "You can't reserve any new book !")

            else:
                self.set_error(self.partition.label_error, "Sent request to officer !", 'green')
                self.request_adder(mode, book)  # add a request for officer to respond

        elif mode == 'borrow':
            if len(self.user.borrowed_books) == 3:
                self.set_error(self.partition.label_error, "You can't borrow any new book !")

            else:
                self.set_error(self.partition.label_error, "Sent request to officer !", 'green')
                self.request_adder(mode, book)  # add a request for officer to respond

    def costumer_request2(self, mode):
        """
            The function to handle request of costumer,
            in 'tableWidget_my_books' and modes 'extension' and 'return'

            Parameters:
                mode (str): The mode of request
        """

        index = self.partition.tableWidget_my_books.currentRow()

        if index == -1:
            self.set_error(self.partition.label_error_2, "Please select a book from table !")
            return

        book = [i for i in self.books if i.name == self.partition.tableWidget_my_books.item(index, 0).text()][0]

        if mode == 'extension':
            current = int(self.partition.tableWidget_my_books.item(index, 4).text())
            if self.partition.spinBox.value() <= current:
                self.set_error(self.partition.label_error_2, f"Extension days can't be equal/less than {current} !")

            else:
                self.set_error(self.partition.label_error_2, "Sent request to officer !", 'green')
                self.request_adder(mode, book, extension=self.partition.spinBox.value())

        elif mode == 'return':
            self.set_error(self.partition.label_error_2, "Sent request to officer !", 'green')
            self.request_adder(mode, book)

    def request_adder(self, request: str, book: Lending, date: str = Datetime.now().strftime("%Y/%m/%d"),
                      accepted: str = 'Not Accepted', extension: int = 0):
        """
            The function to add a new request to

            Parameters:
                request (str): The string value of the request
                book (Lending): The book object request made for
                date (str): The date of the request
                accepted (str): The acceptation of the request (default is Not Accepted)
                extension (int): The int value of extension days if it does
        """

        for req in self.requests[self.user]:
            if req['request'] == request and req['book'] == book and req['accepted'] == accepted:
                return
        else:
            if extension:
                self.requests[self.user].append({"request": request, 'book': book, 'date': date, 'accepted': accepted,
                                                 "extension": extension})
            else:
                self.requests[self.user].append({"request": request, 'book': book, 'date': date, 'accepted': accepted})

    def officer_confirm(self, accept: bool = True):
        """
            The function to add a new request to

            Parameters:
                accept (bool): The boolean value of action officer performed on a request
        """

        index = self.partition.listWidget.row(self.partition.listWidget.currentItem())

        x, user = 0, ""  # find the user
        for user_ in self.requests.keys():
            x += len(self.requests[user_])
            if x > index:
                user = user_
                break

        # find the user's information
        index = -1
        for i in self.list_:
            if i.endswith(f'{user.first_name} {user.last_name}'):
                index += 1

            if i == self.partition.listWidget.currentItem().text():
                break

        info = self.requests[user][index]

        print(self.requests[user])
        if self.requests[user][index]['accepted'] != "Not Accepted":  # don't handle the handled request
            self.set_error(self.partition.label_error, "This request is already handled !")
            return


        if isinstance(info['date'], Datetime): # find date
            time = info['date']

        else:
            time = Datetime.strptime(info['date'], "%Y/%m/%d")



        self.set_error(self.partition.label_error)

        if accept:  # if accept button clicked
            if info['request'] == "borrow":
                borrow = user.borrow_book(info['book'], time)
                if borrow == CommandState.Done:
                    self.requests[user][index]['accepted'] = "Accepted"
                    self.set_error(self.partition.label_error, "User request accepted !", 'green')

                elif borrow == CommandState.BorrowedBefore:
                    self.set_error(self.partition.label_error, "User already borrowed this book !")

                elif borrow == CommandState.MaximumBorrow:
                    self.set_error(self.partition.label_error, "User's maximum borrowed books reached !")

            elif info['request'] == "reserve":
                reserve = user.reserve_book(info['book'], time)

                if reserve == CommandState.Done:
                    self.requests[user][index]['accepted'] = "Accepted"
                    self.set_error(self.partition.label_error, "User request accepted !", 'green')

                elif reserve == CommandState.MaximumReserved:
                    self.set_error(self.partition.label_error, "User's maximum reserved books reached !")

            elif info['request'] == "extension":
                try:
                    extension = user.extension_book(info['book'], time, info['extension'])
                except:
                    self.set_error(self.partition.label_error, "User doesn't have the book !")
                    return

                if extension == CommandState.Done:
                    self.requests[user][index]['accepted'] = "Accepted"
                    self.set_error(self.partition.label_error, "User request accepted !", 'green')

                elif extension == CommandState.ExtensionLimitReached:
                    self.set_error(self.partition.label_error, "User passed the limit of maximum extension days !")

                elif extension == CommandState.NoMoreExtension:
                    self.set_error(self.partition.label_error, "User already used the extension week !")

            elif info['request'] == 'return':
                try:
                    return_ = user.return_book(info['book'], time, time)
                except:
                    self.set_error(self.partition.label_error, "User doesn't have the book !")
                    return

                if return_ == CommandState.Done:
                    self.requests[user][index]['accepted'] = "Accepted"
                    self.set_error(self.partition.label_error, "User request accepted ! Issue a receipt", 'green')

                else:
                    self.requests[user][index]['accepted'] = "Accepted"
                    self.set_error(self.partition.label_error,
                                   f"User request accepted ! Issue a bill for {return_[-1]} $", 'green')

        else:  # if deny button clicked
            self.requests[user][index]['accepted'] = "Denied"
            self.set_error(self.partition.label_error, "User request denied !", 'green')

        self.fill_list(self.partition.listWidget, 'officer')

    def issue_rb(self, mode: str):
        """
            The function to create a bill or receipt

            Parameters:
                mode (str): The mode of being bill or receipt
        """

        index = self.partition.listWidget.row(self.partition.listWidget.currentItem())
        x, user = 0, 0
        for user_ in self.requests.keys():
            x += len(self.requests[user_])
            if x > index:
                user = user_
                break

        index = -1
        for i in self.list_:
            if i.endswith(f'{user.first_name} {user.last_name}'):
                index += 1

            if i == self.partition.listWidget.currentItem().text():
                break

        info = self.requests[user][index]

        if info['accepted'] == "Accepted":
            if mode == 'receipt':
                receipt = Receipt(info['book'], user, user.returned_books[info['book']]['delay'])
                self.set_error(self.partition.label_error, "Done !", 'green')
                Tools.create_pdf(receipt)

            elif mode == 'bill':
                bill = 0
                for order in user.orders:
                    if 'bill' in order and order['book'] == info['book']:
                        bill = order['bill']

                bill = Bill(info['book'], user, user.returned_books[info['book']]['delay'], bill)
                self.set_error(self.partition.label_error, "Done !", 'green')
                Tools.create_pdf(bill)

        else:
            self.set_error(self.partition.label_error, f"Only accepted returning can have a {mode} !")

    def add_officer(self):
        """
            The function to add a new officer, it's similar to sign up
        """

        self.set_error(self.partition.label_error_2, "")

        regex = '^[A-Za-z0-9._%+-]+[@][A-Za-z0-9.-]+[A-Z|a-z]{2,3}$'
        all = [i.username for i in list(self.officers_costumers['costumer'] + self.officers_costumers['officer'])]

        username = self.partition.lineEdit_username.text().lower()
        password = self.partition.lineEdit_password.text()
        password_2 = self.partition.lineEdit_password_2.text()
        fullname = self.partition.lineEdit_full_name.text()
        email = self.partition.lineEdit_email.text()
        phone = self.partition.lineEdit_phone.text()

        if not username:
            self.set_error(self.partition.label_error_2, "Username is empty !")
            return

        elif username in all:
            self.set_error(self.partition.label_error_2, "Username is already used !")
            return

        elif not password or not password_2:
            self.set_error(self.partition.label_error_2, "Password is empty !")
            return

        elif not fullname:
            self.set_error(self.partition.label_error_2, "Name is empty !")
            return

        elif password != password_2:
            self.set_error(self.partition.label_error_2, "Passwords are not matching !")
            return

        elif email and not search(regex, email):
            self.set_error(self.partition.label_error_2, "Entered email is not valid !")
            return

        first_name = fullname.split(" ")[0]
        last_name = fullname.replace(first_name, "", 1)
        self.officers_costumers["officer"].append(Officer(first_name, last_name, username, password, email, phone))

        self.set_error(self.partition.label_error_2, "Signed up the new user successfully !", 'green')
        self.empty_boxes("officer")

    def SwitchTab(self, mode: str) -> None:
        """
            This function handle changes when switching between tabs

            Parameters:
                mode (str): The mode of being costumer or officer
        """

        if mode == "costumer":
            if self.partition.tabWidget.currentIndex() == 0:
                self.fill_table(self.partition.tableWidget_books, 'books', self.partition.comboBox_books)

            elif self.partition.tabWidget.currentIndex() == 1:
                self.fill_table(self.partition.tableWidget_my_books, 'my_books')

            elif self.partition.tabWidget.currentIndex() == 2:
                self.fill_list(self.partition.listWidget, mode)

        else:
            if 1:
                if self.partition.tabWidget.currentIndex() == 0:
                    self.fill_list(self.partition.listWidget, 'officer')

                elif self.partition.tabWidget.currentIndex() == 1:
                    self.fill_table(self.partition.tableWidget_books, 'books', self.partition.comboBox_books)

                elif self.partition.tabWidget.currentIndex() == 2:
                    pass

    def saveSqlite(self):
        """The function to save information to sqlite database"""

        def create_connection(db_file):
            try:
                with open(db_file, "r"):
                    pass
            except:
                with open(db_file, "w"):
                    pass

            try:
                conn = connect(db_file)
                return conn
            except:
                return None

        # create a database connection
        conn = create_connection("../Database/Database.db")

        # create books table
        create_table_exe = """ CREATE TABLE IF NOT EXISTS Books (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            author text NOT NULL,
                                            state text,
                                            reserved text,
                                            borrowed text,
                                            borrowed_time text,
                                            return_time text
                                        ); """
        c = conn.cursor()
        c.execute(create_table_exe)
        conn.commit()
        # insert data
        if self.books:
            for book in self.books:
                sql = ''' INSERT OR REPLACE INTO Books(name, author)
                              VALUES(?,?) '''
                cur = conn.cursor()
                cur.execute(sql, [book.name, book.author])
                conn.commit()

    def readSqlite(self):
        """
            The function to load information from sqlite database,
            if database doesn't exists it will create a officer and costumer and adds some books
        """

        try:
            with open("../Database/Database.db", "r"):
                pass
        except:
            self.add_book("Me Before you", "Jojo Moyes")
            self.add_book("Me After you", "Jojo Moyes")
            self.add_book("Paris 1", "Jojo Moyes")
            self.add_book("Paris 2", "Jojo Moyes")
            self.add_book("Paris 3", "Jojo Moyes")
            self.add_book("Paris 4", "Jojo Moyes")
            self.add_book("Paris 5", "Jojo Moyes")
            self.add_book("Paris 6", "Jojo Moyes")
            return

        def create_connection(db_file):
            conn = None
            try:
                conn = connect(db_file)
                return conn
            except:
                pass

            return conn

        # create a database connection
        conn = create_connection("../Database/Database.db")

        # read books data
        self.books = []

        cur = conn.cursor()
        cur.execute("SELECT * FROM Books")
        rows = cur.fetchall()
        for row in rows:
            self.books.append(Book(row[1], row[2], BookState.Available))


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    MainWindow = QtWidgets.QMainWindow()

    ui = GUI()
    ui.setupUi(MainWindow)

    ## for adding a new book:
    # ui.add_book("My Name", "Tokio")

    ui.main()

    MainWindow.closeEvent = ui.closeEvent
    ui.pushButton_Signin.clicked.connect(ui.sign_in)
    ui.pushButton_create_account.clicked.connect(ui.open_sign_up)

    MainWindow.show()
    exit(app.exec_())

