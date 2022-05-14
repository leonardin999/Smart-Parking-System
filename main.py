from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QCoreApplication, QThreadPool, QTimer
from PySide6.QtGui import QScreen

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
        self.camera_connection = False

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
        self.btn_send_email.clicked.connect(lambda: functions.MainFunctions.open_message_tool(self))
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

        self.entrance_result.textChanged.connect(lambda: functions.MainFunctions.check_entrance_result(self))
        self.exit_result.textChanged.connect(lambda: functions.MainFunctions.check_exit_result(self))

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


class MessageWindow(QMainWindow, Ui_ConnectWindow):
    def __init__(self):
        super(MessageWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Information Search Engine')
        self.license_search.setPlaceholderText('insert license number...')
        self.slot_edit.setReadOnly(True)

        self.db = None
        self.cursor = None
        self.db_connection = False
        self.founded = False
        functions.MessageFunctions.initial_connection(self)

        self.btn_search.clicked.connect(lambda: functions.MessageFunctions.search_information(self))
        self.btn_clear.clicked.connect(lambda: functions.MessageFunctions.reset_tools(self))
        self.btn_save.clicked.connect(lambda: functions.MessageFunctions.save_information(self))
        self.btn_send_sms.clicked.connect(lambda: functions.MessageFunctions.send_SMS(self))
        self.btn_email.clicked.connect(lambda: functions.MessageFunctions.send_Email(self))


if __name__ == '__main__':
    # setting screen to the center
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    centerPoint = QScreen.availableGeometry(app.primaryScreen()).center()

    login_window = LoginWindow()
    fg = login_window.frameGeometry()
    fg.moveCenter(centerPoint)
    login_window.move(fg.topLeft())

    # setup stylesheet
    app.setStyleSheet(load_stylesheet(theme="light"))
    # run
    login_window.show()
    app.exec()
