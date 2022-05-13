from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomMessageInformation(QDialog):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.setWindowTitle("Announcement:")
        button = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(button)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        content = QLabel(f"{self.message}")
        self.layout.addWidget(content)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)