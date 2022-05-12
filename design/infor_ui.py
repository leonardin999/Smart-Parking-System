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
    QFont, QFontDatabase, QGradient, QIcon,QScreen,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from qdarktheme import load_stylesheet, get_themes

import sys
class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow):
        if not ConnectWindow.objectName():
            ConnectWindow.setObjectName(u"ConnectWindow")
        ConnectWindow.resize(348, 290)
        self.centralwidget = QWidget(ConnectWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 331, 91))
        self.btn_search = QPushButton(self.groupBox)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(200, 55, 121, 31))
        self.license_search = QLineEdit(self.groupBox)
        self.license_search.setObjectName(u"license_search")
        self.license_search.setGeometry(QRect(10, 20, 311, 31))
        self.layoutWidget4_2 = QWidget(self.centralwidget)
        self.layoutWidget4_2.setObjectName(u"layoutWidget4_2")
        self.layoutWidget4_2.setGeometry(QRect(20, 110, 91, 121))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget4_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget4_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget4_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)

        self.label_19 = QLabel(self.layoutWidget4_2)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_6.addWidget(self.label_19)

        self.label_20 = QLabel(self.layoutWidget4_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_6.addWidget(self.label_20)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 240, 331, 41))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(121, 110, 221, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_edit = QLineEdit(self.layoutWidget)
        self.name_edit.setObjectName(u"name_edit")

        self.verticalLayout.addWidget(self.name_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.number_edit = QLineEdit(self.layoutWidget)
        self.number_edit.setObjectName(u"number_edit")

        self.horizontalLayout.addWidget(self.number_edit)

        self.btn_send_sms = QPushButton(self.layoutWidget)
        self.btn_send_sms.setObjectName(u"btn_send_sms")

        self.horizontalLayout.addWidget(self.btn_send_sms)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.email_edit = QLineEdit(self.layoutWidget)
        self.email_edit.setObjectName(u"email_edit")

        self.verticalLayout.addWidget(self.email_edit)

        self.slot_edit = QLineEdit(self.layoutWidget)
        self.slot_edit.setObjectName(u"slot_edit")

        self.verticalLayout.addWidget(self.slot_edit)

        ConnectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConnectWindow)

        QMetaObject.connectSlotsByName(ConnectWindow)
    # setupUi

    def retranslateUi(self, ConnectWindow):
        ConnectWindow.setWindowTitle(QCoreApplication.translate("ConnectWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConnectWindow", u"License Plate Search:", None))
        self.btn_search.setText(QCoreApplication.translate("ConnectWindow", u"Search", None))
        self.label_16.setText(QCoreApplication.translate("ConnectWindow", u"Owner name:", None))
        self.label_17.setText(QCoreApplication.translate("ConnectWindow", u"Number:", None))
        self.label_19.setText(QCoreApplication.translate("ConnectWindow", u"Email:", None))
        self.label_20.setText(QCoreApplication.translate("ConnectWindow", u"Parking slot:", None))
        self.pushButton_3.setText(QCoreApplication.translate("ConnectWindow", u"Send Email", None))
        self.btn_send_sms.setText(QCoreApplication.translate("ConnectWindow", u"send SMS", None))
    # retranslateUi

if __name__ == '__main__':
    # setting screen to the center
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    centerPoint = QScreen.availableGeometry(app.primaryScreen()).center()
    ui = QMainWindow()
    window = Ui_ConnectWindow()
    window.setupUi(ui)
    fg = ui.frameGeometry()
    fg.moveCenter(centerPoint)
    ui.move(fg.topLeft())
    # setup stylesheet
    app.setStyleSheet(load_stylesheet(theme="light"))
    # run
    ui.show()
    app.exec()