# -*- coding: utf-8 -*-
import sys
from ftplib import FTP

from PyQt4 import QtCore

from loggers.error_logger import log_the_error


class FTP_ServerAPI(QtCore.QRunnable):
    """This class represent a writer thread, that write data to the serial port's buffer."""

    def __init__(self, file_address, file_name):
        """Make a instance of the WriterThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        super(FTP_ServerAPI, self).__init__()
        self.file_address = file_address
        self.file_name = file_name

    def run(self):
        try:
            self.send()
        except:
            error_message = "It is impossible to access to the FTP-server" + ";" + str(sys.exc_info())
            log_the_error(error_message)

    def send(self):
        """Send file to the server.

        Args:
         file_address (str): It is a destination address of the file.
         file_name (str): It is a file name.
        """
        ftp = FTP('192.168.10.44', 'admin', 'admin')
        file_for_sending = open(self.file_address + self.file_name, "r")
        ftp.storbinary("STOR " + self.file_name, file_for_sending)
        ftp.quit()
        file_for_sending.close()
