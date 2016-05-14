# -*- coding: utf-8 -*-
import csv
import datetime
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
from UI_forms import telemetry_decoder_form
from bar_chart_plotter import DataPlotter


class GUI_for_telemetry_decoder(QtGui.QMainWindow):
    """This class represent graphical user interface(GUI) of telemetry decoder for miniaturized satellite simulator.

    Attributes:
        ui_main_window (Ui_MainWindow): Main window as first of two parts of graphical user interface.
        windows_with_graphs (list): Windows that represents time-dependent graphs of value selected with help of
                                    checkboxes.
        column_index (dict): Column index of telemetry data at log files.
    """
    ui_main_window = None
    windows_with_graphs = []
    column_index = {'time': 0, 'CPU_temperature': 1, 'CPU_usage': 2, 'RAM_usage': 3, \
                                'payload_module_temperature': 1,'payload_module_humidity': 2}

    def __init__(self):
        """Constructor."""
        QtGui.QMainWindow.__init__(self)
        self.ui_main_window = telemetry_decoder_form.Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.ui_main_window.undecoded_data_textEdit.moveCursor(QtGui.QTextCursor.End)

        QtCore.QObject.connect(self.ui_main_window.communication_rssi_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_communication_rssi)
        QtCore.QObject.connect(self.ui_main_window.communication_temperature_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_communication_temperature)
        QtCore.QObject.connect(self.ui_main_window.communication_voltage_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_communication_voltage)

        QtCore.QObject.connect(self.ui_main_window.onboard_computer_CPU_usage_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_on_board_computer_CPU_usage)
        QtCore.QObject.connect(self.ui_main_window.onboard_computer_CPU_temperature_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_on_board_computer_CPU_temperature)
        QtCore.QObject.connect(self.ui_main_window.onboard_computer_RAM_usage_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_on_board_computer_RAM_usage)

        QtCore.QObject.connect(self.ui_main_window.payloads_humidity_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_payloads_humidity)
        QtCore.QObject.connect(self.ui_main_window.payloads_temperature_checkBox, SIGNAL("stateChanged(int)"),
                               self.plot_bar_chart_for_payloads_temperature)

    def get_data_for_plotting(self, log_file_name, measurement_parameter):
        """Get required data from required telemetry log file for plotting of a bar chart.

        Args:
         log_file_name (str): Name of required telemetry log file.
         measurement_parameter (str): This argument represent required kind of data, that need to be extracted from
            telemetry_log.csv file.

        Returns:
         data (list): Data for plotting of a bar chart.
        """
        telemetry_log = open(log_file_name, "r")
        line_quantity = sum(1 for line in telemetry_log)
        telemetry_log.seek(0, 0)
        reader = csv.reader(telemetry_log, delimiter=';', quoting=csv.QUOTE_NONE, dialect=csv.excel_tab)
        data = []
        for row in reader:
            if reader.line_num in range(line_quantity-11, line_quantity):
                data.append((datetime.datetime.fromtimestamp(float(row[self.column_index['time']])).
                             strftime('%m-%d-%y \n %H:%M:%S'), float(row[self.column_index[measurement_parameter]])))
        telemetry_log.close()
        print data
        return data

    def plot_bar_chart_for_communication_rssi(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("RSSI of last received packet", "RSSI, dBm",
                                                        self.get_data_for_plotting("./telemetry_log_files/Communication_system_telemetry_log.csv",
                                                                                   "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1200, 600)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()

        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_communication_temperature(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Chip internal temperature of RXQ3 transceiver",
                                                        "Temperature, Celsius degrees",
                                                        self.get_data_for_plotting("./telemetry_log_files/Communication_system_telemetry_log.csv",
                                                                                   "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_communication_voltage(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Chip supply voltage of RXQ3 transceiver", "Voltage, mV",
                                                        self.get_data_for_plotting("./telemetry_log_files/Communication_system_telemetry_log.csv",
                                                                                   "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_on_board_computer_CPU_usage(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Intel Atom CPU usage", "Usage, %",
                                                        self.get_data_for_plotting("./telemetry_log_files/On-board_computer_telemetry_log.csv",
                                                                                   "CPU_usage")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()

        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_on_board_computer_CPU_temperature(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Chip internal temperature of Intel Atom CPU", "Temperature, Celsius degrees",
                                                        self.get_data_for_plotting("./telemetry_log_files/On-board_computer_telemetry_log.csv",
                                                                                   "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_on_board_computer_RAM_usage(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("RAM usage", "Usage, %",
                                                        self.get_data_for_plotting("./telemetry_log_files/On-board_computer_telemetry_log.csv",
                                                                                   "RAM_usage")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_payloads_humidity(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Humidity at the research module", "Humidity, %",
                                                        self.get_data_for_plotting("./telemetry_log_files/Payload_system_telemetry_log.csv",
                                                                                   "payload_module_humidity")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)

    def plot_bar_chart_for_payloads_temperature(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(DataPlotter("Temperature at the research module", "Temperature, Celsius degrees",
                                                        self.get_data_for_plotting("./telemetry_log_files/Payload_system_telemetry_log.csv",
                                                                                   "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)




