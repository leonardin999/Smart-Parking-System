from modules import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QScreen


class LoginFunctions(LoginWindow):
    styleLineEditOk = ("QLineEdit {\n"
                       "    border: 2px solid rgb(45, 45, 45);\n"
                       "    border-radius: 5px;\n"
                       "    padding: 15px;\n"
                       "    background-color: rgb(30, 30, 30);    \n"
                       "    color: rgb(100, 100, 100);\n"
                       "}\n"
                       "QLineEdit:hover {\n"
                       "    border: 2px solid rgb(55, 55, 55);\n"
                       "}\n"
                       "QLineEdit:focus {\n"
                       "    border: 2px solid rgb(255, 207, 0);    \n"
                       "    color: rgb(200, 200, 200);\n"
                       "}")

    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    padding: 15px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    stylePopupError = "background-color: rgb(255, 85, 127); border-radius: 5px;"
    stylePopupOk = "background-color: rgb(0, 255, 123); border-radius: 5px;"

    def checkFields(self):
        self.textUser = ""
        self.textPassword = ""

        def showMessage(message):
            self.frame_error.show()
            self.label_error.setText(message)

        # CHECK USER
        if not self.label_error.text():
            self.textUser = " Username is empty... "
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditError)
        elif not self.Username.text() == "admin":
            self.textUser = " Wrong username "
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditError)
        else:
            self.textUser = ""
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditOk)

        # CHECK PASSWORD
        if not self.password.text():
            self.textPassword = " Password is empty... "
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditError)
        elif not self.password.text() == "password":
            self.textPassword = "  Wrong password "
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditError)
        else:
            self.textPassword = ""
            self.label_error.setStyleSheet(LoginFunctions.styleLineEditOk)

        # CHECK FIELDS
        if self.textUser != '':
            text = f"{self.textUser}"
            showMessage(text)
            self.frame_error.setStyleSheet(LoginFunctions.stylePopupError)
        elif self.textPassword != '':
            text = f"{self.textPassword}"
            showMessage(text)
            self.frame_error.setStyleSheet(LoginFunctions.stylePopupError)
        else:
            self.frame_error.setStyleSheet(LoginFunctions.stylePopupOk)
            LoginFunctions.LogIn(self)

    def LogIn(self):
        self.main = MainWindow()
        self.close()
        self.main.show()

    def ui_definition(self):

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

        ### ==> MINIMIZE
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())

        self.frame_error.hide()
