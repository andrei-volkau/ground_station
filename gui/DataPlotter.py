from PyQt4.QtCore import QObject
from BarChart import BarChart
import csv
import datetime
from PayloadParser import get_category, SENSOR_TIMESTAMP, SENSOR_CPU_TEMP, SENSOR_OS_CPU0, SENSOR_OS_RAM, \
    SENSOR_PAYLOAD_TEMP, SENSOR_OS_CPU1, SENSOR_OS_DISK
from telemetry_sharing.push_to_csv import get_csv_filename, FIELD_NAMES


PAYLOAD_LOG_ADR = "./log_files/telemetry_log_files/Payload_system_telemetry_log.csv"
ONBOARD_COMPUTER_LOG_ADR = "./log_files/telemetry_log_files/onboard_comp_sys.csv"
COMMUNICATION_LOG_ADR = "./log_files/telemetry_log_files/Communication_system_telemetry_log.csv"


class DataPlotter(QObject):
    """
        GUI for telemetry decoder for miniaturized satellite imitator
    """

    def __init__(self, parent):
        QObject.__init__(self, parent)

    def get_data_for_plotting(self, sensor):
        """
            Get required data from telemetry log file for plotting on a bar chart.

        Args:
            log_file_name (str): Name of telemetry log file.
            measurement_parameter (str): Kind of data, that need to be extracted from telemetry_log.csv file.

        Returns:
            data (list): Data for plotting on a bar chart.
        """
        category = get_category(sensor)
        filename = get_csv_filename(category)
        fieldnames = FIELD_NAMES[category]

        data = []
        with open(filename, "r") as file:
            lines = [line for line in file]
            lines = lines[-11:]
            reader = csv.DictReader(lines, fieldnames=fieldnames)
            for row in reader:
                unix_time = float(row[SENSOR_TIMESTAMP])
                time = datetime.datetime.fromtimestamp(unix_time).strftime('%m-%d-%y \n %H:%M:%S')
                val = float(row[sensor])
                data.append((time, val))
        return data

    def get_onboard_computer_CPU_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_CPU0)
        return BarChart("Intel Atom CPU usage of first core", "Usage, %", data)

    def get_onboard_computer_CPU_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_CPU1)
        return BarChart("Intel Atom CPU usage of second core", "Usage, %", data)

    def get_onboard_computer_CPU_temperature_plot(self):
        data = self.get_data_for_plotting(SENSOR_CPU_TEMP)
        return BarChart("Chip internal temperature of Intel Atom CPU",
                        "Temperature, Celsius degrees", data)

    def get_onboard_computer_RAM_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_RAM)
        return BarChart("RAM usage", "Usage, %", data)

    def get_onboard_computer_HDD_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_DISK)
        return BarChart("HDD usage", "Usage, %", data)

    def get_payload_module_temperature_plot(self):
        data = self.get_data_for_plotting(SENSOR_PAYLOAD_TEMP)
        return BarChart("Temperature at the research module", "Temperature, Celsius degrees", data)
