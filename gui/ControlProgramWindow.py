# -*- coding: utf-8 -*-

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMainWindow, QTextCursor

from ControlSystem import CMD_MINIMAL, CMD_NOMINAL, CMD_OPERATING, CMD_ENABLE_BROADCASTING, CMD_DISABLE_BROADCASTING, \
    CMD_SET_REAL_TIME, CMD_ENABLE_DEVICE, CMD_DISABLE_DEVICE, CMD_TRANSCEIVER_SELECT
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
        self.connect(self.ui_main_window.enable_broadcasting_pushButton,
                     SIGNAL("clicked()"), self.on_enable_broadcasting)
        self.connect(self.ui_main_window.disable_broadcasting_pushButton,
                     SIGNAL("clicked()"), self.on_disable_broadcasting)
        self.connect(self.ui_main_window.set_real_time_pushButton,
                     SIGNAL("clicked()"), self.on_set_real_time)
        self.connect(self.ui_main_window.device_power_enable_pushButton,
                     SIGNAL("clicked()"), self.on_device_power_enable)
        self.connect(self.ui_main_window.device_power_disable_pushButton,
                     SIGNAL("clicked()"), self.on_device_power_disable)
        self.connect(self.ui_main_window.transceiver_select_pushButton,
                     SIGNAL("clicked()"), self.on_transceiver_select)
        self.connect(self.ui_main_window.exec_command_pushButton,
                     SIGNAL("clicked()"), self.on_exec_command)

    # def check_

    def send_command_with_time_mark(self, command, argument = None):
        if self.ui_main_window.execution_date_time_checkBox.checkState() == 0:
            execution_time = self.ui_main_window.execution_dateTimeEdit.dateTime().toTime_t()
            self.control_system.send_command(command, arg = argument, time_of_execution = execution_time)
        else:
            self.control_system.send_command(command, arg = argument)

    def on_enable_minimal_mode(self):
        self.send_command_with_time_mark(CMD_MINIMAL)

    def on_enable_nominal_mode(self):
        self.send_command_with_time_mark(CMD_NOMINAL)

    def on_enable_operating_mode(self):
        self.send_command_with_time_mark(CMD_OPERATING)

    def on_enable_broadcasting(self):
        self.send_command_with_time_mark(CMD_ENABLE_BROADCASTING)

    def on_disable_broadcasting(self):
        self.send_command_with_time_mark(CMD_DISABLE_BROADCASTING)

    def on_set_real_time(self):
        time = self.ui_main_window.set_real_time_date_TimeEdit.dateTime().toTime_t()
        self.control_system.send_command_with_time_mark(CMD_SET_REAL_TIME, time)

    # def get_combobox_text(combobox):
    #     combobox_index = combobox.currentIndex()
    #     combobox_text =  str(combobox.itemText(combobox_index))
    #     return combobox_text

    def on_device_power_enable(self):
        text_index = self.ui_main_window.device_id_comboBox.currentIndex()
        text = str(self.ui_main_window.device_id_comboBox.itemText(text_index))
        self.send_command_with_time_mark(CMD_ENABLE_DEVICE, text)

    def on_device_power_disable(self):
        text_index = self.ui_main_window.device_id_comboBox.currentIndex()
        text = str(self.ui_main_window.device_id_comboBox.itemText(text_index))
        self.send_command_with_time_mark(CMD_DISABLE_DEVICE, text)

    def on_transceiver_select(self):
        text_index = self.ui_main_window.device_id_comboBox.currentIndex()
        text = str(self.ui_main_window.transceiver_select_comboBox.itemText(text_index))
        self.send_command_with_time_mark(CMD_TRANSCEIVER_SELECT, text)

    def on_exec_command(self):
        command_name = str(self.ui_main_window.command_name_lineEdit.displayText())
        arg_name = str(self.ui_main_window.command_argument_lineEdit.displayText())
        if command_name != "":
            if arg_name == "":
                self.send_command_with_time_mark(command_name)
            else:
                self.send_command_with_time_mark(command_name, arg_name)
