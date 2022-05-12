from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QCoreApplication, QThreadPool, QTimer
from PySide6.QtGui import QIcon, QPixmap, QScreen, QColor

import serial
import sys
from qdarktheme import load_stylesheet, get_themes
from design import *
import functions


# create the application and the main window


def toggle_theme(theme) -> None:
    stylesheet = load_stylesheet(theme)
    QApplication.instance().setStyleSheet(stylesheet)


class MainWindow(QMainWindow, Ui_MainWindow):
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Smart Parking System')
        self.style_box.addItems(get_themes())
        self.style_box.setCurrentText("light")
        self.style_box.currentTextChanged.connect(toggle_theme)
        self.entrance_thread = QThreadPool()
        self.exit_thread = QThreadPool()

        self.detected_entrance = False
        self.detected_exit = False

        self.ser = serial.Serial()
        self.connected = False
        self.command = ''
        self.slot_information = ''
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: functions.MainFunctions.start_camera(self))

        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda: functions.MainFunctions.current_time(self))
        self.timer1.start()
        self.slot_map = []
        self.db = None
        self.cursor = None
        self.db_connection = False
        functions.DatabaseFunctions.initial_connection(self)
        functions.MainFunctions.ui_definitions(self)
        functions.DatabaseFunctions.show_table_data(self)
        functions.DatabaseFunctions.counted_function(self)
        functions.SlotFunctions.initial_slot(self)

        self.btn_login.clicked.connect(lambda: functions.MainFunctions.LogOut(self))
        self.btn_website.clicked.connect(lambda: functions.MainFunctions.goToWebsite(self))
        self.run_cam.clicked.connect(lambda: functions.MainFunctions.reset_camera(self))

        self.btn_connect_cam.clicked.connect(lambda: functions.MainFunctions.setup_camera(self))
        self.btn_disconnect_cam.clicked.connect(lambda: functions.MainFunctions.disconnect_camera(self))

        self.capture_entrance.clicked.connect(lambda: functions.MainFunctions.entrance_thread_capture(self))
        self.capture_exit.clicked.connect(lambda: functions.MainFunctions.exit_thread_capture(self))

        self.btn_connect.clicked.connect(lambda: functions.SystemFunctions.option_check(self))

        self.btn_find.clicked.connect(lambda: functions.DatabaseFunctions.unfinished_function(self))
        self.btn_export.clicked.connect(lambda: functions.DatabaseFunctions.unfinished_function(self))

        self.btn_reset.clicked.connect(lambda: functions.DatabaseFunctions.show_table_data(self))
        self.btn_reset.clicked.connect(lambda: functions.DatabaseFunctions.counted_function(self))

        self.btn_refresh.clicked.connect(lambda: functions.SlotFunctions.initial_slot(self))
        self.all_opt.clicked.connect(lambda: functions.SlotFunctions.show_all_slot(self))
        self.available_opt.clicked.connect(lambda: functions.SlotFunctions.show_available_list(self))
        self.resersed_opt.clicked.connect(lambda: functions.SlotFunctions.show_reserved_list(self))
        self.unavailable_opt.clicked.connect(lambda: functions.SlotFunctions.show_unavailable_list(self))

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Adding function
        functions.LoginFunctions.ui_definition(self)
        self.close_popup.clicked.connect(lambda: self.frame_error.hide())
        self.Log_In.clicked.connect(lambda: functions.LoginFunctions.checkFields(self))


if __name__ == '__main__':
    # setting screen to the center
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    centerPoint = QScreen.availableGeometry(app.primaryScreen()).center()
    window = LoginWindow()
    fg = window.frameGeometry()
    fg.moveCenter(centerPoint)
    window.move(fg.topLeft())
    # setup stylesheet
    app.setStyleSheet(load_stylesheet(theme="light"))
    # run
    window.show()
    app.exec()
