# -*- coding: utf-8 -*-
import sys

import kiss
import kiss.constants
import kiss.util
from PyQt4 import QtCore

import config
from loggers.error_logger import log_the_error
from loggers.logger import log_the_data

kiss_prot = None


class KISS_thread(QtCore.QThread):
    """This class represent a writer thread, that write data to the serial port's buffer."""

    def __init__(self, parent, reader_thread):
        """Make a instance of the ReaderAndWriterThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        self.reader_thread = reader_thread
        super(KISS_thread, self).__init__(parent)

    def run(self):
        print "connect strted"
        self.connect()
    # currentN = 0
    # t1 = None
    # bytes = 0
    #
    # def time_data(n):
    #     global t1
    #     global bytes
    #     global currentN
    #     if t1 == None:
    #         t1 = time.time()
    #     else:
    #         bytes += n
    #     if currentN == 100:
    #         sec = time.time() - t1
    #         print float(bytes) / sec, bytes, sec
    #         exit()

    # def process_packet(data):
    #     global currentN
    #     currentN += 1
    #
    #     num = int(data[:6])
    #     if num != currentN:
    #         print "Dropped", num - currentN
    #     currentN = num
    #
    #     payload = data[6:]
    #     size = len(payload)
    #     ideal = "".join([chr(i % 25 + 65) for i in range(size)])
    #     if ideal != payload:
    #         print "Data was corrupted"
    #         print data
    #     print "OK", currentN
    #     time_data(len(payload))

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
        print data
        kiss_data = kiss.constants.FEND + kiss.util.escape_special_codes(data) + kiss.constants.FEND
        log_the_data("./telemetry_log_files/BSU_satellite.kss", kiss_data)
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
        print "AX25 data field is", payload
        print "payload variable type", type(payload)
        package_type = payload[0]
        print "package_type variable", package_type
        print "package _type variable type", type(payload)
        dataString = payload[2:]
        print "data string variable", dataString
        package_info = {'package_type': package_type, 'payload': dataString.strip()}
        self.reader_thread.packet_received(package_info)

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
            print "ax.25 is faled"


    def kiss_send_packet(self,message):
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
