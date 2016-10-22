# -*- coding: utf-8 -*-
import serial.tools.list_ports
from loggers.error_logger import log_the_error

def get_kiss_serial_name():
    # Get available serial ports
    port_list = serial.tools.list_ports.comports()
    if not port_list:
        print u"Ошибка: Не обнаружено последовательных портов. Подключите, пожалуйста, пакетный контроллер!"
        raw_input()
        log_the_error("No serial ports found")
        exit()
    
    # Select appropriate ports
    kiss_port_list = [ x for x in port_list if x.vid == 1105 and x.pid == 62514 ]
    if not kiss_port_list:
        print u"Ошибка: Не обнаружено подходящих последовательных портов. Подключите, пожалуйста, пакетный контроллер!"
        raw_input()
        log_the_error("No MSP430 devices found")
        exit()
    
    # Check whether there are several appropriate ports
    selected_port = 0
    if len(kiss_port_list) > 1:
        # Ask user to select one
        print u"Обнаружено несколько подходящих портов:"
        for index, obj in enumerate(kiss_port_list):
            print u"{0}. {1} ({2})".format(index+1, obj.description, obj.device)

        while selected_port not in range(1, len(kiss_port_list)+1):
            selected_port = input(u"Введите номер порта: ")

        selected_port -= 1
        
    kiss_port = kiss_port_list[selected_port].device
    print u"Используется порт "+kiss_port
    return kiss_port

kiss_serial_name = get_kiss_serial_name()
kiss_baudrate = 9600
SOUND_ENABLED = False
FTP_ENABLED = False
CSV_ENABLED = True
WEB_ENABLED = False
