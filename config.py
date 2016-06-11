import os

if os.name == 'nt':
    kiss_com_port_number = 5  # Enter Your COM Port Number Here.
    kiss_serial_name = kiss_com_port_number - 1
else:
    kiss_serial_name = "/dev/ttyACM0"

kiss_baudrate = 9600

