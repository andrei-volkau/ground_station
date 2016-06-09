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
                     self.on_plot_CPU_0_usage)
        self.connect(self.ui_main_window.CPU_usage_2_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_CPU_1_usage)
        self.connect(self.ui_main_window.CPU_temperature_checkBox,
                     SIGNAL("stateChanged(int)"),
                     self.on_plot_CPU_temperature)
        self.connect(self.ui_main_window.RAM_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_RAM_usage)
        self.connect(self.ui_main_window.HDD_usage_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_HDD_usage)
        self.connect(self.ui_main_window.CPU_plate_temp_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_cpu_board_temp)
        self.connect(self.ui_main_window.solar_sensor_1_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_solar_sensor_1)
        self.connect(self.ui_main_window.solar_sensor_2_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_solar_sensor_2)
        self.connect(self.ui_main_window.solar_sensor_3_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_solar_sensor_3)
        self.connect(self.ui_main_window.solar_sensor_4_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_solar_sensor_4)
        self.connect(self.ui_main_window.magnetometer_x_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_magnetometer_x)
        self.connect(self.ui_main_window.magnetometer_y_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_magnetometer_y)
        self.connect(self.ui_main_window.magnetometer_z_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_magnetometer_z)
        self.connect(self.ui_main_window.accelerometer_gyroscope_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_accelerometer_gyroscope_temperature)
        self.connect(self.ui_main_window.payload_temperature_checkBox, SIGNAL("stateChanged(int)"),
                     self.on_plot_payload_temperature)



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


    def on_plot_CPU_0_usage(self, state):
        self.toggle_plot(state, SENSOR_OS_CPU0 , self.data_plotter.get_CPU_0_usage_plot)

    def on_plot_CPU_1_usage(self, state):
        self.toggle_plot(state, SENSOR_OS_CPU1, self.data_plotter.get_CPU_1_usage_plot)

    def on_plot_CPU_temperature(self, state):
        self.toggle_plot(state, SENSOR_CPU_TEMP, self.data_plotter.get_CPU_temperature_plot)

    def on_plot_RAM_usage(self, state):
        self.toggle_plot(state, SENSOR_OS_RAM, self.data_plotter.get_RAM_usage_plot)

    def on_plot_HDD_usage(self, state):
        self.toggle_plot(state, SENSOR_OS_DISK, self.data_plotter.get_HDD_usage_plot)

    def on_plot_cpu_board_temp(self, state):
        self.toggle_plot(state, SENSOR_BOARD_TEMP, self.data_plotter.get_cpu_board_temp_plot)

    def on_plot_solar_sensor_1(self, state):
        self.toggle_plot(state, SENSOR_LIGHT1, self.data_plotter.get_solar_sensor_1_plot)

    def on_plot_solar_sensor_2(self, state):
        self.toggle_plot(state, SENSOR_LIGHT2, self.data_plotter.get_solar_sensor_2_plot)

    def on_plot_solar_sensor_3(self, state):
        self.toggle_plot(state, SENSOR_LIGHT3, self.data_plotter.get_solar_sensor_3_plot)

    def on_plot_solar_sensor_4(self, state):
        self.toggle_plot(state, SENSOR_LIGHT4, self.data_plotter.get_solar_sensor_4_plot)

    def on_plot_magnetometer_x(self, state):
        self.toggle_plot(state, SENSOR_MAGNET_X, self.data_plotter.get_magnetometer_x_plot)

    def on_plot_magnetometer_y(self, state):
        self.toggle_plot(state, SENSOR_MAGNET_Y, self.data_plotter.get_magnetometer_y_plot)

    def on_plot_magnetometer_z(self, state):
        self.toggle_plot(state, SENSOR_MAGNET_Z, self.data_plotter.get_magnetometer_z_plot)

    def on_plot_accelerometer_gyroscope_temperature(self, state):
        self.toggle_plot(state, SENSOR_ACCELEROMETER_GYROSCOPE_TEMP, self.data_plotter.get_accelerometer_gyroscope_temperature_plot)

    def on_plot_payload_temperature(self, state):
        self.toggle_plot(state, SENSOR_PAYLOAD_TEMP, self.data_plotter.get_payload_module_temperature_plot)

    def get_value(self, payload, sensor):
        if sensor in payload:
            return str(payload[sensor]["val"])
        return ""

    def on_payload_received(self, payload):
        self.ui_main_window.undecoded_data_textEdit.append(str(payload))
        self.ui_main_window.undecoded_data_textEdit.append("----------------------------------------------------")

        self.ui_main_window.CPU_usage_lcdNumber.display(self.get_value(payload, SENSOR_OS_CPU0))
        self.ui_main_window.CPU_usage_2_lcdNumber.display(self.get_value(payload, SENSOR_OS_CPU1))
        self.ui_main_window.CPU_temperature_lcdNumber.display(self.get_value(payload, SENSOR_CPU_TEMP))
        self.ui_main_window.RAM_usage_lcdNumber.display(self.get_value(payload, SENSOR_OS_RAM))
        self.ui_main_window.HDD_usage_lcdNumber.display(self.get_value(payload, SENSOR_OS_DISK))
        self.ui_main_window.CPU_plate_temp_lcdNumber.display(self.get_value(payload, SENSOR_BOARD_TEMP))

        self.ui_main_window.solar_sensor_1_lcdNumber.display(self.get_value(payload, SENSOR_LIGHT1))
        self.ui_main_window.solar_sensor_2_lcdNumber.display(self.get_value(payload, SENSOR_LIGHT2))
        self.ui_main_window.solar_sensor_3_lcdNumber.display(self.get_value(payload, SENSOR_LIGHT3))
        self.ui_main_window.solar_sensor_4_lcdNumber.display(self.get_value(payload, SENSOR_LIGHT4))
        self.ui_main_window.magnetometer_x_lcdNumber.display(self.get_value(payload, SENSOR_MAGNET_X))
        self.ui_main_window.magnetometer_y_lcdNumber.display(self.get_value(payload, SENSOR_MAGNET_Y))
        self.ui_main_window.magnetometer_z_lcdNumber.display(self.get_value(payload, SENSOR_MAGNET_Z))
        self.ui_main_window.accelerometer_gyroscope_temperature_lcdNumber.display(self.get_value(payload, SENSOR_ACCELEROMETER_GYROSCOPE_TEMP))

        self.ui_main_window.payload_temperature_lcdNumber.display(self.get_value(payload, SENSOR_PAYLOAD_TEMP))
