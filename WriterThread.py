# -*- coding: utf-8 -*-
from PyQt4 import QtCore
import winsound


class WriterThread(QtCore.QThread):
    """This class represent a writer thread, that write data to the serial port's buffer."""
    def __init__(self, protocol):
        """Make a instance of the WriterThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        super(WriterThread, self).__init__()
        self.communication_protocol = protocol

    def send_command(self, name, arg=None):
        """Send command to the miniaturized satellite simulator."""
        if arg is not None:
            data = '1;1;%s;%s' % name, str(arg)
        else:
            data = '1;1;%s' % name
        self.communication_protocol.send_packet('c', data)
        winsound.PlaySound('./sound_files/command_is_sent.wav', winsound.SND_FILENAME)

    def enable_emergency_mode(self):
        """Enable emergency mode of work for miniaturized satellite simulator."""
        self.send_command("m")

    def enable_nominal_mode(self):
        """Enable nominal mode of work for miniaturized satellite simulator."""
        self.send_command("q")

    def enable_operating_mode(self):
        """Enable operating mode of work for miniaturized satellite simulator."""
        self.send_command("z")

    def disable_enable_transmission(self):
        """Disable or enable transmission of any packages in any mode of work for the miniaturized satellite simulator."""
        if self.ui_main_window.data_handling_disable_enable_transmission_comboBox.currentText() == "Disable":
            self.send_command("a")
        elif self.ui_main_window.data_handling_disable_enable_transmission_comboBox.currentText() == "Enable":
            self.send_command("b")