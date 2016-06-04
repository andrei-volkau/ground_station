# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelemetryDecoderForm.ui'
#
# Created: Sat Jun 04 18:51:51 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(719, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.undecoded_data_from_packages_label = QtGui.QLabel(self.centralwidget)
        self.undecoded_data_from_packages_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.undecoded_data_from_packages_label.setObjectName(_fromUtf8("undecoded_data_from_packages_label"))
        self.verticalLayout.addWidget(self.undecoded_data_from_packages_label)
        self.undecoded_data_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.undecoded_data_textEdit.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0.038, y1:0.517045, x2:1, y2:0.511, stop:0.402844 rgba(255, 255, 255, 254), stop:1 rgba(174, 151, 255, 255));"))
        self.undecoded_data_textEdit.setObjectName(_fromUtf8("undecoded_data_textEdit"))
        self.verticalLayout.addWidget(self.undecoded_data_textEdit)
        self.simulator_systems_condition_label = QtGui.QLabel(self.centralwidget)
        self.simulator_systems_condition_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.simulator_systems_condition_label.setObjectName(_fromUtf8("simulator_systems_condition_label"))
        self.verticalLayout.addWidget(self.simulator_systems_condition_label)
        self.simulator_systems_condition_tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.simulator_systems_condition_tabWidget.setStyleSheet(_fromUtf8("font: 75 12pt \"Ubuntu\";"))
        self.simulator_systems_condition_tabWidget.setDocumentMode(True)
        self.simulator_systems_condition_tabWidget.setObjectName(_fromUtf8("simulator_systems_condition_tabWidget"))
        self.electrical_power_tab = QtGui.QWidget()
        self.electrical_power_tab.setObjectName(_fromUtf8("electrical_power_tab"))
        self.electrical_power_solar_batteries_parameters_label = QtGui.QLabel(self.electrical_power_tab)
        self.electrical_power_solar_batteries_parameters_label.setGeometry(QtCore.QRect(440, 380, 268, 23))
        self.electrical_power_solar_batteries_parameters_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.electrical_power_solar_batteries_parameters_label.setObjectName(_fromUtf8("electrical_power_solar_batteries_parameters_label"))
        self.simulator_systems_condition_tabWidget.addTab(self.electrical_power_tab, _fromUtf8(""))
        self.communication_tab = QtGui.QWidget()
        self.communication_tab.setObjectName(_fromUtf8("communication_tab"))
        self.formLayout_2 = QtGui.QFormLayout(self.communication_tab)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.simulator_systems_condition_tabWidget.addTab(self.communication_tab, _fromUtf8(""))
        self.onboard_computer_tab = QtGui.QWidget()
        self.onboard_computer_tab.setObjectName(_fromUtf8("onboard_computer_tab"))
        self.formLayout = QtGui.QFormLayout(self.onboard_computer_tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.onboard_computer_parameters_gridLayout = QtGui.QGridLayout()
        self.onboard_computer_parameters_gridLayout.setObjectName(_fromUtf8("onboard_computer_parameters_gridLayout"))
        self.CPU_usage_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.CPU_usage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.CPU_usage_checkBox.setObjectName(_fromUtf8("CPU_usage_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_usage_checkBox, 0, 0, 1, 1)
        self.CPU_temperature_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.CPU_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.CPU_temperature_lcdNumber.setDigitCount(6)
        self.CPU_temperature_lcdNumber.setObjectName(_fromUtf8("CPU_temperature_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_temperature_lcdNumber, 2, 1, 1, 1)
        self.CPU_percent_label = QtGui.QLabel(self.onboard_computer_tab)
        self.CPU_percent_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.CPU_percent_label.setObjectName(_fromUtf8("CPU_percent_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_percent_label, 0, 2, 1, 1)
        self.CPU_temperature_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.CPU_temperature_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.CPU_temperature_checkBox.setObjectName(_fromUtf8("CPU_temperature_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_temperature_checkBox, 2, 0, 1, 1)
        self.CPU_usage_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.CPU_usage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.CPU_usage_lcdNumber.setDigitCount(6)
        self.CPU_usage_lcdNumber.setObjectName(_fromUtf8("CPU_usage_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_usage_lcdNumber, 0, 1, 1, 1)
        self.CPU_usage_2_label = QtGui.QLabel(self.onboard_computer_tab)
        self.CPU_usage_2_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.CPU_usage_2_label.setObjectName(_fromUtf8("CPU_usage_2_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_usage_2_label, 1, 2, 1, 1)
        self.CPU_usage_2_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.CPU_usage_2_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.CPU_usage_2_lcdNumber.setObjectName(_fromUtf8("CPU_usage_2_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_usage_2_lcdNumber, 1, 1, 1, 1)
        self.RAM_usage_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.RAM_usage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.RAM_usage_lcdNumber.setDigitCount(6)
        self.RAM_usage_lcdNumber.setObjectName(_fromUtf8("RAM_usage_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.RAM_usage_lcdNumber, 3, 1, 1, 1)
        self.RAM_usage_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.RAM_usage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.RAM_usage_checkBox.setObjectName(_fromUtf8("RAM_usage_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.RAM_usage_checkBox, 3, 0, 1, 1)
        self.CPU_celsious_label = QtGui.QLabel(self.onboard_computer_tab)
        self.CPU_celsious_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.CPU_celsious_label.setObjectName(_fromUtf8("CPU_celsious_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_celsious_label, 2, 2, 1, 1)
        self.RAM_percent_label = QtGui.QLabel(self.onboard_computer_tab)
        self.RAM_percent_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.RAM_percent_label.setObjectName(_fromUtf8("RAM_percent_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.RAM_percent_label, 3, 2, 1, 1)
        self.CPU_usage_2_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.CPU_usage_2_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.CPU_usage_2_checkBox.setObjectName(_fromUtf8("CPU_usage_2_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_usage_2_checkBox, 1, 0, 1, 1)
        self.HDD_usage_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.HDD_usage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.HDD_usage_checkBox.setObjectName(_fromUtf8("HDD_usage_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.HDD_usage_checkBox, 4, 0, 1, 1)
        self.HDD_usage_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.HDD_usage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.HDD_usage_lcdNumber.setObjectName(_fromUtf8("HDD_usage_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.HDD_usage_lcdNumber, 4, 1, 1, 1)
        self.HDD_usage_label = QtGui.QLabel(self.onboard_computer_tab)
        self.HDD_usage_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.HDD_usage_label.setObjectName(_fromUtf8("HDD_usage_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.HDD_usage_label, 4, 2, 1, 1)
        self.CPU_plate_temp_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.CPU_plate_temp_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.CPU_plate_temp_checkBox.setObjectName(_fromUtf8("CPU_plate_temp_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_plate_temp_checkBox, 5, 0, 1, 1)
        self.CPU_plate_temp_label = QtGui.QLabel(self.onboard_computer_tab)
        self.CPU_plate_temp_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.CPU_plate_temp_label.setObjectName(_fromUtf8("CPU_plate_temp_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_plate_temp_label, 5, 2, 1, 1)
        self.CPU_plate_temp_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.CPU_plate_temp_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.CPU_plate_temp_lcdNumber.setObjectName(_fromUtf8("CPU_plate_temp_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.CPU_plate_temp_lcdNumber, 5, 1, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.onboard_computer_parameters_gridLayout)
        self.simulator_systems_condition_tabWidget.addTab(self.onboard_computer_tab, _fromUtf8(""))
        self.attitude_control_tab = QtGui.QWidget()
        self.attitude_control_tab.setObjectName(_fromUtf8("attitude_control_tab"))
        self.layoutWidget_2 = QtGui.QWidget(self.attitude_control_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 351, 136))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.onboard_computer_parameters_gridLayout_2 = QtGui.QGridLayout(self.layoutWidget_2)
        self.onboard_computer_parameters_gridLayout_2.setMargin(0)
        self.onboard_computer_parameters_gridLayout_2.setObjectName(_fromUtf8("onboard_computer_parameters_gridLayout_2"))
        self.solar_sensor_2_lcdNumber = QtGui.QLCDNumber(self.layoutWidget_2)
        self.solar_sensor_2_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.solar_sensor_2_lcdNumber.setDigitCount(6)
        self.solar_sensor_2_lcdNumber.setObjectName(_fromUtf8("solar_sensor_2_lcdNumber"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_2_lcdNumber, 1, 1, 1, 1)
        self.solar_sensor_4_lcdNumber = QtGui.QLCDNumber(self.layoutWidget_2)
        self.solar_sensor_4_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.solar_sensor_4_lcdNumber.setObjectName(_fromUtf8("solar_sensor_4_lcdNumber"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_4_lcdNumber, 3, 1, 1, 1)
        self.solar_sensor_2_label = QtGui.QLabel(self.layoutWidget_2)
        self.solar_sensor_2_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.solar_sensor_2_label.setObjectName(_fromUtf8("solar_sensor_2_label"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_2_label, 1, 2, 1, 1)
        self.solar_sensor_4_checkBox = QtGui.QCheckBox(self.layoutWidget_2)
        self.solar_sensor_4_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.solar_sensor_4_checkBox.setObjectName(_fromUtf8("solar_sensor_4_checkBox"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_4_checkBox, 3, 0, 1, 1)
        self.solar_sensor_4_label = QtGui.QLabel(self.layoutWidget_2)
        self.solar_sensor_4_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.solar_sensor_4_label.setObjectName(_fromUtf8("solar_sensor_4_label"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_4_label, 3, 2, 1, 1)
        self.solar_sensor_3_checkBox = QtGui.QCheckBox(self.layoutWidget_2)
        self.solar_sensor_3_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.solar_sensor_3_checkBox.setObjectName(_fromUtf8("solar_sensor_3_checkBox"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_3_checkBox, 2, 0, 1, 1)
        self.solar_sensor_3_lcdNumber = QtGui.QLCDNumber(self.layoutWidget_2)
        self.solar_sensor_3_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.solar_sensor_3_lcdNumber.setDigitCount(6)
        self.solar_sensor_3_lcdNumber.setObjectName(_fromUtf8("solar_sensor_3_lcdNumber"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_3_lcdNumber, 2, 1, 1, 1)
        self.solar_sensor_3_label = QtGui.QLabel(self.layoutWidget_2)
        self.solar_sensor_3_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.solar_sensor_3_label.setObjectName(_fromUtf8("solar_sensor_3_label"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_3_label, 2, 2, 1, 1)
        self.solar_sensor_1_label = QtGui.QLabel(self.layoutWidget_2)
        self.solar_sensor_1_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.solar_sensor_1_label.setObjectName(_fromUtf8("solar_sensor_1_label"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_1_label, 0, 2, 1, 1)
        self.solar_sensor_1_lcdNumber = QtGui.QLCDNumber(self.layoutWidget_2)
        self.solar_sensor_1_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.solar_sensor_1_lcdNumber.setDigitCount(6)
        self.solar_sensor_1_lcdNumber.setObjectName(_fromUtf8("solar_sensor_1_lcdNumber"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_1_lcdNumber, 0, 1, 1, 1)
        self.solar_sensor_1_checkBox = QtGui.QCheckBox(self.layoutWidget_2)
        self.solar_sensor_1_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.solar_sensor_1_checkBox.setObjectName(_fromUtf8("solar_sensor_1_checkBox"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_1_checkBox, 0, 0, 1, 1)
        self.solar_sensor_2_checkBox = QtGui.QCheckBox(self.layoutWidget_2)
        self.solar_sensor_2_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.solar_sensor_2_checkBox.setObjectName(_fromUtf8("solar_sensor_2_checkBox"))
        self.onboard_computer_parameters_gridLayout_2.addWidget(self.solar_sensor_2_checkBox, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.attitude_control_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 519, 41))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.accelerometer_gyroscope_temperature_lcdNumber = QtGui.QLCDNumber(self.gridLayoutWidget_2)
        self.accelerometer_gyroscope_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.accelerometer_gyroscope_temperature_lcdNumber.setObjectName(_fromUtf8("accelerometer_gyroscope_temperature_lcdNumber"))
        self.gridLayout_2.addWidget(self.accelerometer_gyroscope_temperature_lcdNumber, 0, 1, 1, 1)
        self.accelerometer_gyroscope_checkBox = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.accelerometer_gyroscope_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.accelerometer_gyroscope_checkBox.setObjectName(_fromUtf8("accelerometer_gyroscope_checkBox"))
        self.gridLayout_2.addWidget(self.accelerometer_gyroscope_checkBox, 0, 0, 1, 1)
        self.accelerometer_gyroscope_temperature_lcdNumberlabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.accelerometer_gyroscope_temperature_lcdNumberlabel.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.accelerometer_gyroscope_temperature_lcdNumberlabel.setObjectName(_fromUtf8("accelerometer_gyroscope_temperature_lcdNumberlabel"))
        self.gridLayout_2.addWidget(self.accelerometer_gyroscope_temperature_lcdNumberlabel, 0, 2, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.attitude_control_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(370, 10, 341, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.magnetometer_x_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.magnetometer_x_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.magnetometer_x_checkBox.setObjectName(_fromUtf8("magnetometer_x_checkBox"))
        self.gridLayout.addWidget(self.magnetometer_x_checkBox, 0, 0, 1, 1)
        self.magnetometer_z_lcdNumber = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.magnetometer_z_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.magnetometer_z_lcdNumber.setObjectName(_fromUtf8("magnetometer_z_lcdNumber"))
        self.gridLayout.addWidget(self.magnetometer_z_lcdNumber, 2, 1, 1, 1)
        self.magnetometer_y_label = QtGui.QLabel(self.gridLayoutWidget)
        self.magnetometer_y_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.magnetometer_y_label.setObjectName(_fromUtf8("magnetometer_y_label"))
        self.gridLayout.addWidget(self.magnetometer_y_label, 1, 2, 1, 1)
        self.magnetometer_x_lcdNumber = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.magnetometer_x_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.magnetometer_x_lcdNumber.setObjectName(_fromUtf8("magnetometer_x_lcdNumber"))
        self.gridLayout.addWidget(self.magnetometer_x_lcdNumber, 0, 1, 1, 1)
        self.magnetometer_z_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.magnetometer_z_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.magnetometer_z_checkBox.setObjectName(_fromUtf8("magnetometer_z_checkBox"))
        self.gridLayout.addWidget(self.magnetometer_z_checkBox, 2, 0, 1, 1)
        self.magnetometer_z_label = QtGui.QLabel(self.gridLayoutWidget)
        self.magnetometer_z_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.magnetometer_z_label.setObjectName(_fromUtf8("magnetometer_z_label"))
        self.gridLayout.addWidget(self.magnetometer_z_label, 2, 2, 1, 1)
        self.magnetometer_y_lcdNumber = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.magnetometer_y_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.magnetometer_y_lcdNumber.setObjectName(_fromUtf8("magnetometer_y_lcdNumber"))
        self.gridLayout.addWidget(self.magnetometer_y_lcdNumber, 1, 1, 1, 1)
        self.magnetometer_x_label = QtGui.QLabel(self.gridLayoutWidget)
        self.magnetometer_x_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.magnetometer_x_label.setObjectName(_fromUtf8("magnetometer_x_label"))
        self.gridLayout.addWidget(self.magnetometer_x_label, 0, 2, 1, 1)
        self.magnetometer_y_checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.magnetometer_y_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.magnetometer_y_checkBox.setObjectName(_fromUtf8("magnetometer_y_checkBox"))
        self.gridLayout.addWidget(self.magnetometer_y_checkBox, 1, 0, 1, 1)
        self.simulator_systems_condition_tabWidget.addTab(self.attitude_control_tab, _fromUtf8(""))
        self.payloads_tab = QtGui.QWidget()
        self.payloads_tab.setObjectName(_fromUtf8("payloads_tab"))
        self.layoutWidget = QtGui.QWidget(self.payloads_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.parameters_gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.parameters_gridLayout.setMargin(0)
        self.parameters_gridLayout.setObjectName(_fromUtf8("parameters_gridLayout"))
        self.payload_temperature_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.payload_temperature_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.payload_temperature_checkBox.setObjectName(_fromUtf8("payload_temperature_checkBox"))
        self.parameters_gridLayout.addWidget(self.payload_temperature_checkBox, 1, 0, 1, 1)
        self.payload_temperature_lcdNumber = QtGui.QLCDNumber(self.layoutWidget)
        self.payload_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(133, 113, 255);\n"
"}"))
        self.payload_temperature_lcdNumber.setDigitCount(6)
        self.payload_temperature_lcdNumber.setObjectName(_fromUtf8("payload_temperature_lcdNumber"))
        self.parameters_gridLayout.addWidget(self.payload_temperature_lcdNumber, 1, 1, 1, 1)
        self.payload_temperature_celsious_label = QtGui.QLabel(self.layoutWidget)
        self.payload_temperature_celsious_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.payload_temperature_celsious_label.setObjectName(_fromUtf8("payload_temperature_celsious_label"))
        self.parameters_gridLayout.addWidget(self.payload_temperature_celsious_label, 1, 2, 1, 1)
        self.parameters_research_module_label = QtGui.QLabel(self.layoutWidget)
        self.parameters_research_module_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.parameters_research_module_label.setObjectName(_fromUtf8("parameters_research_module_label"))
        self.parameters_gridLayout.addWidget(self.parameters_research_module_label, 0, 0, 1, 2)
        self.simulator_systems_condition_tabWidget.addTab(self.payloads_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.simulator_systems_condition_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.retranslateUi(MainWindow)
        self.simulator_systems_condition_tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Telemetry decoder for miniaturized satellite simulator", None))
        self.undecoded_data_from_packages_label.setText(_translate("MainWindow", "Содержимое пришедших пакетов телеметрической информации:", None))
        self.undecoded_data_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>", None))
        self.simulator_systems_condition_label.setText(_translate("MainWindow", "Параметры систем имитатора СМКА:", None))
        self.electrical_power_solar_batteries_parameters_label.setText(_translate("MainWindow", "Parameters of solar baterries: ", None))
        self.simulator_systems_condition_tabWidget.setTabText(self.simulator_systems_condition_tabWidget.indexOf(self.electrical_power_tab), _translate("MainWindow", "Электроснабжение", None))
        self.simulator_systems_condition_tabWidget.setTabText(self.simulator_systems_condition_tabWidget.indexOf(self.communication_tab), _translate("MainWindow", "Связь", None))
        self.CPU_usage_checkBox.setText(_translate("MainWindow", "Загруженность 1-го ядра ЦП ", None))
        self.CPU_percent_label.setText(_translate("MainWindow", "%", None))
        self.CPU_temperature_checkBox.setText(_translate("MainWindow", "Температура ЦП  ", None))
        self.CPU_usage_2_label.setText(_translate("MainWindow", "%", None))
        self.RAM_usage_checkBox.setText(_translate("MainWindow", "Загруженность ОЗУ", None))
        self.CPU_celsious_label.setText(_translate("MainWindow", " °C", None))
        self.RAM_percent_label.setText(_translate("MainWindow", "%", None))
        self.CPU_usage_2_checkBox.setText(_translate("MainWindow", "Загруженность 2-го ядра ЦП ", None))
        self.HDD_usage_checkBox.setText(_translate("MainWindow", "Объём занятой памяти жёсткого диска", None))
        self.HDD_usage_label.setText(_translate("MainWindow", "%", None))
        self.CPU_plate_temp_checkBox.setText(_translate("MainWindow", "Температура платы процессорного модуля", None))
        self.CPU_plate_temp_label.setText(_translate("MainWindow", " °C", None))
        self.simulator_systems_condition_tabWidget.setTabText(self.simulator_systems_condition_tabWidget.indexOf(self.onboard_computer_tab), _translate("MainWindow", "Бортовой компьютер", None))
        self.solar_sensor_2_label.setText(_translate("MainWindow", "лк", None))
        self.solar_sensor_4_checkBox.setText(_translate("MainWindow", "Солнечный датчик №4", None))
        self.solar_sensor_4_label.setText(_translate("MainWindow", "лк", None))
        self.solar_sensor_3_checkBox.setText(_translate("MainWindow", "Солнечный датчик №3", None))
        self.solar_sensor_3_label.setText(_translate("MainWindow", "лк", None))
        self.solar_sensor_1_label.setText(_translate("MainWindow", "лк", None))
        self.solar_sensor_1_checkBox.setText(_translate("MainWindow", "Солнечный датчик №1", None))
        self.solar_sensor_2_checkBox.setText(_translate("MainWindow", "Солнечный датчик №2", None))
        self.accelerometer_gyroscope_checkBox.setText(_translate("MainWindow", "Температура аскелерометра и гироскопа", None))
        self.accelerometer_gyroscope_temperature_lcdNumberlabel.setText(_translate("MainWindow", " °C", None))
        self.magnetometer_x_checkBox.setText(_translate("MainWindow", "Магнитометр, X ", None))
        self.magnetometer_y_label.setText(_translate("MainWindow", "Тл", None))
        self.magnetometer_z_checkBox.setText(_translate("MainWindow", "Магнитометр, Z", None))
        self.magnetometer_z_label.setText(_translate("MainWindow", "Тл", None))
        self.magnetometer_x_label.setText(_translate("MainWindow", "Тл", None))
        self.magnetometer_y_checkBox.setText(_translate("MainWindow", "Магнитометр, Y", None))
        self.simulator_systems_condition_tabWidget.setTabText(self.simulator_systems_condition_tabWidget.indexOf(self.attitude_control_tab), _translate("MainWindow", "Ориентация", None))
        self.payload_temperature_checkBox.setText(_translate("MainWindow", "Датчик температуры ", None))
        self.payload_temperature_celsious_label.setText(_translate("MainWindow", " °C", None))
        self.parameters_research_module_label.setText(_translate("MainWindow", "Параметры научного моудля :", None))
        self.simulator_systems_condition_tabWidget.setTabText(self.simulator_systems_condition_tabWidget.indexOf(self.payloads_tab), _translate("MainWindow", "Научная аппаратура", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))

