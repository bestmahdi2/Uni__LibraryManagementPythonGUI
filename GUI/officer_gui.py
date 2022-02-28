# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'officer_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OfficerWindow(object):
    def setupUi(self, OfficerWindow):
        OfficerWindow.setObjectName("OfficerWindow")
        OfficerWindow.resize(794, 816)
        OfficerWindow.setStyleSheet("background-color:#F0F0F0;")
        self.tabWidget = QtWidgets.QTabWidget(OfficerWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 180, 771, 621))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Notification = QtWidgets.QWidget()
        self.tab_Notification.setObjectName("tab_Notification")
        self.label_6 = QtWidgets.QLabel(self.tab_Notification)
        self.label_6.setGeometry(QtCore.QRect(40, 23, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#F6F8FA")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_Notification)
        self.textBrowser.setGeometry(QtCore.QRect(30, 320, 701, 156))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:white")
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.tab_Notification)
        self.listWidget.setGeometry(QtCore.QRect(30, 67, 701, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("background-color:white")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.tab_Notification)
        self.frame.setGeometry(QtCore.QRect(10, 10, 741, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #DAE5EA;")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        self.pushButton_issue_bill = QtWidgets.QPushButton(self.frame)
        self.pushButton_issue_bill.setGeometry(QtCore.QRect(210, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_issue_bill.setFont(font)
        self.pushButton_issue_bill.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_issue_bill.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_issue_bill.setObjectName("pushButton_issue_bill")
        self.pushButton_confirm = QtWidgets.QPushButton(self.frame)
        self.pushButton_confirm.setGeometry(QtCore.QRect(600, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_confirm.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_issue_receipt = QtWidgets.QPushButton(self.frame)
        self.pushButton_issue_receipt.setGeometry(QtCore.QRect(340, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_issue_receipt.setFont(font)
        self.pushButton_issue_receipt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_issue_receipt.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_issue_receipt.setObjectName("pushButton_issue_receipt")
        self.pushButton_deny = QtWidgets.QPushButton(self.frame)
        self.pushButton_deny.setGeometry(QtCore.QRect(470, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_deny.setFont(font)
        self.pushButton_deny.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_deny.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_deny.setObjectName("pushButton_deny")
        self.label_7 = QtWidgets.QLabel(self.tab_Notification)
        self.label_7.setGeometry(QtCore.QRect(40, 275, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#F6F8FA")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.tab_Notification)
        self.line_2.setGeometry(QtCore.QRect(220, 50, 321, 16))
        self.line_2.setStyleSheet("background-color:#F6F8FA")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.tab_Notification)
        self.line_4.setGeometry(QtCore.QRect(220, 304, 321, 16))
        self.line_4.setStyleSheet("background-color:#F6F8FA")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_error = QtWidgets.QLabel(self.tab_Notification)
        self.label_error.setGeometry(QtCore.QRect(30, 480, 711, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.frame.raise_()
        self.label_6.raise_()
        self.textBrowser.raise_()
        self.listWidget.raise_()
        self.label_7.raise_()
        self.line_2.raise_()
        self.line_4.raise_()
        self.label_error.raise_()
        self.tabWidget.addTab(self.tab_Notification, "")
        self.tab_Books_State = QtWidgets.QWidget()
        self.tab_Books_State.setObjectName("tab_Books_State")
        self.tableWidget_books = QtWidgets.QTableWidget(self.tab_Books_State)
        self.tableWidget_books.setGeometry(QtCore.QRect(20, 160, 721, 391))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_books.setFont(font)
        self.tableWidget_books.setStyleSheet("background-color:#FAFAFA")
        self.tableWidget_books.setAutoScrollMargin(20)
        self.tableWidget_books.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_books.setAlternatingRowColors(True)
        self.tableWidget_books.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_books.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget_books.setObjectName("tableWidget_books")
        self.tableWidget_books.setColumnCount(7)
        self.tableWidget_books.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(6, item)
        self.tableWidget_books.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_books.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_books.horizontalHeader().setHighlightSections(True)
        self.tableWidget_books.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_books.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_books.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_books.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_books.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_books.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_books.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_books.verticalHeader().setStretchLastSection(False)
        self.comboBox_books = QtWidgets.QComboBox(self.tab_Books_State)
        self.comboBox_books.setGeometry(QtCore.QRect(240, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_books.setFont(font)
        self.comboBox_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_books.setStyleSheet("background-color:white")
        self.comboBox_books.setObjectName("comboBox_books")
        self.comboBox_books.addItem("")
        self.comboBox_books.addItem("")
        self.comboBox_books.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.tab_Books_State)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 741, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #DAE5EA;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(4)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.tab_Books_State)
        self.label_9.setGeometry(QtCore.QRect(30, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:#F6F8FA")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.line_3 = QtWidgets.QFrame(self.tab_Books_State)
        self.line_3.setGeometry(QtCore.QRect(220, 70, 321, 16))
        self.line_3.setStyleSheet("background-color:#F6F8FA")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.tab_Books_State)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#F6F8FA")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.frame_2.raise_()
        self.tableWidget_books.raise_()
        self.comboBox_books.raise_()
        self.label_9.raise_()
        self.line_3.raise_()
        self.label_8.raise_()
        self.tabWidget.addTab(self.tab_Books_State, "")
        self.tab_Officer = QtWidgets.QWidget()
        self.tab_Officer.setObjectName("tab_Officer")
        self.lineEdit_password = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_password.setGeometry(QtCore.QRect(30, 250, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_2 = QtWidgets.QLabel(self.tab_Officer)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#F6F8FA")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.tab_Officer)
        self.label.setGeometry(QtCore.QRect(30, 100, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#F6F8FA")
        self.label.setObjectName("label")
        self.lineEdit_full_name = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_full_name.setGeometry(QtCore.QRect(390, 130, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_full_name.setFont(font)
        self.lineEdit_full_name.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_full_name.setClearButtonEnabled(True)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.label_5 = QtWidgets.QLabel(self.tab_Officer)
        self.label_5.setGeometry(QtCore.QRect(390, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#F6F8FA")
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.tab_Officer)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 741, 521))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #D9DFE5;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(4)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_create_officer = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_create_officer.setGeometry(QtCore.QRect(290, 450, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_create_officer.setFont(font)
        self.pushButton_create_officer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_create_officer.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_create_officer.setObjectName("pushButton_create_officer")
        self.label_4 = QtWidgets.QLabel(self.tab_Officer)
        self.label_4.setGeometry(QtCore.QRect(390, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#F6F8FA")
        self.label_4.setObjectName("label_4")
        self.lineEdit_username = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_username.setGeometry(QtCore.QRect(30, 130, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_phone.setGeometry(QtCore.QRect(390, 370, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_phone.setClearButtonEnabled(True)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_11 = QtWidgets.QLabel(self.tab_Officer)
        self.label_11.setGeometry(QtCore.QRect(390, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:#F6F8FA")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.tab_Officer)
        self.label_10.setGeometry(QtCore.QRect(30, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#F6F8FA")
        self.label_10.setObjectName("label_10")
        self.lineEdit_email = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_email.setGeometry(QtCore.QRect(30, 370, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_email.setClearButtonEnabled(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password_2 = QtWidgets.QLineEdit(self.tab_Officer)
        self.lineEdit_password_2.setGeometry(QtCore.QRect(390, 250, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_password_2.setFont(font)
        self.lineEdit_password_2.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_2.setClearButtonEnabled(True)
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.line_6 = QtWidgets.QFrame(self.tab_Officer)
        self.line_6.setGeometry(QtCore.QRect(220, 70, 321, 16))
        self.line_6.setStyleSheet("background-color:#F6F8FA")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_14 = QtWidgets.QLabel(self.tab_Officer)
        self.label_14.setGeometry(QtCore.QRect(240, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:#F6F8FA")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_error_2 = QtWidgets.QLabel(self.tab_Officer)
        self.label_error_2.setGeometry(QtCore.QRect(30, 420, 701, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_error_2.setFont(font)
        self.label_error_2.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error_2.setText("")
        self.label_error_2.setObjectName("label_error_2")
        self.frame_3.raise_()
        self.lineEdit_password.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit_full_name.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.lineEdit_username.raise_()
        self.lineEdit_phone.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.lineEdit_email.raise_()
        self.lineEdit_password_2.raise_()
        self.line_6.raise_()
        self.label_14.raise_()
        self.label_error_2.raise_()
        self.tabWidget.addTab(self.tab_Officer, "")
        self.line = QtWidgets.QFrame(OfficerWindow)
        self.line.setGeometry(QtCore.QRect(180, 150, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_logo = QtWidgets.QLabel(OfficerWindow)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 761, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.label_3 = QtWidgets.QLabel(OfficerWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 761, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(OfficerWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OfficerWindow)
        OfficerWindow.setTabOrder(self.tabWidget, self.listWidget)
        OfficerWindow.setTabOrder(self.listWidget, self.textBrowser)
        OfficerWindow.setTabOrder(self.textBrowser, self.pushButton_confirm)
        OfficerWindow.setTabOrder(self.pushButton_confirm, self.pushButton_deny)
        OfficerWindow.setTabOrder(self.pushButton_deny, self.pushButton_issue_receipt)
        OfficerWindow.setTabOrder(self.pushButton_issue_receipt, self.pushButton_issue_bill)
        OfficerWindow.setTabOrder(self.pushButton_issue_bill, self.comboBox_books)
        OfficerWindow.setTabOrder(self.comboBox_books, self.tableWidget_books)
        OfficerWindow.setTabOrder(self.tableWidget_books, self.lineEdit_username)
        OfficerWindow.setTabOrder(self.lineEdit_username, self.lineEdit_full_name)
        OfficerWindow.setTabOrder(self.lineEdit_full_name, self.lineEdit_password)
        OfficerWindow.setTabOrder(self.lineEdit_password, self.lineEdit_password_2)
        OfficerWindow.setTabOrder(self.lineEdit_password_2, self.lineEdit_email)
        OfficerWindow.setTabOrder(self.lineEdit_email, self.lineEdit_phone)
        OfficerWindow.setTabOrder(self.lineEdit_phone, self.pushButton_create_officer)

    def retranslateUi(self, OfficerWindow):
        _translate = QtCore.QCoreApplication.translate
        OfficerWindow.setWindowTitle(_translate("OfficerWindow", "Officer Partition"))
        self.label_6.setText(_translate("OfficerWindow", "Select a notification bellow to manage users requests"))
        self.textBrowser.setStatusTip(_translate("OfficerWindow", "Full description of notification"))
        self.listWidget.setStatusTip(_translate("OfficerWindow", "Select a notification to manage"))
        self.pushButton_issue_bill.setStatusTip(_translate("OfficerWindow", "Click to issue bill ..."))
        self.pushButton_issue_bill.setText(_translate("OfficerWindow", "Issue Bill"))
        self.pushButton_confirm.setStatusTip(_translate("OfficerWindow", "Click to confirm notification ..."))
        self.pushButton_confirm.setText(_translate("OfficerWindow", "Confirm"))
        self.pushButton_issue_receipt.setStatusTip(_translate("OfficerWindow", "Click to issue receipt ..."))
        self.pushButton_issue_receipt.setText(_translate("OfficerWindow", "Issue Receipt"))
        self.pushButton_deny.setStatusTip(_translate("OfficerWindow", "Click to confirm notification ..."))
        self.pushButton_deny.setText(_translate("OfficerWindow", "Deny"))
        self.label_7.setText(_translate("OfficerWindow", "Full Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Notification), _translate("OfficerWindow", "🔔 Notification"))
        self.tableWidget_books.setSortingEnabled(True)
        item = self.tableWidget_books.horizontalHeaderItem(0)
        item.setText(_translate("OfficerWindow", "📕 Name"))
        item = self.tableWidget_books.horizontalHeaderItem(1)
        item.setText(_translate("OfficerWindow", "👩🏻‍🎓 Author"))
        item = self.tableWidget_books.horizontalHeaderItem(2)
        item.setText(_translate("OfficerWindow", "🧾 State"))
        item = self.tableWidget_books.horizontalHeaderItem(3)
        item.setText(_translate("OfficerWindow", "🤙🏻 Reserved"))
        item = self.tableWidget_books.horizontalHeaderItem(4)
        item.setText(_translate("OfficerWindow", "👋🏻 Borrowed"))
        item = self.tableWidget_books.horizontalHeaderItem(5)
        item.setText(_translate("OfficerWindow", "📅 Borrowed"))
        item = self.tableWidget_books.horizontalHeaderItem(6)
        item.setText(_translate("OfficerWindow", "📅 Return"))
        self.comboBox_books.setStatusTip(_translate("OfficerWindow", "Select a book state to show books on table"))
        self.comboBox_books.setItemText(0, _translate("OfficerWindow", "Available"))
        self.comboBox_books.setItemText(1, _translate("OfficerWindow", "Borrowed"))
        self.comboBox_books.setItemText(2, _translate("OfficerWindow", "Reserved"))
        self.label_9.setText(_translate("OfficerWindow", "Books with statement:"))
        self.label_8.setText(_translate("OfficerWindow", "Select a state from combobox bellow to see the related books"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Books_State), _translate("OfficerWindow", "📚 Books State"))
        self.lineEdit_password.setStatusTip(_translate("OfficerWindow", "Enter a password"))
        self.label_2.setText(_translate("OfficerWindow", "Password"))
        self.label.setText(_translate("OfficerWindow", "Username"))
        self.lineEdit_full_name.setStatusTip(_translate("OfficerWindow", "Enter your full name"))
        self.label_5.setText(_translate("OfficerWindow", "Full Name"))
        self.pushButton_create_officer.setStatusTip(_translate("OfficerWindow", "Click to create an officer ..."))
        self.pushButton_create_officer.setText(_translate("OfficerWindow", "Create An Officer"))
        self.label_4.setText(_translate("OfficerWindow", "Confirm Password"))
        self.lineEdit_username.setStatusTip(_translate("OfficerWindow", "Enter your username"))
        self.lineEdit_phone.setStatusTip(_translate("OfficerWindow", "Enter your phone number"))
        self.label_11.setText(_translate("OfficerWindow", "Phone Number"))
        self.label_10.setText(_translate("OfficerWindow", "Email Address"))
        self.lineEdit_email.setStatusTip(_translate("OfficerWindow", "Enter your email address"))
        self.lineEdit_password_2.setStatusTip(_translate("OfficerWindow", "Confirm the password"))
        self.label_14.setText(_translate("OfficerWindow", "Create a new officer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Officer), _translate("OfficerWindow", "👩‍💻 Officer"))
        self.label_3.setText(_translate("OfficerWindow", "Officer Partition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OfficerWindow = QtWidgets.QDialog()
    ui = Ui_OfficerWindow()
    ui.setupUi(OfficerWindow)
    OfficerWindow.show()
    sys.exit(app.exec_())
