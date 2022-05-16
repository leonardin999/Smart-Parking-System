from serial.tools.list_ports_windows import comports
from modules import *
import serial.tools.list_ports
from Dialog import CustomSystemConnectionDialog


class SystemFunctions(MainWindow):

    def generated_port(self):
        """
        List all comm port available in devices manager
        """
        ports = serial.tools.list_ports.comports()
        self.comPort = [
            comport.device for comport in serial.tools.list_ports.comports()
        ]
        count = len(self.comPort)
        if count == 0:
            pass
        elif count == 1:
            self.port.addItem(str(self.comPort[0]))
        else:
            self.port.addItem(str(self.commPort[0]))
            self.port.addItem(str(self.commPort[1]))

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
            print(messages)
            self.ser.write(chr(255))
            self.ser.flushInput()
