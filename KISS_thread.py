# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import QThread, pyqtSignal

import kiss
import kiss.constants
import kiss.util
from PyQt4 import QtCore

import config
from loggers.error_logger import log_the_error
from loggers.logger import log_the_data

kiss_prot = None


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
        self.connect()

    def buildpacket(self,source,source_ssid,dest,dest_ssid,control,pid,payload):
        packet=[]
        for j in range(6):
            if j<len(dest):
                c=ord(dest[j])
                packet.append(c<<1)
            else:
                packet.append(0x40)
        packet.append(0x60|(dest_ssid<<1))
        for j in range(6):
            if j<len(source):
                c=ord(source[j])
                packet.append(c<<1)
            else:
                packet.append(0x40)
        packet.append(0xe1|(source_ssid<<1))
        packet.append(control)
        packet.append(pid)
        for j in range(len(payload)):
            packet.append(ord(payload[j]))
        return packet

    def read_callback(self,data):
        print "read_callback"
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
        if dest != "BSUGS ":
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

    def connect(self):
        try:
            print "connect"
            global kiss_prot
            kiss_prot = kiss.KISS(port=config.kiss_serial_name, speed=config.kiss_baudrate)
            kiss_prot.start()
            kiss_prot.read(self.read_callback)
        except:
            error_mesage = "Could not open port for CC430 transceiver." + ";" + str(sys.exc_info())
            log_the_error(error_mesage)

            print sys.exc_info()
            print "ax.25 is failed"


    def kiss_send_packet(self, message):
        packet=self.buildpacket("BSUIM",0,"CQ",0,0x03,0xf0,message)
        final_packet = ''
        for i in packet:
            final_packet += chr(i)
        print packet
        try:
            global kiss_prot
            kiss_prot.write(final_packet)
        except:
            self.connect()
