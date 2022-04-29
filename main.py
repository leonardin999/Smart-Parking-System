from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QIcon, QPixmap, QScreen

import sys
from qdarktheme import load_stylesheet
from modules import Ui_MainWindow


# create the application and the main window


class MainWindow(QMainWindow, Ui_MainWindow):
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Smart Parking System!')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = MainWindow()
    # setting screen to the center
    centerPoint = QScreen.availableGeometry(app.primaryScreen()).center()
    fg = window.frameGeometry()
    fg.moveCenter(centerPoint)
    window.move(fg.topLeft())
    # setup stylesheet
    app.setStyleSheet(load_stylesheet(theme="light", border="rounded"))
    # run
    window.show()
    app.exec()
