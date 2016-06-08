# -*- coding: utf-8 -*-

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMainWindow, QTextCursor

from ControlSystem import CMD_MINIMAL, CMD_NOMINAL, CMD_OPERATING, CMD_ENABLE_TRANSMISSION, CMD_DISABLE_TRANSMISSION
from gui.ui_forms import ControlProgramForm


class ControlProgramWindow(QMainWindow):
    """
        GUI for control program for miniaturized satellite imitator
    """
    def __init__(self, control_system):
        QMainWindow.__init__(self)
        self.control_system = control_system
        self.ui_main_window = ControlProgramForm.Ui_MainWindow()
        self.ui_main_window.setupUi(self)
        self.ui_main_window.undecoded_packages_textEdit.moveCursor(QTextCursor.EndOfBlock)

        self.connect(self.ui_main_window.enable_minimal_mode_pushButton,
                     SIGNAL("clicked()"), self.on_enable_minimal_mode)
        self.connect(self.ui_main_window.enable_nominal_mode_pushButton,
                     SIGNAL("clicked()"), self.on_enable_nominal_mode)
        self.connect(self.ui_main_window.enable_operating_mode_pushButton,
                     SIGNAL("clicked()"), self.on_enable_operating_mode)
        # self.connect(self.ui_main_window.toggle_transmission_pushButton,
        #              SIGNAL("clicked()"), self.on_toggle_transmission)

    def on_enable_minimal_mode(self):
        self.control_system.send_command(CMD_MINIMAL)

    def on_enable_nominal_mode(self):
        self.control_system.send_command(CMD_NOMINAL)

    def on_enable_operating_mode(self):
        self.control_system.send_command(CMD_OPERATING)

    def on_toggle_transmission(self):
        if self.ui_main_window.toggle_transmission_comboBox.currentIndex() == 0:
            self.control_system.send_command(CMD_DISABLE_TRANSMISSION)
        else:
            self.control_system.send_command(CMD_ENABLE_TRANSMISSION)
