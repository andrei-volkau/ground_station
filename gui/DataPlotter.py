# -*- coding: utf-8 -*-

import csv
import datetime

from PyQt4.QtCore import QObject, QString

from BarChart import BarChart
from telemetry_sharing.push_to_csv import get_csv_filename, FIELD_NAMES
from PayloadParser import *


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
            # lines = []
            # for line in file:
            # if line != None:
            #        lines.append(line)
            # if len(lines) > 10:
            #     lines = lines[-11:]
            # print lines
            reader = csv.DictReader(lines, fieldnames=fieldnames)
            rows_without_blank_sensor_data = []
            for row in reader:
                if row[sensor] != "":
                    rows_without_blank_sensor_data.append(row)

            rows_without_blank_sensor_data = rows_without_blank_sensor_data[-11:]

            for row in rows_without_blank_sensor_data:
                unix_time = float(row[SENSOR_TIMESTAMP])
                time = datetime.datetime.fromtimestamp(unix_time).strftime('%m-%d-%y \n %H:%M:%S')
                val = float(row[sensor])
                data.append((time, val))
        return data

    def get_CPU_0_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_CPU0)
        return BarChart("Intel Atom CPU usage of first core", "Usage, %", data)

    def get_CPU_1_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_CPU1)
        return BarChart("Intel Atom CPU usage of second core", "Usage, %", data)

    def get_CPU_temperature_plot(self):
        data = self.get_data_for_plotting(SENSOR_CPU_TEMP)
        return BarChart("Chip internal temperature of Intel Atom CPU",
                        "Temperature, Celsius degrees", data)

    def get_RAM_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_RAM)
        return BarChart("RAM usage", "Usage, %", data)

    def get_HDD_usage_plot(self):
        data = self.get_data_for_plotting(SENSOR_OS_DISK)
        return BarChart("HDD usage", "Usage, %", data)

    def get_cpu_board_temp_plot(self):
        data = self.get_data_for_plotting(SENSOR_BOARD_TEMP)
        return BarChart("HDD usage", "Usage, %", data)

    def get_solar_sensor_1_plot(self):
        data = self.get_data_for_plotting(SENSOR_LIGHT1)
        return BarChart(u"Solar sensor N1", u"Illumination, conventional units", data)

    def get_solar_sensor_2_plot(self):
        data = self.get_data_for_plotting(SENSOR_LIGHT2)
        return BarChart(u"Solar sensor N2", u"Illumination, conventional units", data)

    def get_solar_sensor_3_plot(self):
        data = self.get_data_for_plotting(SENSOR_LIGHT3)
        return BarChart(u"Solar sensor N3", u"Illumination, conventional units", data)

    def get_solar_sensor_4_plot(self):
        data = self.get_data_for_plotting(SENSOR_LIGHT4)
        return BarChart(u"Solar sensor N4", u"Illumination, conventional units", data)

    def get_magnetometer_x_plot(self):
        data = self.get_data_for_plotting(SENSOR_MAGNET_X)
        return BarChart(u"Magnetometer", u"Magnetic induction, mGs", data)

    def get_magnetometer_y_plot(self):
        data = self.get_data_for_plotting(SENSOR_MAGNET_Y)
        return BarChart(u"Magnetometer", u"Magnetic induction, mGs", data)

    def get_magnetometer_z_plot(self):
        data = self.get_data_for_plotting(SENSOR_MAGNET_Z)
        return BarChart(u"Magnetometer", u"Magnetic induction, mGs", data)

    def get_accelerometer_gyroscope_board_temperature_plot(self):
        data = self.get_data_for_plotting(SENSOR_ACCELEROMETER_GYROSCOPE_TEMP)
        return BarChart(u"Temperature of accelerometer and gyroscope board", u"Temperature, Celsius degrees", data)

    def get_payload_module_temperature_plot(self):
        data = self.get_data_for_plotting(SENSOR_PAYLOAD_TEMP)
        return BarChart("Temperature at the research module", "Temperature, Celsius degrees", data)

    def get_gyroscope_x_angular_velocity(self):
        data = self.get_data_for_plotting(SENSOR_GYRO_X)
        return BarChart("Angular velocity, X", "X component of angular velocity, Degrees/s", data)

    def get_gyroscope_y_angular_velocity(self):
        data = self.get_data_for_plotting(SENSOR_GYRO_X)
        return BarChart("Angular velocity, Y", "Y component of angular velocity, Degrees/s", data)

    def get_gyroscope_z_angular_velocity(self):
        data = self.get_data_for_plotting(SENSOR_GYRO_X)
        return BarChart("Angular velocity, Z", "Z component of angular velocity, Degrees/s", data)

    def get_accelerometer_x_acceleration(self):
        data = self.get_data_for_plotting(SENSOR_ACCEL_X)
        return BarChart("Acceleration, X", "X component of acceleration, m/s2", data)

    def get_accelerometer_y_acceleration(self):
        data = self.get_data_for_plotting(SENSOR_ACCEL_Y)
        return BarChart("Acceleration, Y", "Y component of acceleration, m/s2", data)

    def get_accelerometer_z_acceleration(self):
        data = self.get_data_for_plotting(SENSOR_ACCEL_Z)
        return BarChart("Acceleration, Z", "Z component of acceleration, m/s2", data)