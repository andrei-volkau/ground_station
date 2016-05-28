# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telemetry_decoder_form.ui'
#
# Created: Sat Nov 21 11:32:47 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(736, 619)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.undecoded_data_from_packages_label = QtGui.QLabel(self.centralwidget)
        self.undecoded_data_from_packages_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.undecoded_data_from_packages_label.setObjectName(_fromUtf8("undecoded_data_from_packages_label"))
        self.verticalLayout.addWidget(self.undecoded_data_from_packages_label)
        self.undecoded_data_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.undecoded_data_textEdit.setStyleSheet(_fromUtf8(
            "background-color: qlineargradient(spread:reflect, x1:0.038, y1:0.517045, x2:1, y2:0.511, stop:0.402844 rgba(255, 255, 255, 254), stop:1 rgba(174, 151, 255, 255));"))
        self.undecoded_data_textEdit.setObjectName(_fromUtf8("undecoded_data_textEdit"))
        self.verticalLayout.addWidget(self.undecoded_data_textEdit)
        self.imitator_systems_condition_label = QtGui.QLabel(self.centralwidget)
        self.imitator_systems_condition_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.imitator_systems_condition_label.setObjectName(_fromUtf8("imitator_systems_condition_label"))
        self.verticalLayout.addWidget(self.imitator_systems_condition_label)
        self.imitator_systems_condition_tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.imitator_systems_condition_tabWidget.setStyleSheet(_fromUtf8("font: 75 12pt \"Ubuntu\";"))
        self.imitator_systems_condition_tabWidget.setDocumentMode(True)
        self.imitator_systems_condition_tabWidget.setObjectName(_fromUtf8("imitator_systems_condition_tabWidget"))
        self.electrical_power_tab = QtGui.QWidget()
        self.electrical_power_tab.setObjectName(_fromUtf8("electrical_power_tab"))
        self.electrical_power_solar_batteries_parameters_label = QtGui.QLabel(self.electrical_power_tab)
        self.electrical_power_solar_batteries_parameters_label.setGeometry(QtCore.QRect(440, 380, 268, 23))
        self.electrical_power_solar_batteries_parameters_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.electrical_power_solar_batteries_parameters_label.setObjectName(
            _fromUtf8("electrical_power_solar_batteries_parameters_label"))
        self.imitator_systems_condition_tabWidget.addTab(self.electrical_power_tab, _fromUtf8(""))
        self.communication_tab = QtGui.QWidget()
        self.communication_tab.setObjectName(_fromUtf8("communication_tab"))
        self.formLayout_2 = QtGui.QFormLayout(self.communication_tab)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.communication_transceiver_parameters_gridLayout = QtGui.QGridLayout()
        self.communication_transceiver_parameters_gridLayout.setObjectName(
            _fromUtf8("communication_transceiver_parameters_gridLayout"))
        self.communication_dBm_label = QtGui.QLabel(self.communication_tab)
        self.communication_dBm_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.communication_dBm_label.setObjectName(_fromUtf8("communication_dBm_label"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_dBm_label, 2, 2, 1, 1)
        self.communication_temperature_lcdNumber = QtGui.QLCDNumber(self.communication_tab)
        self.communication_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                         "    color: rgb(255, 255, 255);    \n"
                                                                         "    background-color: rgb(133, 113, 255);\n"
                                                                         "}"))
        self.communication_temperature_lcdNumber.setNumDigits(6)
        self.communication_temperature_lcdNumber.setObjectName(_fromUtf8("communication_temperature_lcdNumber"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_temperature_lcdNumber, 3, 1,
                                                                       1, 1)
        self.communication_rssi_checkBox = QtGui.QCheckBox(self.communication_tab)
        self.communication_rssi_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.communication_rssi_checkBox.setObjectName(_fromUtf8("communication_rssi_checkBox"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_rssi_checkBox, 2, 0, 1, 1)
        self.communication_mV_label = QtGui.QLabel(self.communication_tab)
        self.communication_mV_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.communication_mV_label.setObjectName(_fromUtf8("communication_mV_label"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_mV_label, 4, 2, 1, 1)
        self.communication_celsius_label = QtGui.QLabel(self.communication_tab)
        self.communication_celsius_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.communication_celsius_label.setObjectName(_fromUtf8("communication_celsius_label"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_celsius_label, 3, 2, 1, 1)
        self.communication_rssi_lcdNumber = QtGui.QLCDNumber(self.communication_tab)
        self.communication_rssi_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                  "    color: rgb(255, 255, 255);    \n"
                                                                  "    background-color: rgb(133, 113, 255);\n"
                                                                  "}"))
        self.communication_rssi_lcdNumber.setNumDigits(6)
        self.communication_rssi_lcdNumber.setObjectName(_fromUtf8("communication_rssi_lcdNumber"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_rssi_lcdNumber, 2, 1, 1, 1)
        self.communication_voltage_lcdNumber = QtGui.QLCDNumber(self.communication_tab)
        self.communication_voltage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                     "    color: rgb(255, 255, 255);    \n"
                                                                     "    background-color: rgb(133, 113, 255);\n"
                                                                     "}"))
        self.communication_voltage_lcdNumber.setNumDigits(6)
        self.communication_voltage_lcdNumber.setObjectName(_fromUtf8("communication_voltage_lcdNumber"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_voltage_lcdNumber, 4, 1, 1, 1)
        self.communication_voltage_checkBox = QtGui.QCheckBox(self.communication_tab)
        self.communication_voltage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.communication_voltage_checkBox.setObjectName(_fromUtf8("communication_voltage_checkBox"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_voltage_checkBox, 4, 0, 1, 1)
        self.communication_temperature_checkBox = QtGui.QCheckBox(self.communication_tab)
        self.communication_temperature_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.communication_temperature_checkBox.setObjectName(_fromUtf8("communication_temperature_checkBox"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_temperature_checkBox, 3, 0, 1,
                                                                       1)
        self.communication_parameter_transceiver_label = QtGui.QLabel(self.communication_tab)
        self.communication_parameter_transceiver_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.communication_parameter_transceiver_label.setObjectName(
            _fromUtf8("communication_parameter_transceiver_label"))
        self.communication_transceiver_parameters_gridLayout.addWidget(self.communication_parameter_transceiver_label,
                                                                       1, 0, 1, 1)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole,
                                    self.communication_transceiver_parameters_gridLayout)
        self.imitator_systems_condition_tabWidget.addTab(self.communication_tab, _fromUtf8(""))
        self.onboard_computer_tab = QtGui.QWidget()
        self.onboard_computer_tab.setObjectName(_fromUtf8("onboard_computer_tab"))
        self.formLayout = QtGui.QFormLayout(self.onboard_computer_tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.onboard_computer_parameters_gridLayout = QtGui.QGridLayout()
        self.onboard_computer_parameters_gridLayout.setObjectName(_fromUtf8("onboard_computer_parameters_gridLayout"))
        self.onboard_computer_parameters_CPU_RAM_label = QtGui.QLabel(self.onboard_computer_tab)
        self.onboard_computer_parameters_CPU_RAM_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.onboard_computer_parameters_CPU_RAM_label.setObjectName(
            _fromUtf8("onboard_computer_parameters_CPU_RAM_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_parameters_CPU_RAM_label, 0, 0, 1,
                                                              2)
        self.onboard_computer_CPU_usage_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.onboard_computer_CPU_usage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.onboard_computer_CPU_usage_checkBox.setObjectName(_fromUtf8("onboard_computer_CPU_usage_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_CPU_usage_checkBox, 1, 0, 1, 1)
        self.onboard_computer_CPU_usage_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.onboard_computer_CPU_usage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                          "    color: rgb(255, 255, 255);    \n"
                                                                          "    background-color: rgb(133, 113, 255);\n"
                                                                          "}"))
        self.onboard_computer_CPU_usage_lcdNumber.setNumDigits(6)
        self.onboard_computer_CPU_usage_lcdNumber.setObjectName(_fromUtf8("onboard_computer_CPU_usage_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_CPU_usage_lcdNumber, 1, 1, 1, 1)
        self.onboard_computer_CPU_percent_label = QtGui.QLabel(self.onboard_computer_tab)
        self.onboard_computer_CPU_percent_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.onboard_computer_CPU_percent_label.setObjectName(_fromUtf8("onboard_computer_CPU_percent_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_CPU_percent_label, 1, 2, 1, 1)
        self.onboard_computer_CPU_temperature_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.onboard_computer_CPU_temperature_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.onboard_computer_CPU_temperature_checkBox.setObjectName(
            _fromUtf8("onboard_computer_CPU_temperature_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_CPU_temperature_checkBox, 2, 0, 1,
                                                              1)
        self.onboard_computer_CPU_temperature_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.onboard_computer_CPU_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                                "    color: rgb(255, 255, 255);    \n"
                                                                                "    background-color: rgb(133, 113, 255);\n"
                                                                                "}"))
        self.onboard_computer_CPU_temperature_lcdNumber.setNumDigits(6)
        self.onboard_computer_CPU_temperature_lcdNumber.setObjectName(
            _fromUtf8("onboard_computer_CPU_temperature_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_CPU_temperature_lcdNumber, 2, 1, 1,
                                                              1)
        self.onboard_computer_celsious_label = QtGui.QLabel(self.onboard_computer_tab)
        self.onboard_computer_celsious_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.onboard_computer_celsious_label.setObjectName(_fromUtf8("onboard_computer_celsious_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_celsious_label, 2, 2, 1, 1)
        self.onboard_computer_RAM_usage_checkBox = QtGui.QCheckBox(self.onboard_computer_tab)
        self.onboard_computer_RAM_usage_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.onboard_computer_RAM_usage_checkBox.setObjectName(_fromUtf8("onboard_computer_RAM_usage_checkBox"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_RAM_usage_checkBox, 3, 0, 1, 1)
        self.onboard_computer_RAM_usage_lcdNumber = QtGui.QLCDNumber(self.onboard_computer_tab)
        self.onboard_computer_RAM_usage_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                          "    color: rgb(255, 255, 255);    \n"
                                                                          "    background-color: rgb(133, 113, 255);\n"
                                                                          "}"))
        self.onboard_computer_RAM_usage_lcdNumber.setNumDigits(6)
        self.onboard_computer_RAM_usage_lcdNumber.setObjectName(_fromUtf8("onboard_computer_RAM_usage_lcdNumber"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_RAM_usage_lcdNumber, 3, 1, 1, 1)
        self.onboard_computer_RAM_percent_label = QtGui.QLabel(self.onboard_computer_tab)
        self.onboard_computer_RAM_percent_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.onboard_computer_RAM_percent_label.setObjectName(_fromUtf8("onboard_computer_RAM_percent_label"))
        self.onboard_computer_parameters_gridLayout.addWidget(self.onboard_computer_RAM_percent_label, 3, 2, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.onboard_computer_parameters_gridLayout)
        self.imitator_systems_condition_tabWidget.addTab(self.onboard_computer_tab, _fromUtf8(""))
        self.attitude_control_tab = QtGui.QWidget()
        self.attitude_control_tab.setObjectName(_fromUtf8("attitude_control_tab"))
        self.imitator_systems_condition_tabWidget.addTab(self.attitude_control_tab, _fromUtf8(""))
        self.payloads_tab = QtGui.QWidget()
        self.payloads_tab.setObjectName(_fromUtf8("payloads_tab"))
        self.layoutWidget = QtGui.QWidget(self.payloads_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 93))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.payloads_parameters_gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.payloads_parameters_gridLayout.setMargin(0)
        self.payloads_parameters_gridLayout.setObjectName(_fromUtf8("payloads_parameters_gridLayout"))
        self.payloads_parameters_research_module_label = QtGui.QLabel(self.layoutWidget)
        self.payloads_parameters_research_module_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.payloads_parameters_research_module_label.setObjectName(
            _fromUtf8("payloads_parameters_research_module_label"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_parameters_research_module_label, 0, 0, 1, 2)
        self.payloads_humidity_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.payloads_humidity_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.payloads_humidity_checkBox.setObjectName(_fromUtf8("payloads_humidity_checkBox"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_humidity_checkBox, 1, 0, 1, 1)
        self.payloads_humidity_lcdNumber = QtGui.QLCDNumber(self.layoutWidget)
        self.payloads_humidity_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                 "    color: rgb(255, 255, 255);    \n"
                                                                 "    background-color: rgb(133, 113, 255);\n"
                                                                 "}"))
        self.payloads_humidity_lcdNumber.setNumDigits(6)
        self.payloads_humidity_lcdNumber.setObjectName(_fromUtf8("payloads_humidity_lcdNumber"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_humidity_lcdNumber, 1, 1, 1, 1)
        self.payloads_humidity_percent_label = QtGui.QLabel(self.layoutWidget)
        self.payloads_humidity_percent_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.payloads_humidity_percent_label.setObjectName(_fromUtf8("payloads_humidity_percent_label"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_humidity_percent_label, 1, 2, 1, 1)
        self.payloads_temperature_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.payloads_temperature_checkBox.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.payloads_temperature_checkBox.setObjectName(_fromUtf8("payloads_temperature_checkBox"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_temperature_checkBox, 2, 0, 1, 1)
        self.payloads_temperature_lcdNumber = QtGui.QLCDNumber(self.layoutWidget)
        self.payloads_temperature_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
                                                                    "    color: rgb(255, 255, 255);    \n"
                                                                    "    background-color: rgb(133, 113, 255);\n"
                                                                    "}"))
        self.payloads_temperature_lcdNumber.setNumDigits(6)
        self.payloads_temperature_lcdNumber.setObjectName(_fromUtf8("payloads_temperature_lcdNumber"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_temperature_lcdNumber, 2, 1, 1, 1)
        self.payloads_temperature_celsious_label = QtGui.QLabel(self.layoutWidget)
        self.payloads_temperature_celsious_label.setStyleSheet(_fromUtf8("font: 75 18pt \"Ubuntu\";"))
        self.payloads_temperature_celsious_label.setObjectName(_fromUtf8("payloads_temperature_celsious_label"))
        self.payloads_parameters_gridLayout.addWidget(self.payloads_temperature_celsious_label, 2, 2, 1, 1)
        self.imitator_systems_condition_tabWidget.addTab(self.payloads_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.imitator_systems_condition_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.imitator_systems_condition_tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Telemetry decoder for miniaturized satellite imitator", None))
        self.undecoded_data_from_packages_label.setText(
            _translate("MainWindow", "Undecoded data from received telemetry packets:", None))
        self.undecoded_data_textEdit.setHtml(_translate("MainWindow",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                        None))
        self.imitator_systems_condition_label.setText(
            _translate("MainWindow", "Real-time condition of miniaturized satellite imitator\'s systems:", None))
        self.electrical_power_solar_batteries_parameters_label.setText(
            _translate("MainWindow", "Parameters of solar baterries: ", None))
        self.imitator_systems_condition_tabWidget.setTabText(
            self.imitator_systems_condition_tabWidget.indexOf(self.electrical_power_tab),
            _translate("MainWindow", "Electrical Power", None))
        self.communication_dBm_label.setText(_translate("MainWindow", "dBm", None))
        self.communication_rssi_checkBox.setText(_translate("MainWindow", "RSSI of last resieved packet", None))
        self.communication_mV_label.setText(_translate("MainWindow", "mV", None))
        self.communication_celsius_label.setText(_translate("MainWindow", " °C", None))
        self.communication_voltage_checkBox.setText(_translate("MainWindow", "Chip supply voltage", None))
        self.communication_temperature_checkBox.setText(
            _translate("MainWindow", "Chip internal temperature          ", None))
        self.communication_parameter_transceiver_label.setText(
            _translate("MainWindow", "Parameters of RXQ3 Smart Transceiver:", None))
        self.imitator_systems_condition_tabWidget.setTabText(
            self.imitator_systems_condition_tabWidget.indexOf(self.communication_tab),
            _translate("MainWindow", "Communication", None))
        self.onboard_computer_parameters_CPU_RAM_label.setText(
            _translate("MainWindow", "Parameters of Intel Atom on-board computer:", None))
        self.onboard_computer_CPU_usage_checkBox.setText(
            _translate("MainWindow", "CPU usage                                              ", None))
        self.onboard_computer_CPU_percent_label.setText(_translate("MainWindow", "%", None))
        self.onboard_computer_CPU_temperature_checkBox.setText(
            _translate("MainWindow", "CPU\'s chip internal temperature        ", None))
        self.onboard_computer_celsious_label.setText(_translate("MainWindow", " °C", None))
        self.onboard_computer_RAM_usage_checkBox.setText(_translate("MainWindow", "RAM usage", None))
        self.onboard_computer_RAM_percent_label.setText(_translate("MainWindow", "%", None))
        self.imitator_systems_condition_tabWidget.setTabText(
            self.imitator_systems_condition_tabWidget.indexOf(self.onboard_computer_tab),
            _translate("MainWindow", "On-board computer", None))
        self.imitator_systems_condition_tabWidget.setTabText(
            self.imitator_systems_condition_tabWidget.indexOf(self.attitude_control_tab),
            _translate("MainWindow", "Attitude Control", None))
        self.payloads_parameters_research_module_label.setText(
            _translate("MainWindow", "Parameters of research module :", None))
        self.payloads_humidity_checkBox.setText(_translate("MainWindow", "Humidity sensor", None))
        self.payloads_humidity_percent_label.setText(_translate("MainWindow", "%", None))
        self.payloads_temperature_checkBox.setText(_translate("MainWindow", "Temperature sensor ", None))
        self.payloads_temperature_celsious_label.setText(_translate("MainWindow", " °C", None))
        self.imitator_systems_condition_tabWidget.setTabText(
            self.imitator_systems_condition_tabWidget.indexOf(self.payloads_tab),
            _translate("MainWindow", "Payloads", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
