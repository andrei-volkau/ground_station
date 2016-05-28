# -*- coding: utf-8 -*-
import requests
import sys
from PyQt4 import QtCore
from loggers.error_logger import log_the_error


class WEB_request_thread(QtCore.QRunnable):
    """This class represent a writer thread, that write data to the serial port's buffer."""
    def __init__(self, address, data_for_sending):
        """Make a instance of the WriterThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        super(WEB_request_thread, self).__init__()
        self.data = data_for_sending
        self.addr = address


    def run(self):
        try:
            self.send()
        except:
            error_mesage = "It is impossible to access to the WEB-server" + ";" + str(sys.exc_info())
            log_the_error(error_mesage)

    def send(self):
        """Send file to the server.
        Args:
         file_address (str): It is a destination address of the file.
         file_name (str): It is a file name.
        """
        r = requests.post(self.addr, self.data)
        print r.content

