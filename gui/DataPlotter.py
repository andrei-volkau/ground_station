from PyQt4.QtCore import QObject
from BarChart import BarChart
import csv
import datetime


column_index = {'time': 0, 'CPU_temperature': 1, 'CPU_usage': 2, 'RAM_usage': 3,
                    'payload_module_temperature': 1, 'payload_module_humidity': 2}
PAYLOAD_LOG_ADR = "./log_files/telemetry_log_files/Payload_system_telemetry_log.csv"
ONBOARD_COMPUTER_LOG_ADR = "./log_files/telemetry_log_files/On-board_computer_telemetry_log.csv"
COMMUNICATION_LOG_ADR = "./log_files/telemetry_log_files/Communication_system_telemetry_log.csv"


class DataPlotter(QObject):
    """
        GUI for telemetry decoder for miniaturized satellite imitator
    """

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
        lines = [line for line in telemetry_log]
        telemetry_log.close()
        lines = lines[-11:]
        reader = csv.reader(lines, delimiter=';', quoting=csv.QUOTE_NONE, dialect=csv.excel_tab)
        data = []
        for row in reader:
            time = datetime.datetime.fromtimestamp(float(row[self.column_index['time']])).strftime('%m-%d-%y \n %H:%M:%S')
            param = float(row[self.column_index[measurement_parameter]])
            data.append((time, param))
        return data

    def get_rssi_plot(self):
        return BarChart("RSSI of last received packet", "RSSI, dBm",
                        self.get_data_for_plotting(COMMUNICATION_LOG_ADR, "CPU_temperature"))

    def get_rxq3_temperature_plot(self):
        return BarChart("Chip internal temperature of RXQ3 transceiver", "Temperature, Celsius degrees",
                           self.get_data_for_plotting(COMMUNICATION_LOG_ADR, "CPU_temperature"))

    def get_rxq3_voltage_plot(self):
        return BarChart("Chip supply voltage of RXQ3 transceiver", "Voltage, mV",
                        self.get_data_for_plotting(COMMUNICATION_LOG_ADR, "CPU_temperature"))

    def get_on_board_computer_CPU_usage_plot(self):
        return BarChart("Intel Atom CPU usage", "Usage, %",
                                                     self.get_data_for_plotting(ONBOARD_COMPUTER_LOG_ADR, "CPU_usage"))

    def get_on_board_computer_CPU_temperature_plot(self):
        return BarChart("Chip internal temperature of Intel Atom CPU", "Temperature, Celsius degrees",
                             self.get_data_for_plotting(ONBOARD_COMPUTER_LOG_ADR, "CPU_temperature"))

    def get_on_board_computer_RAM_usage_plot(self):
        return BarChart("RAM usage", "Usage, %", self.get_data_for_plotting(ONBOARD_COMPUTER_LOG_ADR, "RAM_usage"))

    def get_payloads_humidity_plot(self):
        return BarChart("Humidity at the research module", "Humidity, %",
                                                     self.get_data_for_plotting(PAYLOAD_LOG_ADR, "payload_module_humidity"))

    def get_payloads_temperature_plot(self):
        return BarChart("Temperature at the research module", "Temperature, Celsius degrees",
                             self.get_data_for_plotting(PAYLOAD_LOG_ADR, "payload_module_temperature"))
