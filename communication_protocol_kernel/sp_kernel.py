# -*- coding: utf-8 -*-
import serial
import time
import config


ser = serial.Serial(config.rxq3_serial_name, config.rxq3_baudrate, timeout=5000)


class SerialProtocol():
    def __init__(self):
        self.sp_startMarker = "<strm>"
        self.sp_stopMarker = "<stpm>"
        self.sp_packetAvailable = False
        self.sp_startMarkerStatus = 0
        self.sp_stopMarkerStatus = 0
        self.sp_dataLength = 0
        self.sp_dataString = ""
        self.sp_package_type = ""

    def sp_Reset(self):
        self.sp_startMarkerStatus = 0
        self.sp_stopMarkerStatus = 0
        self.sp_dataLength = 0
        self.sp_packetAvailable = False
        self.sp_package_type = ""

    def sp_ResetAll(self):
        self.sp_dataString = " "
        self.sp_Reset()

    def read(self):
        if not self.sp_packetAvailable:
            bufferChar = ser.read(1)
            if (self.sp_startMarkerStatus < len(self.sp_startMarker)):
                if ( self.sp_startMarker[self.sp_startMarkerStatus] == bufferChar ):
                    self.sp_startMarkerStatus += 1
                else:
                    self.sp_ResetAll()
            else:
                if not self.sp_package_type:
                    self.sp_package_type = str(bufferChar)
                    return

                if self.sp_dataLength <= 0:
                    self.sp_dataLength = ord(bufferChar)
                    print 'data length: %s' % self.sp_dataLength
                    return

                else:
                    if self.sp_dataLength >= len(self.sp_dataString):
                        self.sp_dataString += str(bufferChar)
                    else:
                        if self.sp_stopMarkerStatus < len(self.sp_stopMarker):
                            if self.sp_stopMarker[self.sp_stopMarkerStatus] == bufferChar:
                                self.sp_stopMarkerStatus += 1
                                if self.sp_stopMarkerStatus == len(self.sp_stopMarker):
                                    print 'data: %s' % self.sp_dataString
                                    print "Package is received"
                                    print "*----------------*"

                                    package_info = {'package_type': self.sp_package_type, 'payload': self.sp_dataString.strip()}

                                    self.sp_Reset()
                                    self.sp_packetAvailable = True

                                    return package_info
                            else:
                                print "Package don't received"
                                print "*----------------*"
                                print "monitoring ..."
                                self.sp_ResetAll()

    def build_packet(self, package_type, message):
        packet = " " + self.sp_startMarker + package_type + chr(int(len(message))) + message + self.sp_stopMarker + " "
        return packet

    def send_packet(self, package_type, message):
        packet = self.build_packet(package_type, message)
        ser.write(packet)
        time.sleep(0.5)