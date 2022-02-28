# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(461, 830)
        SignUpWindow.setStyleSheet("background-color:#FFFFFF")
        self.label_4 = QtWidgets.QLabel(SignUpWindow)
        self.label_4.setGeometry(QtCore.QRect(63, 360, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#F6F8FA")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(SignUpWindow)
        self.label_5.setGeometry(QtCore.QRect(63, 450, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#F6F8FA")
        self.label_5.setObjectName("label_5")
        self.lineEdit_phone = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_phone.setGeometry(QtCore.QRect(60, 660, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_phone.setClearButtonEnabled(True)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.lineEdit_password_2 = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_password_2.setGeometry(QtCore.QRect(60, 390, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_password_2.setFont(font)
        self.lineEdit_password_2.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_2.setClearButtonEnabled(True)
        self.lineEdit_password_2.setObjectName("lineEdit_password_2")
        self.label_logo = QtWidgets.QLabel(SignUpWindow)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.lineEdit_password = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(60, 300, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_username = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_username.setGeometry(QtCore.QRect(60, 210, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_2 = QtWidgets.QLabel(SignUpWindow)
        self.label_2.setGeometry(QtCore.QRect(63, 270, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#F6F8FA")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(SignUpWindow)
        self.frame.setGeometry(QtCore.QRect(30, 160, 401, 656))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #D9DFE5;")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        self.pushButton_Signup = QtWidgets.QPushButton(self.frame)
        self.pushButton_Signup.setGeometry(QtCore.QRect(30, 590, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_Signup.setFont(font)
        self.pushButton_Signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Signup.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_Signup.setAutoDefault(False)
        self.pushButton_Signup.setObjectName("pushButton_Signup")
        self.label = QtWidgets.QLabel(SignUpWindow)
        self.label.setGeometry(QtCore.QRect(63, 180, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#F6F8FA")
        self.label.setObjectName("label")
        self.label_error = QtWidgets.QLabel(SignUpWindow)
        self.label_error.setGeometry(QtCore.QRect(60, 707, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.label_7 = QtWidgets.QLabel(SignUpWindow)
        self.label_7.setGeometry(QtCore.QRect(63, 630, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#F6F8FA")
        self.label_7.setObjectName("label_7")
        self.lineEdit_email = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_email.setGeometry(QtCore.QRect(60, 570, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_email.setClearButtonEnabled(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_6 = QtWidgets.QLabel(SignUpWindow)
        self.label_6.setGeometry(QtCore.QRect(63, 540, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#F6F8FA")
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(SignUpWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_full_name = QtWidgets.QLineEdit(SignUpWindow)
        self.lineEdit_full_name.setGeometry(QtCore.QRect(60, 480, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_full_name.setFont(font)
        self.lineEdit_full_name.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;")
        self.lineEdit_full_name.setClearButtonEnabled(True)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.pushButton_signin = QtWidgets.QPushButton(SignUpWindow)
        self.pushButton_signin.setGeometry(QtCore.QRect(230, 720, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_signin.setFont(font)
        self.pushButton_signin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_signin.setStyleSheet("color:#0969DA")
        self.pushButton_signin.setFlat(True)
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.frame.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_phone.raise_()
        self.lineEdit_password_2.raise_()
        self.label_logo.raise_()
        self.lineEdit_password.raise_()
        self.lineEdit_username.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_error.raise_()
        self.label_7.raise_()
        self.lineEdit_email.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.lineEdit_full_name.raise_()
        self.pushButton_signin.raise_()

        self.retranslateUi(SignUpWindow)
        self.pushButton_signin.clicked.connect(SignUpWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)
        SignUpWindow.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        SignUpWindow.setTabOrder(self.lineEdit_password, self.lineEdit_password_2)
        SignUpWindow.setTabOrder(self.lineEdit_password_2, self.lineEdit_full_name)
        SignUpWindow.setTabOrder(self.lineEdit_full_name, self.lineEdit_email)
        SignUpWindow.setTabOrder(self.lineEdit_email, self.lineEdit_phone)
        SignUpWindow.setTabOrder(self.lineEdit_phone, self.pushButton_signin)
        SignUpWindow.setTabOrder(self.pushButton_signin, self.pushButton_Signup)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Dialog"))
        self.label_4.setText(_translate("SignUpWindow", "Confirm Password"))
        self.label_5.setText(_translate("SignUpWindow", "Full Name"))
        self.lineEdit_phone.setStatusTip(_translate("SignUpWindow", "Enter your phone number"))
        self.lineEdit_password_2.setStatusTip(_translate("SignUpWindow", "Confirm the password"))
        self.lineEdit_password.setStatusTip(_translate("SignUpWindow", "Enter a password"))
        self.lineEdit_username.setStatusTip(_translate("SignUpWindow", "Enter your username"))
        self.label_2.setText(_translate("SignUpWindow", "Password"))
        self.pushButton_Signup.setStatusTip(_translate("SignUpWindow", "Click to sign up ..."))
        self.pushButton_Signup.setText(_translate("SignUpWindow", "Sign up"))
        self.label.setText(_translate("SignUpWindow", "Username"))
        self.label_7.setText(_translate("SignUpWindow", "Phone Number"))
        self.lineEdit_email.setStatusTip(_translate("SignUpWindow", "Enter your email address"))
        self.label_6.setText(_translate("SignUpWindow", "Email Address"))
        self.label_3.setText(_translate("SignUpWindow", "Sign up to Library Manager"))
        self.lineEdit_full_name.setStatusTip(_translate("SignUpWindow", "Enter your full name"))
        self.pushButton_signin.setStatusTip(_translate("SignUpWindow", "Click to sign in ..."))
        self.pushButton_signin.setText(_translate("SignUpWindow", "Already have an account ..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpWindow = QtWidgets.QDialog()
    ui = Ui_SignUpWindow()
    ui.setupUi(SignUpWindow)
    SignUpWindow.show()
    sys.exit(app.exec_())
