#!/usr/bin/env python2
import sys

from PyQt4.QtGui import QApplication

from ControlSystem import ControlSystem
from gui.ControlProgramWindow import ControlProgramWindow
from gui.TelemetryDecoderWindow import TelemetryDecoderWindow

app = QApplication(sys.argv)
control_system = ControlSystem(app)

telemetry_window = ControlProgramWindow(control_system)
control_window = TelemetryDecoderWindow(control_system)

telemetry_window.show()
control_window.show()

sys.exit(app.exec_())
