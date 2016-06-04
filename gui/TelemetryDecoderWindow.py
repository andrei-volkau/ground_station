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
        self.toggle_plot(state, "Загруженность 1-го ядра ЦП ", self.data_plotter.get_onboard_computer_CPU_usage_plot)

    def plot_onboard_computer_CPU_2_usage(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_onboard_computer_CPU_usage_plot)

    def plot_onboard_computer_CPU_temperature(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_onboard_computer_CPU_temperature_plot)

    def plot_onboard_computer_RAM_usage(self, state):
        self.toggle_plot(state, "rxq3_voltage", self.data_plotter.get_onboard_computer_RAM_usage_plot)

    def on_payload_received(self, linearPayload):
        self.ui_main_window.undecoded_data_textEdit.append(str(linearPayload))
        self.ui_main_window.undecoded_data_textEdit.append("----------------------------------------------------")

        self.ui_main_window.CPU_usage_lcdNumber.display(str(linearPayload["tel_os_info.py_cpu_0"]))
        self.ui_main_window.CPU_usage_2_lcdNumber.display(str(linearPayload["tel_os_info.py_cpu_1"]))
        self.ui_main_window.CPU_temperature_lcdNumber.display(str(linearPayload["tel_cpu_temp_c"]))
        self.ui_main_window.RAM_usage_lcdNumber.display(str(linearPayload["tel_os_info.py_ram"]))
        self.ui_main_window.HDD_usage_lcdNumber.display(str(linearPayload["tel_os_info.py_disk"]))
        self.ui_main_window.CPU_plate_temp_lcdNumber.display(str(linearPayload["tel_cpu_temp_p"]))

        self.ui_main_window.solar_sensor_1_lcdNumber.display(str(linearPayload["tel_light_1"]))
        self.ui_main_window.solar_sensor_2_lcdNumber.display(str(linearPayload["tel_light_2"]))
        self.ui_main_window.solar_sensor_3_lcdNumber.display(str(linearPayload["tel_light_3"]))
        self.ui_main_window.solar_sensor_4_lcdNumber.display(str(linearPayload["tel_light_4"]))
        self.ui_main_window.magnetometer_x_lcdNumber.display(str(linearPayload["tel_hmc5883l_x"]))
        self.ui_main_window.magnetometer_y_lcdNumber.display(str(linearPayload["tel_hmc5883l_y"]))
        self.ui_main_window.magnetometer_z_lcdNumber.display(str(linearPayload["tel_hmc5883l_z"]))
        self.ui_main_window.accelerometer_gyroscope_temperature_lcdNumber.display(str(linearPayload["tel_ms5611_temp"]))

        self.ui_main_window.payload_temperature_lcdNumber.display(str(linearPayload["tel_ds1621"]))