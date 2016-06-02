from PyQt4.QtCore import QObject
from KISS_thread import KISS_thread
from PayloadParser import parse_payload
from network_communication import WEB_request_thread, FTP_thread

CMD_EMERGENCY = "CMD_EMERGENCY"
CMD_NOMINAL = "CMD_NOMINAL"
CMD_OPERATING = "CMD_OPERATING"
CMD_ENABLE_TRANSMISSION = "CMD_ENABLE_TRANSMISSION"
CMD_DISABLE_TRANSMISSION = "CMD_DISABLE_TRANSMISSION"


class ControlSystem(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        # communication_protocol = sp_kernel.SerialProtocol()
        # writer_thread = WriterThread.WriterThread(self, communication_protocol)
        # reader_thread = ReaderThread.ReaderThread(self, communication_protocol)
        kiss_thread = KISS_thread(self)
        # reader_thread.start()
        # writer_thread.start()
        kiss_thread.start()

    def send_command(self, cmd):
        print "Issued command:", cmd

    def on_packet_received(self, payload):
        data = parse_payload(payload)
        print "payload in python map", data
        # WEB_request_thread('http://sputnik-bsu.herokuapp.com/api/v1/sensors', )

        #FTP_thread()


