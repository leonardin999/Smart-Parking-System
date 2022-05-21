# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'send_information.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow):
        if not ConnectWindow.objectName():
            ConnectWindow.setObjectName(u"ConnectWindow")
        ConnectWindow.resize(340, 310)
        self.centralwidget = QWidget(ConnectWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 321, 91))
        self.btn_clear = QPushButton(self.groupBox)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(140, 55, 81, 31))
        self.license_search = QLineEdit(self.groupBox)
        self.license_search.setObjectName(u"license_search")
        self.license_search.setGeometry(QRect(10, 20, 301, 31))
        self.btn_search = QPushButton(self.groupBox)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(230, 55, 81, 31))
        self.btn_email = QPushButton(self.centralwidget)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setGeometry(QRect(110, 260, 221, 41))
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(10, 260, 91, 41))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 111, 81, 141))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout.addWidget(self.label_20)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(116, 111, 211, 141))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_edit = QLineEdit(self.widget1)
        self.name_edit.setObjectName(u"name_edit")

        self.verticalLayout_2.addWidget(self.name_edit)

        self.name_edit_2 = QLineEdit(self.widget1)
        self.name_edit_2.setObjectName(u"name_edit_2")

        self.verticalLayout_2.addWidget(self.name_edit_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.number_edit = QLineEdit(self.widget1)
        self.number_edit.setObjectName(u"number_edit")

        self.horizontalLayout.addWidget(self.number_edit)

        self.btn_send_sms = QPushButton(self.widget1)
        self.btn_send_sms.setObjectName(u"btn_send_sms")

        self.horizontalLayout.addWidget(self.btn_send_sms)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.email_edit = QLineEdit(self.widget1)
        self.email_edit.setObjectName(u"email_edit")

        self.verticalLayout_2.addWidget(self.email_edit)

        self.slot_edit = QLineEdit(self.widget1)
        self.slot_edit.setObjectName(u"slot_edit")

        self.verticalLayout_2.addWidget(self.slot_edit)

        ConnectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConnectWindow)

        QMetaObject.connectSlotsByName(ConnectWindow)
    # setupUi

    def retranslateUi(self, ConnectWindow):
        ConnectWindow.setWindowTitle(QCoreApplication.translate("ConnectWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConnectWindow", u"License Plate Search:", None))
        self.btn_clear.setText(QCoreApplication.translate("ConnectWindow", u"Clear", None))
        self.btn_search.setText(QCoreApplication.translate("ConnectWindow", u"Search", None))
        self.btn_email.setText(QCoreApplication.translate("ConnectWindow", u"Send Email", None))
        self.btn_save.setText(QCoreApplication.translate("ConnectWindow", u"Save", None))
        self.label_16.setText(QCoreApplication.translate("ConnectWindow", u"Owner name:", None))
        self.label_18.setText(QCoreApplication.translate("ConnectWindow", u"Type of Car:", None))
        self.label_17.setText(QCoreApplication.translate("ConnectWindow", u"Number:", None))
        self.label_19.setText(QCoreApplication.translate("ConnectWindow", u"Email:", None))
        self.label_20.setText(QCoreApplication.translate("ConnectWindow", u"Parking slot:", None))
        self.btn_send_sms.setText(QCoreApplication.translate("ConnectWindow", u"send SMS", None))
    # retranslateUi

