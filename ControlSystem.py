from PyQt4.QtCore import QObject, pyqtSignal

from communication.KISS_Thread import KISS_Thread
from PayloadParser import parse_json_payload, traverse_telemetry
from sound import sound
from telemetry_sharing.push_to_csv import push_to_csv
from telemetry_sharing.push_to_website import push_to_website
from telemetry_sharing.push_to_ftp_server import push_to_ftp_server
import config

CMD_MINIMAL = "CMD_MINIMAL"
CMD_NOMINAL = "CMD_NOMINAL"
CMD_OPERATING = "CMD_OPERATING"
CMD_ENABLE_BROADCASTING = "CMD_ENABLE_TRANSMISSION"
CMD_DISABLE_BROADCASTING = "CMD_DISABLE_TRANSMISSION"
CMD_SET_REAL_TIME = "CMD_SET_REAL_TIME"
CMD_ENABLE_DEVICE = "CMD_ENABLE_DEVICE"
CMD_DISABLE_DEVICE = "CMD_DISABLE_DEVICE"
CMD_TRANSCEIVER_SELECT = "CMD_TRANSCEIVER_SELECT"
CMD_DEVICE_COMMAND = "CMD_DEVICE_COMMAND"


class ControlSystem(QObject):
    payload_received = pyqtSignal("PyQt_PyObject", name="payloadReceived")
    response_received = pyqtSignal("PyQt_PyObject", name="responseReceived")

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self.kiss_thread = KISS_Thread(self)
        self.kiss_thread.start()
        self.kiss_thread.packet_received.connect(self.on_packet_received)

    def send_command(self, cmd, arg=None, time_of_execution=None, device=None):
        self.kiss_thread.send_command(cmd, arg, device, time_of_execution)
        sound.play(sound.CMD_IS_SENT)

    def on_packet_received(self, packet):
        data = parse_json_payload(str(packet))
        if "CmdID" in data:
            self.response_received.emit(data)
            sound.play(sound.CMD_IS_DONE)
            return
        sound.play(sound.TELEMETRY_RECEIVED)
        payload = traverse_telemetry(data)
        # print "payload in linear struct", payload
        self.payload_received.emit(payload)
        print("ON_PACKET_RECEIVED")
        print(data)
        sound.parse_data(data)
        if config.WEB_ENABLED:
            push_to_website(payload)
        if config.CSV_ENABLED:
            push_to_csv(payload)
        if config.FTP_ENABLED:
            push_to_ftp_server()
