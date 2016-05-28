from PyQt4.QtCore import QObject

from BarChart import BarChart


class DataPlotter(QObject):
    """
        GUI for telemetry decoder for miniaturized satellite imitator
    """

    column_index = {'time': 0, 'CPU_temperature': 1, 'CPU_usage': 2, 'RAM_usage': 3,
                    'payload_module_temperature': 1, 'payload_module_humidity': 2}

    def __init__(self, parent):
        QObject.__init__(parent)

    def get_data_for_plotting(self, log_file_name, measurement_parameter):
        """
            Get required data from telemetry log file for plotting on a bar chart.

        Args:
            log_file_name (str): Name of telemetry log file.
            measurement_parameter (str): Kind of data, that need to be extracted from telemetry_log.csv file.

        Returns:
            data (list): Data for plotting on a bar chart.
        """

        telemetry_log = open(log_file_name, "r")
        line_quantity = sum(1 for line in telemetry_log)
        telemetry_log.seek(0, 0)
        reader = csv.reader(telemetry_log, delimiter=';', quoting=csv.QUOTE_NONE, dialect=csv.excel_tab)
        data = []
        for row in reader:
            if reader.line_num in range(line_quantity - 11, line_quantity):
                data.append((datetime.datetime.fromtimestamp(float(row[self.column_index['time']])).
                             strftime('%m-%d-%y \n %H:%M:%S'), float(row[self.column_index[measurement_parameter]])))
        telemetry_log.close()
        return data

    def get_rssi_plot(self):
        return BarChart("RSSI of last received packet", "RSSI, dBm",
                        self.get_data_for_plotting(
                                "./telemetry_log_files/Communication_system_telemetry_log.csv",
                                "CPU_temperature"))

    def get_rxq3_temperature_plot(self):
        return DataPlotter("Chip internal temperature of RXQ3 transceiver",
                           "Temperature, Celsius degrees",
                           self.get_data_for_plotting("./telemetry_log_files/Communication_system_telemetry_log.csv",
                                                      "CPU_temperature"))

    def get_rxq3_voltage_plot(self):
        return BarChart("Chip supply voltage of RXQ3 transceiver", "Voltage, mV",
                        self.get_data_for_plotting(
                                "./telemetry_log_files/Communication_system_telemetry_log.csv",
                                "CPU_temperature"))

    def plot_bar_chart_for_on_board_computer_CPU_usage(self, state):
        """Plot a bar chart that represents real-time dependence of value selected with help of checkbox. If checkbox
         state become unselected window with real-time graph will be closed.

        Args:
         state (int): This argument represent state of checkbox after toggling of it by a user. If state is equal
         to number two, it means that user checked checkbox. If state is equal to number zero, it means that user
         unchecked checkbox.
        """
        if state == 2:
            self.windows_with_graphs.append(BarChart("Intel Atom CPU usage", "Usage, %",
                                                     self.get_data_for_plotting(
                                                             "./telemetry_log_files/On-board_computer_telemetry_log.csv",
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
            self.windows_with_graphs.append(
                    BarChart("Chip internal temperature of Intel Atom CPU", "Temperature, Celsius degrees",
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
            self.windows_with_graphs.append(BarChart("RAM usage", "Usage, %",
                                                     self.get_data_for_plotting(
                                                             "./telemetry_log_files/On-board_computer_telemetry_log.csv",
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
            self.windows_with_graphs.append(BarChart("Humidity at the research module", "Humidity, %",
                                                     self.get_data_for_plotting(
                                                             "./telemetry_log_files/Payload_system_telemetry_log.csv",
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
            self.windows_with_graphs.append(
                    BarChart("Temperature at the research module", "Temperature, Celsius degrees",
                             self.get_data_for_plotting("./telemetry_log_files/Payload_system_telemetry_log.csv",
                                                        "CPU_temperature")))
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].resize(1000, 700)
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].show()
        else:
            self.windows_with_graphs[len(self.windows_with_graphs) - 1].close()
            self.windows_with_graphs.pop(len(self.windows_with_graphs) - 1)
