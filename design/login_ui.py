# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(382, 294)
        LoginWindow.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Log_In = QPushButton(self.centralwidget)
        self.Log_In.setObjectName(u"Log_In")
        self.Log_In.setGeometry(QRect(230, 230, 141, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.Log_In.setFont(font)
        self.Log_In.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(50, 50, 50);\n"
"	border: 2px solid rgb(60, 60, 60);\n"
"	border-radius: 20px;\n"
"	\n"
"	color: rgb(214, 214, 214);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(150, 150, 150);\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	color: rgb(35, 35, 35);\n"
"}")
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(328, 10, 17, 17))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 80, 161, 21))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(93, 93, 93);")
        self.frame_error = QFrame(self.centralwidget)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setGeometry(QRect(10, 40, 361, 30))
        self.frame_error.setMaximumSize(QSize(450, 16777215))
        self.frame_error.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.label_error = QLabel(self.frame_error)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(70, 5, 241, 21))
        self.label_error.setStyleSheet(u"color: rgb(35, 35, 35);")
        self.label_error.setAlignment(Qt.AlignCenter)
        self.close_popup = QPushButton(self.frame_error)
        self.close_popup.setObjectName(u"close_popup")
        self.close_popup.setGeometry(QRect(335, 7, 17, 17))
        self.close_popup.setMaximumSize(QSize(20, 20))
        self.close_popup.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(163, 163, 163);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 50, 50);	\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);	\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.Sign_Up_Pages = QPushButton(self.centralwidget)
        self.Sign_Up_Pages.setObjectName(u"Sign_Up_Pages")
        self.Sign_Up_Pages.setGeometry(QRect(10, 250, 171, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setUnderline(True)
        self.Sign_Up_Pages.setFont(font1)
        self.Sign_Up_Pages.setStyleSheet(u"QPushButton {	\n"
"	background-color:transparent;\n"
"	border: 5px transparent;\n"
"	color: rgb(38, 38, 38);\n"
"}\n"
"QPushButton:hover {	\n"
"	color:rgb(186, 186, 186);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color:transparent;\n"
"	color:rgb(80, 100, 26);\n"
"}")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 155, 191, 21))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(93, 93, 93);")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 180, 321, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"QLineEdit {\n"
"	border: 5px transparent;\n"
"	background-color: transparent;	\n"
"	color: rgb(74, 74, 74);\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(241, 241, 241);\n"
"	border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid transparent;	\n"
"	color:rgb(0, 0, 0);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.password.setMaxLength(32)
        self.btn_maximize = QPushButton(self.centralwidget)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(306, 10, 17, 17))
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(350, 10, 17, 17))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.Username = QLineEdit(self.centralwidget)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(30, 105, 321, 31))
        self.Username.setFont(font2)
        self.Username.setStyleSheet(u"QLineEdit {\n"
"	border: 5px transparent;\n"
"	background-color: transparent;	\n"
"	color: rgb(90, 90, 90);\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(241, 241, 241);\n"
"	border: 5px solid rgb(241, 241, 241);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid transparent;	\n"
"	color:rgb(0, 0, 0);\n"
"	border-bottom-color: rgb(0, 0, 0);\n"
"}")
        self.Username.setMaxLength(32)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.Log_In.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("LoginWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        self.label_14.setText(QCoreApplication.translate("LoginWindow", u"USERNAME", None))
        self.label_error.setText(QCoreApplication.translate("LoginWindow", u"Error", None))
        self.close_popup.setText("")
        self.Sign_Up_Pages.setText(QCoreApplication.translate("LoginWindow", u"Create a new account ?", None))
        self.label_12.setText(QCoreApplication.translate("LoginWindow", u"PASSWORD", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your password", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("LoginWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("LoginWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.Username.setText("")
        self.Username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your username", None))
    # retranslateUi

