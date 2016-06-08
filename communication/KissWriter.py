import sys
import requests
from PyQt4 import QtCore
from loggers.error_logger import log_the_error


class KissWriter(QtCore.QRunnable):
    def __init__(self, kiss_prot):
        super(KissWriter, self).__init__()
        self.kiss_prot = kiss_prot

    def set_destination(self, ssid):
        self.ssid = ssid

    def set_source(self, ssid):
        None
        # self.ssid = ssid

    def set_data(self, data):
        self.data = data

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

    def run(self):
        packet=self.buildpacket("BSUGS ",0,self.ssid,0,0x03,0xf0,self.data)
        final_packet = ''
        for i in packet:
            final_packet += chr(i)
        print packet
        try:
            self.kiss_prot.write(final_packet)
        except:
            error_message = "Error of packet sending"
            log_the_error(error_message)

