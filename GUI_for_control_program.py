# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
from UI_forms import control_program_form
import  event

class GUI_for_control_program(QtGui.QMainWindow):
    """This class represent graphical user interface(GUI) of control program for miniaturized satellite simulator.

    Attributes:
        ui_main_window (Ui_MainWindow): Frontend of control program.
        windows_with_graphs (list): Windows that represents time-dependent bar chart of value selected with help of
                                    checkboxes.
    """

    def enable_emergency_mode(self):
        self.eventManager.sendControlSignal(event.Event(event.TYPE_CMD_EMERGENCY))

    def enable_nominal_mode(self):
        self.eventManager.sendControlSignal(event.Event(event.TYPE_CMD_NOMINAL))

    def enable_operating_mode(self):
        self.eventManager.sendControlSignal(event.Event(event.TYPE_CMD_OPERATING))

    def disable_enable_transmission(self):
        self.eventManager.sendControlSignal(event.Event(event.TYPE_CMD_ENABLE_TRANSMISSION))

    def __init__(self, eventManager):
        """Constructor."""
        self.eventManager = eventManager
        QtGui.QMainWindow.__init__(self)
        self.ui_main_window = control_program_form.Ui_MainWindow()
        self.ui_main_window.setupUi(self)
        self.ui_main_window.undecoded_data_from_packages_textEdit.moveCursor(QtGui.QTextCursor.EndOfBlock)

        QtCore.QObject.connect(self.ui_main_window.modes_enable_emergency_mode_send_pushButton,
                               SIGNAL("clicked()"), self.enable_emergency_mode)
        QtCore.QObject.connect(self.ui_main_window.modes_enable_nominal_mode_send_pushButton,
                               SIGNAL("clicked()"), self.enable_nominal_mode)
        QtCore.QObject.connect(self.ui_main_window.modes_enable_operating_mode_send_pushButton,
                               SIGNAL("clicked()"), self.enable_operating_mode)
        QtCore.QObject.connect(self.ui_main_window.data_handling_disable_enable_transmission_pushButton,
                               SIGNAL("clicked()"), self.disable_enable_transmission)
