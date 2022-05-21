import time

from modules import *
import serial.tools.list_ports
from Dialog import CustomSystemConnectionDialog, CustomMessageInformation

class SystemFunctions(MainWindow):

    def generated_port(self):
        """
        List all comm port available in devices manager
        """
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'Arduino' in p.description:
                self.comPort.append(p.device)
        self.port.addItems(self.comPort)

    def connectInitial(self, port, baud):
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
        self.ser.parity = serial.PARITY_NONE  # set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        self.ser.xonxoff = False  # disable software flow control
        self.ser.rtscts = False  # disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 0  # timeout for write
        self.ser.timeout = 10
        self.ser.open()

    def system_connected(self):
        try:
            port = self.port.currentText()
            baud = self.baud.currentText()
            SystemFunctions.connectInitial(self, port, baud)
            self.connected = True
            if self.ser.isOpen():
                self.btn_connect.setText("disconnect")
            return
        except:
            dialog = CustomSystemConnectionDialog()
            if dialog.exec_():
                self.connected = False
            else:
                self.connected = False

    def system_disconnected(self):
        self.connected = False
        if self.ser.isOpen():
            self.ser.close()
            self.btn_connect.setText("connect")
        else:
            self.connected = False
            self.btn_connect.setText("connect")

    def option_check(self):
        if not self.connected:
            SystemFunctions.system_connected(self)
        else:
            SystemFunctions.system_disconnected(self)

    def read_information(self):
        """
        reading messages receives from the device response
        """
        if self.ser.isOpen():
            data = self.ser.readline().decode()
            self.command = data.strip()
            if self.command:
                self.comand_edit.setText(self.command)

    def send_information(self, messages):
        """
        Encoding messages to send to Serial connected devices
        """
        if self.ser.isOpen():
            if messages:
                self.ser.write(chr(int(messages)).encode())
                self.ser.flushInput()
                time.sleep(0.3)
            else:
                error_message = f'Invalid Command.\n' \
                                f'Please try again.'
                dialog = CustomMessageInformation(error_message)
                if dialog.exec_():
                    return
