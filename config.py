import os

if os.name == 'nt':
    rxq3_com_port_number = 1  # Enter Your COM Port Number Here.
    rxq3_serial_name = rxq3_com_port_number - 1
else:
    rxq3_serial_name = "/dev/tty.Bluetooth-Incoming-Port"
rxq3_baudrate = 19200

if os.name == 'nt':
    kiss_com_port_number = 5  # Enter Your COM Port Number Here.
    kiss_serial_name = kiss_com_port_number - 1
else:
    kiss_serial_name = "/dev/ttyACM0"


kiss_baudrate = 9600

