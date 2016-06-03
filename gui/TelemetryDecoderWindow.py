# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *

from DataPlotter import DataPlotter
from gui.ui_forms import TelemetryDecoderForm


class TelemetryDecoderWindow(QMainWindow):
    """
        GUI for telemetry decoder for miniaturized satellite imitator
    """

    graph_windows = {}
    column_index = {'time': 0, 'CPU_temperature': 1, 'CPU_usage': 2, 'RAM_usage': 3,
                    'payload_module_temperature': 1, 'payload_module_humidity': 2}

    def __init__(self, control_system):
        QMainWindow.__init__(self)
        self.control_system = control_system

        self.data_plotter = DataPlotter(self)

        self.ui_main_window = TelemetryDecoderForm.Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.ui_main_window.undecoded_data_textEdit.moveCursor(QtGui.QTextCursor.End)

        self.connect(self.ui_main_window.communication_rssi_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_communication_rssi)
        self.connect(self.ui_main_window.communication_temperature_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_communication_temperature)
        self.connect(self.ui_main_window.communication_voltage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_communication_voltage)

        self.connect(self.ui_main_window.onboard_computer_CPU_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_on_board_computer_CPU_usage)
        self.connect(self.ui_main_window.onboard_computer_CPU_temperature_checkBox,
                     SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_on_board_computer_CPU_temperature)
        self.connect(self.ui_main_window.onboard_computer_RAM_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_on_board_computer_RAM_usage)

        self.connect(self.ui_main_window.payloads_humidity_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_payloads_humidity)
        self.connect(self.ui_main_window.payloads_temperature_checkBox, SIGNAL("stateChanged(int)"),
                     self.plot_bar_chart_for_payloads_temperature)

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

    def plot_bar_chart_for_communication_rssi(self, state):
        self.toggle_plot(state, "rssi", self.data_plotter.get_rssi_plot)

    def plot_bar_chart_for_communication_temperature(self, state):
        self.toggle_plot(state, "rxq3_temp", self.data_plotter.get_rxq3_temperature_plot)

    def plot_bar_chart_for_communication_voltage(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_rxq3_voltage_plot)

    def plot_bar_chart_for_on_board_computer_CPU_usage(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_on_board_computer_CPU_usage_plot)

    def plot_bar_chart_for_on_board_computer_CPU_temperature(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_on_board_computer_CPU_temperature_plot)

    def plot_bar_chart_for_on_board_computer_RAM_usage(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_on_board_computer_RAM_usage_plot)

    def plot_bar_chart_for_payloads_humidity(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_payloads_humidity_plot)

    def plot_bar_chart_for_payloads_temperature(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_payloads_temperature_plot)
