import time

from modules import *
from Dialog import CustomLogoutDialog, CustomMessageInformation
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from PySide6.QtGui import QColor, QImage, QPixmap
from PySide6.QtCore import Qt

import cv2
import os
import imutils
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from .worker import Worker


class MainFunctions(MainWindow):

    def LogOut(self):
        dialog = CustomLogoutDialog()
        if dialog.exec_():
            self.close()
            self.login = LoginWindow()
            self.login.show()
        else:
            pass

    @staticmethod
    def goToWebsite(self):
        import webbrowser
        url = "http://localhost/parking/dashboard"
        webbrowser.open_new_tab(url)

    def open_message_tool(self):
        self.mail_window = MessageWindow()
        self.mail_window.close()
        self.mail_window.show()

    def setup_camera(self):
        if not self.camera_connection:
            self.camera_connection = True
            if not self.timer.isActive():
                try:
                    self.entrance_cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
                    self.entrance_cam.set(3, 1280)
                    self.entrance_cam.set(4, 720)
                    self.exit_cam = cv2.VideoCapture(2, cv2.CAP_DSHOW)
                    self.exit_cam.set(3, 1280)
                    self.exit_cam.set(4, 720)
                    self.timer.start(150)
                    self.run_cam.setText("Reset")
                except:
                    self.camera_connection = False
                    error_message = 'Failed to connect to Camera.\n' \
                                    'Please try again.'
                    dialog = CustomMessageInformation(error_message)
                    if dialog.exec_():
                        self.btn_connect_cam.setChecked(False)

    def disconnect_camera(self):
        if self.camera_connection:
            self.camera_connection = False
            if self.timer.isActive():
                try:
                    self.timer.stop()
                    self.entrance_cam.release()
                    self.exit_cam.release()
                    cv2.destroyAllWindows()
                    self.run_cam.setText("Clear")
                except:
                    self.camera_connection = False
                    error_message = 'Failed to disconnect to Camera.\n' \
                                    'Please try again.'
                    dialog = CustomMessageInformation(error_message)
                    if dialog.exec_():
                        self.btn_disconnect_cam.setChecked(False)

    def reset_camera(self):
        if self.camera_connection:
            cv2.destroyAllWindows()
            self.btn_connect_cam.setChecked(False)
            self.btn_disconnect_cam.setChecked(False)
            self.entrance_view.clear()
            self.exit_view.clear()
            self.entrance_capture_1.clear()
            self.entrance_capture_2.clear()
            self.exit_capture_1.clear()
            self.exit_capture_2.clear()
            self.entrance_result.clear()
            self.exit_result.clear()

    def capture_entrance(self):
        if self.ret0:
            image_path = os.path.join(os.getcwd(), 'images/entrance.png')
            cv2.imwrite(image_path, self.img1)

        if os.path.isfile(image_path):
            img = cv2.imread(image_path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (320, 150))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(gray, 13, 15, 15)

            edged = cv2.Canny(gray, 30, 200)
            contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None
            try:
                for c in contours:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

                    if len(approx) == 4:
                        screenCnt = approx
                        break

                if screenCnt is None:
                    detected = 0
                    self.detected_entrance = False
                    self.entrance_result.setText('Error Detected')
                else:
                    self.detected_entrance = True
                    detected = 1

                if detected == 1:
                    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

                mask = np.zeros(gray.shape, np.uint8)
                new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
                new_image = cv2.bitwise_and(img, img, mask=mask)

                (x, y) = np.where(mask == 255)
                (topx, topy) = (np.min(x), np.min(y))
                (bottomx, bottomy) = (np.max(x), np.max(y))
                cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

                # configuration for tesseract
                config = ('-l eng --oem 1 --psm 3')
                text = pytesseract.image_to_string(cropped, config=config)
                self.entrance_result.setText(text)
                img = cv2.resize(img, (320, 150))
                Qimg1 = QImage(img.data, 320, 150, QImage.Format_RGB888)
                Qimg2 = QImage(new_image.data, 320, 100, QImage.Format_RGB888)
                self.entrance_capture_1.setPixmap(QPixmap.fromImage(Qimg1))
                self.entrance_capture_2.setPixmap(QPixmap.fromImage(Qimg2))
                return None
            except:
                self.entrance_result.setText('Error Detected')

    def capture_exit(self):
        if self.ret1:
            image_path = os.path.join(os.getcwd(), 'images/exit.png')
            cv2.imwrite(image_path, self.img2)

        if os.path.isfile(image_path):
            img = cv2.imread(image_path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (320, 150))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(gray, 13, 15, 15)

            edged = cv2.Canny(gray, 30, 200)
            contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None
            try:
                for c in contours:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

                    if len(approx) == 4:
                        screenCnt = approx
                        break

                if screenCnt is None:
                    detected = 0
                    self.detected_exit = False
                    self.exit_result.setText("Error Detected")
                else:
                    self.detected_entrance = True
                    detected = 1

                if detected == 1:
                    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

                mask = np.zeros(gray.shape, np.uint8)
                new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
                new_image = cv2.bitwise_and(img, img, mask=mask)

                (x, y) = np.where(mask == 255)
                (topx, topy) = (np.min(x), np.min(y))
                (bottomx, bottomy) = (np.max(x), np.max(y))
                cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

                # configuration for tesseract
                config = '-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3'
                text = pytesseract.image_to_string(cropped, config=config, lang='eng')
                self.exit_result.setText(text)
                img = cv2.resize(img, (320, 150))
                Qimg1 = QImage(img.data, 320, 150, QImage.Format_RGB888)
                Qimg2 = QImage(new_image.data, 320, 100, QImage.Format_RGB888)
                self.exit_capture_1.setPixmap(QPixmap.fromImage(Qimg1))
                self.exit_capture_2.setPixmap(QPixmap.fromImage(Qimg2))
                return None
            except:
                self.exit_result.setText('Error Detected')

    def entrance_thread_capture(self):
        if self.camera_connection:
            worker = Worker(
                lambda: MainFunctions.capture_entrance(self))  # Any other args, kwargs are passed to the run function
            self.entrance_thread.start(worker)
        else:
            error_message = 'Connected to Camera First.\n' \
                            'Please try again.'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                return

    def exit_thread_capture(self):
        if self.camera_connection:
            worker = Worker(
                lambda: MainFunctions.capture_exit(self))  # Any other args, kwargs are passed to the run function
            self.exit_thread.start(worker)
        else:
            error_message = 'Connected to Camera First.\n' \
                            'Please try again.'
            dialog = CustomMessageInformation(error_message)
            if dialog.exec_():
                return

    def start_camera(self):
        try:
            self.ret0, self.img1 = self.entrance_cam.read()
            self.ret1, self.img2 = self.exit_cam.read()

            if self.btn_connect_cam.isChecked():
                self.img1 = cv2.resize(self.img1, (500, 480), interpolation=cv2.INTER_AREA)
                self.img2 = cv2.resize(self.img2, (500, 480), interpolation=cv2.INTER_AREA)
                self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
                self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2RGB)
                qimg1 = QImage(self.img1.data, 500, 480, QImage.Format_RGB888)
                qimg2 = QImage(self.img2.data, 500, 480, QImage.Format_RGB888)
                self.entrance_view.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.exit_view.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.entrance_view.setPixmap(QPixmap.fromImage(qimg1))
                self.exit_view.setPixmap(QPixmap.fromImage(qimg2))
        except:
            self.camera_connection = False

    def check_entrance_result(self):
        if (self.entrance_result.text() is not None or
                self.entrance_result.text() != 'Error Detected'):
            self.accept_entrance.setChecked(True)
        self.accept_entrance.setChecked(False)

    def check_exit_result(self):
        if (self.exit_result.text() is not None or
                self.exit_result.text() != 'Error Detected'):
            self.accept_exit.setChecked(True)
        self.accept_entrance.setChecked(False)

    def current_time(self):
        # get the current local time in hh:mm:ss format
        current_time = time.strftime('%H:%M:%S')
        self.lcdNumber.display(current_time)

    def ui_definitions(self):
        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)
        self.lcdNumber.setDigitCount(8)
        style_str = 'QWidget {border-color: transparent; ' \
                    'color: #000000;}'
        self.lcdNumber.setStyleSheet(style_str)
