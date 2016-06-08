# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import QThread, pyqtSignal, QThreadPool

import kiss
import kiss.constants
import kiss.util
from PyQt4 import QtCore

import config
from communication.KissWriter import KissWriter
from loggers.error_logger import log_the_error
from loggers.logger import log_the_data
import time
import json

LOCAL_SSID = "BSUGS "
REMOTE_SSID = "BSUIM "


class KISS_thread(QtCore.QThread):
    """
        AX.25 Communication
    """
    packet_received = pyqtSignal("QString", name="packetReceived")

    def __init__(self, control_system):
        """Make a instance of the ReaderAndWriterThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        QThread.__init__(self, control_system)
        # self.control_system = control_system


    def run(self):
        print "connect strted"
        self.kiss_connect()

    def read_callback(self,data):
        print "read_callback, packet length", len(data)
        kiss_data = kiss.constants.FEND + kiss.util.escape_special_codes(data) + kiss.constants.FEND
        log_the_data("./log_files/telemetry_log_files/BSU_satellite.kss", kiss_data)
        data = data[1:]
        if len(data) < 15:
            print "bad packet"
            return
        dest = "".join([chr(ord(c)>>1) for c in data[:6]])
        #print "Destination", dest
        src = "".join([chr(ord(c)>>1) for c in data[7:13]])
        #print "Source", src
        if dest != LOCAL_SSID:
            print "packet not for us"
            return
        start = 16
        ssid = ord(data[13]) & 1
        if ssid == 0:
            via = "".join([chr(ord(c)>>1) for c in data[7:13]])
            print "Retr", via
            start = 23
        size = len(data) - start
        if size == 0:
            print "packet is empty"
            return
        payload = data[start:]
        # self.control_system.on_packet_received(payload)
        self.packet_received.emit(payload)

    def kiss_connect(self):
        try:
            print "connect"
            self.kiss_prot = kiss.KISS(port=config.kiss_serial_name, speed=config.kiss_baudrate)
            self.kiss_prot.start()
            self.kiss_prot.read(self.read_callback)
        except:
            error_mesage = "Could not open port for CC430 transceiver." + ";" + str(sys.exc_info())
            log_the_error(error_mesage)

            print sys.exc_info()
            print "ax.25 is failed"


    def send_command(self, name, arg = None):
        data = {"Timestamp": int(time.time()), "Cmd": name, "Arg": arg}
        json_data = json.dumps(data)
        writer = KissWriter(self.kiss_prot)
        writer.set_destination(REMOTE_SSID)
        writer.set_data(json_data)
        QThreadPool.globalInstance().start(writer)

