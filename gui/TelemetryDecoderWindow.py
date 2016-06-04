# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

from DataPlotter import DataPlotter
from PayloadParser import *
from gui.ui_forms import TelemetryDecoderForm



class TelemetryDecoderWindow(QMainWindow):
    """
        GUI for telemetry decoder for miniaturized satellite imitator
    """

    graph_windows = {}

    def __init__(self, control_system):
        QMainWindow.__init__(self)
        self.control_system = control_system
        self.control_system.payload_received.connect(self.on_payload_received)

        self.data_plotter = DataPlotter(self)

        self.ui_main_window = TelemetryDecoderForm.Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.ui_main_window.undecoded_data_textEdit.moveCursor(QtGui.QTextCursor.End)


        self.connect(self.ui_main_window.CPU_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_CPU_usage)
        self.connect(self.ui_main_window.CPU_usage_2_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_CPU_2_usage)
        self.connect(self.ui_main_window.CPU_temperature_checkBox,
                     SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_CPU_temperature)
        self.connect(self.ui_main_window.RAM_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_RAM_usage)
        self.connect(self.ui_main_window.HDD_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_HDD_usage)
        self.connect(self.ui_main_window.CPU_plate_temp_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_onboard_computer_HDD_usage)

        # self.connect(self.ui_main_window.payload_temperature_checkBox, SIGNAL("stateChanged(int)"),
        #              self.plot_payload_module_temperature)

    def toggle_plot(self, state, name, func):
        """
            Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
            state become unselected window with real-time graph will be closed.

        Args:
            state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
            to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
            unchecked checkbox.
        """
        if state == 2:
            plot = func()
            self.graph_windows[name] = plot
            plot.resize(1000, 700)
            plot.show()
        else:
            plot = self.graph_windows[name]
            self.graph_windows[name] = None
            if plot is not None:
                plot.close()


    def plot_onboard_computer_CPU_usage(self, state):
        self.toggle_plot(state, "Intel Atom CPU usage of first core", self.data_plotter.get_onboard_computer_CPU_usage_plot)

    def plot_onboard_computer_CPU_2_usage(self, state):
        self.toggle_plot(state, "Intel Atom CPU usage of second core", self.data_plotter.get_onboard_computer_CPU_usage_plot)

    def plot_onboard_computer_CPU_temperature(self, state):
        self.toggle_plot(state, "Chip internal temperature of Intel Atom CPU", self.data_plotter.get_onboard_computer_CPU_temperature_plot)

    def plot_onboard_computer_RAM_usage(self, state):
        self.toggle_plot(state, "RAM usage", self.data_plotter.get_onboard_computer_RAM_usage_plot)

    def plot_onboard_computer_HDD_usage(self, state):
        self.toggle_plot(state, "HDD usage", self.data_plotter.get_onboard_computer_HDD_usage_plot)

    def on_payload_received(self, payload):
        self.ui_main_window.undecoded_data_textEdit.append(str(payload))
        self.ui_main_window.undecoded_data_textEdit.append("----------------------------------------------------")

        self.ui_main_window.CPU_usage_lcdNumber.display(str(payload[SENSOR_OS_CPU0]["val"]))
        self.ui_main_window.CPU_usage_2_lcdNumber.display(str(payload[SENSOR_OS_CPU1]["val"]))
        self.ui_main_window.CPU_temperature_lcdNumber.display(str(payload[SENSOR_CPU_TEMP]["val"]))
        self.ui_main_window.RAM_usage_lcdNumber.display(str(payload[SENSOR_OS_RAM]["val"]))
        self.ui_main_window.HDD_usage_lcdNumber.display(str(payload[SENSOR_OS_DISK]["val"]))
        self.ui_main_window.CPU_plate_temp_lcdNumber.display(str(payload[SENSOR_BOARD_TEMP]["val"]))

        self.ui_main_window.solar_sensor_1_lcdNumber.display(str(payload[SENSOR_LIGHT1]["val"]))
        self.ui_main_window.solar_sensor_2_lcdNumber.display(str(payload[SENSOR_LIGHT2]["val"]))
        self.ui_main_window.solar_sensor_3_lcdNumber.display(str(payload[SENSOR_LIGHT3]["val"]))
        self.ui_main_window.solar_sensor_4_lcdNumber.display(str(payload[SENSOR_LIGHT4]["val"]))
        self.ui_main_window.magnetometer_x_lcdNumber.display(str(payload[SENSOR_MAGNET_X]["val"]))
        self.ui_main_window.magnetometer_y_lcdNumber.display(str(payload[SENSOR_MAGNET_Y]["val"]))
        self.ui_main_window.magnetometer_z_lcdNumber.display(str(payload[SENSOR_MAGNET_Z]["val"]))
        self.ui_main_window.accelerometer_gyroscope_temperature_lcdNumber.display(str(payload[SENSOR_MAGNET_TEMP]["val"]))

        self.ui_main_window.payload_temperature_lcdNumber.display(str(payload[SENSOR_PAYLOAD_TEMP]["val"]))