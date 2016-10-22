# -*- coding: utf-8 -*-
import sys
import time
import json

from PyQt4.QtCore import QThread, pyqtSignal, QThreadPool
import kiss
import kiss.constants
import kiss.util
from PyQt4 import QtCore

import config
from communication.KissWriter import KissWriter
from loggers.error_logger import log_the_error
from loggers.logger import log_the_data
from sound import sound


LOCAL_SSID = "BSUGS"
REMOTE_SSID = "BSUIM"


class KISS_Thread(QtCore.QThread):
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
        self.writer_thread = QThreadPool(self)
        self.writer_thread.setMaxThreadCount(1)

    def run(self):
        print "kiss started"
        self.kiss_connect()

    def read_callback(self, data):
        print "received packet, len", len(data)
        kiss_data = kiss.constants.FEND + kiss.util.escape_special_codes(data) + kiss.constants.FEND
        log_the_data("./log_files/telemetry_log_files/BSU_satellite.kss", kiss_data)
        data = data[1:]
        if len(data) < 15:
            print "bad packet"
            return
        dest = "".join([chr(ord(c) >> 1) for c in data[:6]])
        # print "Destination", dest
        src = "".join([chr(ord(c) >> 1) for c in data[7:13]])
        #print "Source", src
        if not dest.startswith(LOCAL_SSID):
            print "packet not for us"
            return
        start = 16
        ssid = ord(data[13]) & 1
        if ssid == 0:
            via = "".join([chr(ord(c) >> 1) for c in data[7:13]])
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
            error_mesage = "CANNOT OPEN PORT"
            log_the_error(error_mesage)
            sound.play(error_mesage)

            print sys.exc_info()
            print "ax.25 is failed"


    def send_command(self, name, arg, device, time_of_execution):
        data = {
            "Timestamp": int(time.time()),
            "Schedule": time_of_execution,
            "Cmd": name,
            "Arg": arg,
            "Device": device
        }
        json_data = json.dumps(data)

        print "Formed packet", json_data
        writer = KissWriter(self.kiss_prot, LOCAL_SSID, REMOTE_SSID)
        writer.set_data(json_data)
        self.writer_thread.start(writer)

