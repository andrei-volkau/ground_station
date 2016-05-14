# -*- coding: utf-8 -*-
from PyQt4.QtCore import QObject

TYPE_TELEMETRY_PACKET = "telemetry_packet"
TYPE_CMD_NOMINAL = "cmd.nominal"
TYPE_CMD_OPERATING = "cmd.operating"
TYPE_CMD_EMERGENCY = "cmd.emergency"
TYPE_CMD_DISABLE_TRANSMISSION = "cmd.disable_transmission"
TYPE_CMD_ENABLE_TRANSMISSION = "cmd.enable_transmission"


class Event(QObject):
    """This class represent event according to event-driven programming paradigm."""

    def __init__(self, type, data=None):
        QObject.__init__(self)
        self.type = type
        self.data = data

