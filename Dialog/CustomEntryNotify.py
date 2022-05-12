from PySide6.QtWidgets import QMessageBox


class CustomEntryNotify(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle("Notification")
        self.setText("Accepted Vehicle.\nOPen the gate for vehicle")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        button = self.exec_()

