import serial

# Assign Arduino's serial port address
#   Windows example
#     usbport = 'COM3'
#   Linux example
#     usbport = '/dev/ttyUSB0'
#   MacOSX example
#     usbport = '/dev/tty.usbserial-FTALLOK2'
usbport = 'COM8'
# Set up serial baud rate
ser = serial.Serial(usbport, 9600, timeout=1)


def read_information():
    """
    reading messages receives from the device response
    """
    if ser.isOpen():
        command = ser.readline().decode()
        print(f'receiver: {command}')


def send_information(messages):
    """
    Encoding messages to send to Serial connected devices
    """
    if ser.isOpen():
        print(messages)
        ser.write(chr(int(messages)).encode())
        ser.flushInput()

import time

while True:
    a = int(input("Enter Number of Slot: "))
    if a in range(1, 13):
        send_information(a)
        time.sleep(0.1)
        read_information()
    else:
        break
