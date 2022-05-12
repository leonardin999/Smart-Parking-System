from PySide6.QtWidgets import QMessageBox


class CustomExitNotify(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle("Notification")
        self.setText("Thanks for using our services.\nEnjoy your ride!")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        button = self.exec_()

