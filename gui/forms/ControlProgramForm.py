# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satellite_imitator_control_program_form.ui'
#
# Created: Tue May 12 18:11:39 2015
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
        MainWindow.resize(940, 605)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.undecoded_data_from_packages_label = QtGui.QLabel(self.centralwidget)
        self.undecoded_data_from_packages_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.undecoded_data_from_packages_label.setObjectName(_fromUtf8("undecoded_data_from_packages_label"))
        self.gridLayout_2.addWidget(self.undecoded_data_from_packages_label, 0, 0, 1, 1)
        self.undecoded_packages_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.undecoded_packages_textEdit.setStyleSheet(_fromUtf8(
            "background-color: qlineargradient(spread:reflect, x1:0.038, y1:0.517045, x2:1, y2:0.511, stop:0.402844 rgba(255, 255, 255, 254), stop:1 rgba(174, 151, 255, 255));"))
        self.undecoded_packages_textEdit.setObjectName(_fromUtf8("undecoded_packages_textEdit"))
        self.gridLayout_2.addWidget(self.undecoded_packages_textEdit, 1, 0, 1, 1)
        self.panel_for_manual_sending_of_commands_label = QtGui.QLabel(self.centralwidget)
        self.panel_for_manual_sending_of_commands_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.panel_for_manual_sending_of_commands_label.setTextFormat(QtCore.Qt.LogText)
        self.panel_for_manual_sending_of_commands_label.setObjectName(
            _fromUtf8("panel_for_manual_sending_of_commands_label"))
        self.gridLayout_2.addWidget(self.panel_for_manual_sending_of_commands_label, 2, 0, 1, 1)
        self.modes_of_operation_tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.modes_of_operation_tabWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.modes_of_operation_tabWidget.setStyleSheet(_fromUtf8("font: 75 12pt \"Ubuntu\";"))
        self.modes_of_operation_tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.modes_of_operation_tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.modes_of_operation_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.modes_of_operation_tabWidget.setDocumentMode(True)
        self.modes_of_operation_tabWidget.setTabsClosable(False)
        self.modes_of_operation_tabWidget.setMovable(False)
        self.modes_of_operation_tabWidget.setObjectName(_fromUtf8("modes_of_operation_tabWidget"))
        self.modes_of_operation_tab = QtGui.QWidget()
        self.modes_of_operation_tab.setObjectName(_fromUtf8("modes_of_operation_tab"))
        self.formLayout_2 = QtGui.QFormLayout(self.modes_of_operation_tab)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.modes_choosing_of_the_operation_mode_gridLayout = QtGui.QGridLayout()
        self.modes_choosing_of_the_operation_mode_gridLayout.setObjectName(
            _fromUtf8("modes_choosing_of_the_operation_mode_gridLayout"))
        self.modes_choosing_of_the_operation_mode_label = QtGui.QLabel(self.modes_of_operation_tab)
        self.modes_choosing_of_the_operation_mode_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.modes_choosing_of_the_operation_mode_label.setObjectName(
            _fromUtf8("modes_choosing_of_the_operation_mode_label"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_choosing_of_the_operation_mode_label,
                                                                       0, 0, 1, 2)
        self.modes_enable_emergency_mode_label = QtGui.QLabel(self.modes_of_operation_tab)
        self.modes_enable_emergency_mode_label.setObjectName(_fromUtf8("modes_enable_emergency_mode_label"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_emergency_mode_label, 1, 0, 1,
                                                                       1)
        self.modes_enable_emergency_mode_pushButton = QtGui.QPushButton(self.modes_of_operation_tab)
        self.modes_enable_emergency_mode_pushButton.setObjectName(_fromUtf8("modes_enable_emergency_mode_pushButton"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_emergency_mode_pushButton, 1,
                                                                       1, 1, 1)
        self.modes_enable_nominal_mode_label = QtGui.QLabel(self.modes_of_operation_tab)
        self.modes_enable_nominal_mode_label.setObjectName(_fromUtf8("modes_enable_nominal_mode_label"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_nominal_mode_label, 2, 0, 1, 1)
        self.modes_enable_nominal_mode_pushButton = QtGui.QPushButton(self.modes_of_operation_tab)
        self.modes_enable_nominal_mode_pushButton.setObjectName(_fromUtf8("modes_enable_nominal_mode_pushButton"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_nominal_mode_pushButton, 2, 1,
                                                                       1, 1)
        self.modes_enable_operating_mode_label = QtGui.QLabel(self.modes_of_operation_tab)
        self.modes_enable_operating_mode_label.setObjectName(_fromUtf8("modes_enable_operating_mode_label"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_operating_mode_label, 3, 0, 1,
                                                                       1)
        self.modes_enable_operating_mode_pushButton = QtGui.QPushButton(self.modes_of_operation_tab)
        self.modes_enable_operating_mode_pushButton.setObjectName(_fromUtf8("modes_enable_operating_mode_pushButton"))
        self.modes_choosing_of_the_operation_mode_gridLayout.addWidget(self.modes_enable_operating_mode_pushButton, 3,
                                                                       1, 1, 1)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole,
                                    self.modes_choosing_of_the_operation_mode_gridLayout)
        self.modes_of_operation_tabWidget.addTab(self.modes_of_operation_tab, _fromUtf8(""))
        self.data_handling_tab = QtGui.QWidget()
        self.data_handling_tab.setObjectName(_fromUtf8("data_handling_tab"))
        self.formLayout = QtGui.QFormLayout(self.data_handling_tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.data_handling_radio_module_settings_gridLayout = QtGui.QGridLayout()
        self.data_handling_radio_module_settings_gridLayout.setObjectName(
            _fromUtf8("data_handling_radio_module_settings_gridLayout"))
        self.data_handling_set_channel_number_comboBox = QtGui.QComboBox(self.data_handling_tab)
        self.data_handling_set_channel_number_comboBox.setObjectName(
            _fromUtf8("data_handling_set_channel_number_comboBox"))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_channel_number_comboBox.addItem(_fromUtf8(""))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_set_channel_number_comboBox, 3,
                                                                      1, 1, 1)
        self.data_handling_set_channel_number_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_channel_number_pushButton.setObjectName(
            _fromUtf8("data_handling_set_channel_number_pushButton"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_set_channel_number_pushButton,
                                                                      3, 2, 1, 1)
        self.data_handling_set_emitting_radio_signal_power_level_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_emitting_radio_signal_power_level_label.setObjectName(
            _fromUtf8("data_handling_set_emitting_radio_signal_power_level_label"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(
            self.data_handling_set_emitting_radio_signal_power_level_label, 2, 0, 1, 1)
        self.modes_toggle_transmission_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.modes_toggle_transmission_pushButton.setObjectName(_fromUtf8("modes_toggle_transmission_pushButton"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.modes_toggle_transmission_pushButton, 1, 2,
                                                                      1, 1)
        self.data_handling_set_emitting_radio_signal_power_level_comboBox = QtGui.QComboBox(self.data_handling_tab)
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setObjectName(
            _fromUtf8("data_handling_set_emitting_radio_signal_power_level_comboBox"))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.addItem(_fromUtf8(""))
        self.data_handling_radio_module_settings_gridLayout.addWidget(
            self.data_handling_set_emitting_radio_signal_power_level_comboBox, 2, 1, 1, 1)
        self.data_handling_radio_module_settings_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_radio_module_settings_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.data_handling_radio_module_settings_label.setObjectName(
            _fromUtf8("data_handling_radio_module_settings_label"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_radio_module_settings_label, 0,
                                                                      0, 1, 1)
        self.data_handling_toggle_transmission_comboBox = QtGui.QComboBox(self.data_handling_tab)
        self.data_handling_toggle_transmission_comboBox.setObjectName(
            _fromUtf8("data_handling_toggle_transmission_comboBox"))
        self.data_handling_toggle_transmission_comboBox.addItem(_fromUtf8(""))
        self.data_handling_toggle_transmission_comboBox.addItem(_fromUtf8(""))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_toggle_transmission_comboBox,
                                                                      1, 1, 1, 1)
        self.data_handling_set_channel_number_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_channel_number_label.setObjectName(_fromUtf8("data_handling_set_channel_number_label"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_set_channel_number_label, 3, 0,
                                                                      1, 1)
        self.data_handling_toggle_transmission_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_toggle_transmission_label.setObjectName(_fromUtf8("data_handling_toggle_transmission_label"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(self.data_handling_toggle_transmission_label, 1,
                                                                      0, 1, 1)
        self.data_handling_set_emitting_radio_signal_power_level_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_emitting_radio_signal_power_level_pushButton.setObjectName(
            _fromUtf8("data_handling_set_emitting_radio_signal_power_level_pushButton"))
        self.data_handling_radio_module_settings_gridLayout.addWidget(
            self.data_handling_set_emitting_radio_signal_power_level_pushButton, 2, 2, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.data_handling_radio_module_settings_gridLayout)
        self.data_handling_real_time_clock_settings_gridLayout = QtGui.QGridLayout()
        self.data_handling_real_time_clock_settings_gridLayout.setObjectName(
            _fromUtf8("data_handling_real_time_clock_settings_gridLayout"))
        self.data_handling_real_time_clock_settings_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_real_time_clock_settings_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.data_handling_real_time_clock_settings_label.setObjectName(
            _fromUtf8("data_handling_real_time_clock_settings_label"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(
            self.data_handling_real_time_clock_settings_label, 0, 0, 1, 3)
        self.data_handling_set_hours_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_hours_label.setObjectName(_fromUtf8("data_handling_set_hours_label"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_hours_label, 1, 0, 1, 1)
        self.data_handling_set_hours_spinBox = QtGui.QSpinBox(self.data_handling_tab)
        self.data_handling_set_hours_spinBox.setMaximum(23)
        self.data_handling_set_hours_spinBox.setObjectName(_fromUtf8("data_handling_set_hours_spinBox"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_hours_spinBox, 1, 1, 1,
                                                                         1)
        self.data_handling_set_hours_send_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_hours_send_pushButton.setObjectName(_fromUtf8("data_handling_set_hours_send_pushButton"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_hours_send_pushButton,
                                                                         1, 2, 1, 1)
        self.data_handling_set_minutes_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_minutes_label.setObjectName(_fromUtf8("data_handling_set_minutes_label"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_minutes_label, 2, 0, 1,
                                                                         1)
        self.data_handling_set_minutes_spinBox = QtGui.QSpinBox(self.data_handling_tab)
        self.data_handling_set_minutes_spinBox.setMaximum(59)
        self.data_handling_set_minutes_spinBox.setObjectName(_fromUtf8("data_handling_set_minutes_spinBox"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_minutes_spinBox, 2, 1,
                                                                         1, 1)
        self.data_handling_set_minutes_send_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_minutes_send_pushButton.setObjectName(
            _fromUtf8("data_handling_set_minutes_send_pushButton"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_minutes_send_pushButton,
                                                                         2, 2, 1, 1)
        self.data_handling_set_seconds_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_seconds_label.setObjectName(_fromUtf8("data_handling_set_seconds_label"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_seconds_label, 3, 0, 1,
                                                                         1)
        self.data_handling_set_seconds_spinBox = QtGui.QSpinBox(self.data_handling_tab)
        self.data_handling_set_seconds_spinBox.setMaximum(59)
        self.data_handling_set_seconds_spinBox.setObjectName(_fromUtf8("data_handling_set_seconds_spinBox"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_seconds_spinBox, 3, 1,
                                                                         1, 1)
        self.data_handling_set_seconds_send_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_seconds_send_pushButton.setObjectName(
            _fromUtf8("data_handling_set_seconds_send_pushButton"))
        self.data_handling_real_time_clock_settings_gridLayout.addWidget(self.data_handling_set_seconds_send_pushButton,
                                                                         3, 2, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole,
                                  self.data_handling_real_time_clock_settings_gridLayout)
        self.separation_label = QtGui.QLabel(self.data_handling_tab)
        self.separation_label.setText(_fromUtf8(""))
        self.separation_label.setObjectName(_fromUtf8("separation_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.separation_label)
        self.data_handling_delay_settings_gridLayout = QtGui.QGridLayout()
        self.data_handling_delay_settings_gridLayout.setObjectName(_fromUtf8("data_handling_delay_settings_gridLayout"))
        self.data_handling_set_delay_between_emitting_send_Button = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_delay_between_emitting_send_Button.setObjectName(
            _fromUtf8("data_handling_set_delay_between_emitting_send_Button"))
        self.data_handling_delay_settings_gridLayout.addWidget(
            self.data_handling_set_delay_between_emitting_send_Button, 2, 2, 1, 1)
        self.data_handling_set_delay_between_emitting_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_delay_between_emitting_label.setObjectName(
            _fromUtf8("data_handling_set_delay_between_emitting_label"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_set_delay_between_emitting_label, 2,
                                                               0, 1, 1)
        self.data_handling_set_telemetry_delay_send_pushButton = QtGui.QPushButton(self.data_handling_tab)
        self.data_handling_set_telemetry_delay_send_pushButton.setObjectName(
            _fromUtf8("data_handling_set_telemetry_delay_send_pushButton"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_set_telemetry_delay_send_pushButton,
                                                               1, 2, 1, 1)
        self.data_handling_telemetry_settings_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_telemetry_settings_label.setStyleSheet(_fromUtf8("font: 75 15pt \"Ubuntu\";"))
        self.data_handling_telemetry_settings_label.setObjectName(_fromUtf8("data_handling_telemetry_settings_label"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_telemetry_settings_label, 0, 0, 1, 3)
        self.data_handling_set_telemetry_delay_label = QtGui.QLabel(self.data_handling_tab)
        self.data_handling_set_telemetry_delay_label.setObjectName(_fromUtf8("data_handling_set_telemetry_delay_label"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_set_telemetry_delay_label, 1, 0, 1, 1)
        self.data_handling_set_telemetry_delay_spinBox = QtGui.QSpinBox(self.data_handling_tab)
        self.data_handling_set_telemetry_delay_spinBox.setMinimum(1)
        self.data_handling_set_telemetry_delay_spinBox.setMaximum(60)
        self.data_handling_set_telemetry_delay_spinBox.setObjectName(
            _fromUtf8("data_handling_set_telemetry_delay_spinBox"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_set_telemetry_delay_spinBox, 1, 1, 1,
                                                               1)
        self.data_handling_set_delay_between_emitting_spinBox = QtGui.QSpinBox(self.data_handling_tab)
        self.data_handling_set_delay_between_emitting_spinBox.setObjectName(
            _fromUtf8("data_handling_set_delay_between_emitting_spinBox"))
        self.data_handling_delay_settings_gridLayout.addWidget(self.data_handling_set_delay_between_emitting_spinBox, 2,
                                                               1, 1, 1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.data_handling_delay_settings_gridLayout)
        self.modes_of_operation_tabWidget.addTab(self.data_handling_tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.modes_of_operation_tabWidget, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
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
        self.modes_of_operation_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Satellite imitator control program", None))
        self.undecoded_data_from_packages_label.setText(
            _translate("MainWindow", "Undecoded data from received acknowledgment packets:", None))
        self.panel_for_manual_sending_of_commands_label.setText(
            _translate("MainWindow", "Panel for manual sending of commands to the miniaturized satellite imitator:",
                       None))
        self.modes_choosing_of_the_operation_mode_label.setText(
            _translate("MainWindow", "Choosing of the operation mode :", None))
        self.modes_enable_emergency_mode_label.setText(_translate("MainWindow", "Enable emergency mode", None))
        self.modes_enable_emergency_mode_pushButton.setText(_translate("MainWindow", "Send", None))
        self.modes_enable_nominal_mode_label.setText(_translate("MainWindow", "Enable nominal mode", None))
        self.modes_enable_nominal_mode_pushButton.setText(_translate("MainWindow", "Send", None))
        self.modes_enable_operating_mode_label.setText(_translate("MainWindow", "Enable operating mode", None))
        self.modes_enable_operating_mode_pushButton.setText(_translate("MainWindow", "Send", None))
        self.modes_of_operation_tabWidget.setTabText(
            self.modes_of_operation_tabWidget.indexOf(self.modes_of_operation_tab),
            _translate("MainWindow", "Modes of operation ", None))
        self.data_handling_set_channel_number_comboBox.setItemText(0,
                                                                   _translate("MainWindow", "1)   433.15 - 433.25  MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(1,
                                                                   _translate("MainWindow", "2)   433.25 - 433.35  MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(2,
                                                                   _translate("MainWindow", "3)   433.25 - 433.35  MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(3,
                                                                   _translate("MainWindow", "4)   433.45 - 433.55 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(4,
                                                                   _translate("MainWindow", "5)   433.55 - 433.65 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(5,
                                                                   _translate("MainWindow", "6)   433.65 - 433.75 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(6,
                                                                   _translate("MainWindow", "7)   433.75 - 433.85 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(7,
                                                                   _translate("MainWindow", "8)   433.85 - 433.95 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(8,
                                                                   _translate("MainWindow", "9)   433.95 - 434.05 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(9,
                                                                   _translate("MainWindow", "10) 434.05 - 434.15 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(10,
                                                                   _translate("MainWindow", "11) 434.15 - 434.25 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(11,
                                                                   _translate("MainWindow", "12) 434.25 - 434.35 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(12,
                                                                   _translate("MainWindow", "13) 434.35 - 434.45 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(13,
                                                                   _translate("MainWindow", "14) 434.45 - 434.55 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(14,
                                                                   _translate("MainWindow", "15) 434.55 - 434.65 MHz",
                                                                              None))
        self.data_handling_set_channel_number_comboBox.setItemText(15,
                                                                   _translate("MainWindow", "16) 434.65 - 434.75 MHz",
                                                                              None))
        self.data_handling_set_channel_number_pushButton.setText(_translate("MainWindow", "Send ", None))
        self.data_handling_set_emitting_radio_signal_power_level_label.setText(
            _translate("MainWindow", "Set emitting radio signal power level", None))
        self.modes_toggle_transmission_pushButton.setText(_translate("MainWindow", "Send ", None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(0, _translate("MainWindow",
                                                                                                    "+10 dBm", None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(1,
                                                                                      _translate("MainWindow", "+5 dBm",
                                                                                                 None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(2,
                                                                                      _translate("MainWindow", "0 dBm",
                                                                                                 None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(3, _translate("MainWindow",
                                                                                                    "-10 dBm", None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(4, _translate("MainWindow",
                                                                                                    "-20 dBm", None))
        self.data_handling_set_emitting_radio_signal_power_level_comboBox.setItemText(5, _translate("MainWindow",
                                                                                                    "-30 dBm", None))
        self.data_handling_radio_module_settings_label.setText(
            _translate("MainWindow", "Radio Module Settings: ", None))
        self.data_handling_toggle_transmission_comboBox.setItemText(0, _translate("MainWindow", "Disable", None))
        self.data_handling_toggle_transmission_comboBox.setItemText(1, _translate("MainWindow", "Enable", None))
        self.data_handling_set_channel_number_label.setText(_translate("MainWindow", "Set channel number", None))
        self.data_handling_toggle_transmission_label.setText(
            _translate("MainWindow", "Disable/Enable radio signal transmission", None))
        self.data_handling_set_emitting_radio_signal_power_level_pushButton.setText(
            _translate("MainWindow", "Send ", None))
        self.data_handling_real_time_clock_settings_label.setText(
            _translate("MainWindow", " Real time Clock module Settings: ", None))
        self.data_handling_set_hours_label.setText(_translate("MainWindow", "  Set the hours ", None))
        self.data_handling_set_hours_send_pushButton.setText(_translate("MainWindow", "Send", None))
        self.data_handling_set_minutes_label.setText(_translate("MainWindow", "  Set the minutes", None))
        self.data_handling_set_minutes_send_pushButton.setText(_translate("MainWindow", "Send", None))
        self.data_handling_set_seconds_label.setText(_translate("MainWindow", "  Set the seconds ", None))
        self.data_handling_set_seconds_send_pushButton.setText(_translate("MainWindow", "Send", None))
        self.data_handling_set_delay_between_emitting_send_Button.setText(_translate("MainWindow", "Send", None))
        self.data_handling_set_delay_between_emitting_label.setText(
            _translate("MainWindow", "Set delay between emitting of packages", None))
        self.data_handling_set_telemetry_delay_send_pushButton.setText(_translate("MainWindow", "Send ", None))
        self.data_handling_telemetry_settings_label.setText(
            _translate("MainWindow", "Delay settings for current mode of work: ", None))
        self.data_handling_set_telemetry_delay_label.setText(_translate("MainWindow", "Set telemetry delay", None))
        self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.data_handling_tab),
                                                     _translate("MainWindow", "Data Handling", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
