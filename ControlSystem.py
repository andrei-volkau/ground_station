from PyQt4.QtCore import QObject, pyqtSignal

from communication.KISS_thread import KISS_thread
from PayloadParser import parse_ax25_payload
from telemetry_sharing.push_to_csv import push_to_csv
from telemetry_sharing.push_to_website import push_to_website

CMD_MINIMAL = "CMD_MINIMAL"
CMD_NOMINAL = "CMD_NOMINAL"
CMD_OPERATING = "CMD_OPERATING"
CMD_ENABLE_BROADCASTING = "CMD_ENABLE_TRANSMISSION"
CMD_DISABLE_BROADCASTING = "CMD_DISABLE_TRANSMISSION"
CMD_SET_REAL_TIME = "CMD_SET_REAL_TIME"


class ControlSystem(QObject):
    payload_received = pyqtSignal("PyQt_PyObject", name="payloadReceived")

    def __init__(self, parent):
        QObject.__init__(self, parent)
        # communication_protocol = sp_kernel.SerialProtocol()
        # writer_thread = WriterThread.WriterThread(self, communication_protocol)
        # reader_thread = ReaderThread.ReaderThread(self, communication_protocol)
        self.kiss_thread = KISS_thread(self)
        # reader_thread.start()
        # writer_thread.start()
        self.kiss_thread.start()
        self.kiss_thread.packet_received.connect(self.on_packet_received)

    def send_command(self, cmd, arg = None, time_of_execution = None):
         self.kiss_thread.send_command(cmd, arg, time_of_execution)


    def on_packet_received(self, packet):
        payload = parse_ax25_payload(str(packet))
        print "payload in linear struct", payload
        self.payload_received.emit(payload)
        push_to_website(payload)
        push_to_csv(payload)


