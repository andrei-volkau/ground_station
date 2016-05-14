# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui
from EventManager import EventManager
from GUI_for_telemetry_decoder import GUI_for_telemetry_decoder
from GUI_for_control_program import GUI_for_control_program
from control_system import ControlSystem


app = QtGui.QApplication(sys.argv)
event_manager = EventManager()

telemetry_decoder = GUI_for_telemetry_decoder(event_manager)
control_program = GUI_for_control_program(event_manager)

control_system = ControlSystem(event_manager)

telemetry_decoder.show()
control_program.show()

app.exec_()
