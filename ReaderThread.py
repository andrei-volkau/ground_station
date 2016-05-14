# -*- coding: utf-8 -*-
import winsound
from PyQt4 import QtCore
from PyQt4.QtCore import QThreadPool
from communication_protocol_kernel import sp_kernel
from loggers.logger import log_the_data
from network_communication.FTP_thread import FTP_thread
from network_communication.WEB_request_thread import WEB_request_thread


class ReaderThread(QtCore.QThread):
    """This class represent a reader thread, that read data from the serial port's buffer in a block mode."""
    def __init__(self, parent, protocol):
        """Make a instance of the ReaderThread class.
        Args:
            protocol (SerialProtocol): It is a instance of a communication protocol.
        """
        super(ReaderThread, self).__init__(parent)
        self.communication_protocol = protocol
        self.package_time_mark = set()

    def set_control_program(self, control_program):
        """Set a control program.
        Args:
            control_program (GUI_for_control_program): It is a instance of GUI of a miniaturized satellite simulator
             control program.
        """
        self.control_program = control_program

    def set_telemetry_decoder(self, telemetry_decoder):
        """Set a telemetry decoder.
        Args:
            telemetry_decoder (GUI_for_telemetry_decoder): It is a instance of GUI of telemetry decoder for a
            miniaturized satellite simulator.
        """
        self.telemetry_decoder = telemetry_decoder


    def packet_received(self, package_info):

        telemetry_tokens = package_info['payload'].split(";")
        time = telemetry_tokens[2]
        if (time in self.package_time_mark) == False:
            self.package_time_mark.add(time)
            print self.package_time_mark


            if package_info.get('package_type') == 's' or package_info.get('package_type') == 'r':
                self.control_program \
                    .ui_main_window.undecoded_data_from_packages_textEdit.append(str(package_info))
                winsound.PlaySound('./sound_files/command_is_done.wav', winsound.SND_FILENAME)
            elif package_info.get('package_type') == 'r':
                self.control_program \
                    .ui_main_window.undecoded_data_from_packages_textEdit.append(str(package_info))
            # elif package_info.get('package_type') == 'd':
            #     winsound.PlaySound("./sound_files\\telemetry_information_is_reseived.wav", winsound.SND_FILENAME)
            #     self.telemetry_decoder.ui_main_window.undecoded_data_textEdit.append(str(package_info))
            #     telemetry_tokens = package_info['payload'].split(";")
            #     print telemetry_tokens
            #     time = telemetry_tokens[2]
            #     CPU_temperature = telemetry_tokens[3]
            #     payload_module_temperature = telemetry_tokens[4]
            #     payload_module_humidity = telemetry_tokens[5]
            #
            #     data = str(time) + ';' + str(CPU_temperature) + '\n'
            #     log_the_data("./telemetry_log_files/On-board_computer_telemetry_log.csv", data)
            #
            #     try:
            #         send_file_to_the_server('./telemetry_log_files\\', 'On-board_computer_telemetry_log.csv')
            #     except error_perm:
            #         log_the_data("./exception_log_files\exception_log.csv",
            #                      str(time) + ';' + "Cannot access to the server" + '\n')
            #     except error:
            #         log_the_data("./exception_log_files\exception_log.csv",
            #                      str(time) + ';' + "Cannot access to the server" + '\n')
            #
            #     data = str(time) + ';' + str(payload_module_temperature) + ';' + str(payload_module_humidity) + '\n'
            #     log_the_data("./telemetry_log_files/Payload_system_telemetry_log.csv", data)
            #
            #     try:
            #         send_file_to_the_server('./telemetry_log_files\\', 'Payload_system_telemetry_log.csv')
            #     except error_perm:
            #         log_the_data("./exception_log_files\exception_log.csv",
            #                      str(time) + ';' + "Cannot access to the server" + '\n')
            #     except error:
            #         log_the_data("./exception_log_files\exception_log.csv",
            #                      str(time) + ';' + "Cannot access to the server" + '\n')
            #
            #     self.telemetry_decoder.ui_main_window.onboard_computer_CPU_temperature_lcdNumber.\
            #         display(str(CPU_temperature))
            #     self.telemetry_decoder.ui_main_window.payloads_humidity_lcdNumber.\
            #         display(str(payload_module_humidity))
            #     self.telemetry_decoder.ui_main_window.payloads_temperature_lcdNumber.\
            #         display(str(payload_module_temperature))


            elif package_info.get('package_type') == 'e':
                winsound.PlaySound("./sound_files/telemetry_information_is_reseived.wav", winsound.SND_FILENAME)
                self.telemetry_decoder.ui_main_window.undecoded_data_textEdit.append(str(package_info))
                telemetry_tokens = package_info['payload'].split(";")
                print telemetry_tokens
                time = telemetry_tokens[2]
                CPU_temperature = telemetry_tokens[3]
                CPU_usage = telemetry_tokens[4]
                RAM_usage = telemetry_tokens[5]


                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_temperature_lcdNumber.\
                    display(str(CPU_temperature))
                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_usage_lcdNumber.\
                    display(str(CPU_usage))
                self.telemetry_decoder.ui_main_window.onboard_computer_RAM_usage_lcdNumber.\
                    display(str(RAM_usage))

                data = str(time) + ';' + str(CPU_temperature) + ';' + str(CPU_usage) + ';' + str(RAM_usage) +'\n'
                print "data is ",data
                log_the_data("./telemetry_log_files/On-board_computer_telemetry_log.csv", data)

                self.send_file_to_the_server('./telemetry_log_files\\', 'On-board_computer_telemetry_log.csv')
                #TODO: send to web

            elif package_info.get('package_type') == 'n':
                winsound.PlaySound("./sound_files/telemetry_information_is_reseived.wav", winsound.SND_FILENAME)
                self.telemetry_decoder.ui_main_window.undecoded_data_textEdit.append(str(package_info))
                telemetry_tokens = package_info['payload'].split(";")
                print telemetry_tokens
                time = telemetry_tokens[2]
                CPU_temperature = telemetry_tokens[3]
                CPU_usage = telemetry_tokens[4]
                RAM_usage = telemetry_tokens[5]

                data = str(time) + ';' + str(CPU_temperature) + ';' + str(CPU_usage) + ';' + str(RAM_usage) +'\n'
                log_the_data("./telemetry_log_files/On-board_computer_telemetry_log.csv", data)

                self.send_file_to_the_server('./telemetry_log_files\\', 'On-board_computer_telemetry_log.csv')
                #TODO: send to web

                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_temperature_lcdNumber.\
                    display(str(CPU_temperature))
                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_usage_lcdNumber.\
                    display(str(CPU_usage))
                self.telemetry_decoder.ui_main_window.onboard_computer_RAM_usage_lcdNumber.\
                    display(str(RAM_usage))

            elif package_info.get('package_type') == 'o':
                winsound.PlaySound("./sound_files/telemetry_information_is_reseived.wav", winsound.SND_FILENAME)
                self.telemetry_decoder.ui_main_window.undecoded_data_textEdit.append(str(package_info))
                telemetry_tokens = package_info['payload'].split(";")
                print telemetry_tokens
                time = telemetry_tokens[2]
                CPU_temperature = telemetry_tokens[3]
                CPU_usage = telemetry_tokens[4]
                RAM_usage = telemetry_tokens[5]
                payload_module_temperature = telemetry_tokens[6]
                payload_module_humidity = telemetry_tokens[7]

                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_temperature_lcdNumber.\
                    display(str(CPU_temperature))
                self.telemetry_decoder.ui_main_window.onboard_computer_CPU_usage_lcdNumber.\
                    display(str(CPU_usage))
                self.telemetry_decoder.ui_main_window.onboard_computer_RAM_usage_lcdNumber.\
                    display(str(RAM_usage))
                self.telemetry_decoder.ui_main_window.payloads_humidity_lcdNumber.\
                    display(str(payload_module_humidity))
                self.telemetry_decoder.ui_main_window.payloads_temperature_lcdNumber.\
                    display(str(payload_module_temperature))

                data = str(time) + ';' + str(CPU_temperature) + ';' + str(CPU_usage) + ';' + str(RAM_usage) + '\n'
                log_the_data("./telemetry_log_files/On-board_computer_telemetry_log.csv", data)


                self.send_file_to_the_server('./telemetry_log_files\\', 'On-board_computer_telemetry_log.csv')
                params = {"time": time,"temp": payload_module_temperature, "hum": payload_module_humidity}
                # params = {"time": time,"temperature": payload_module_temperature, "humidity": payload_module_humidity}
                # params = {"temperature": payload_module_temperature, "humidity": payload_module_humidity, "time": time}                                                                                                                                                                                                                                                                                      self.send_file_to_the_web_server(params)
                self.send_file_to_the_web_server( "/update", params)
                data = str(time) + ';' + str(payload_module_temperature) + ';' + str(payload_module_humidity) + '\n'
                log_the_data("./telemetry_log_files/Payload_system_telemetry_log.csv", data)

                self.send_file_to_the_server('./telemetry_log_files\\', 'Payload_system_telemetry_log.csv')


    def run(self):
        """ Run the reader thread. """
        # clear old data from port
        if sp_kernel.ser.inWaiting() > 0:
            sp_kernel.ser.readall()

        print "Listening_of_the_RXQ-433_serial_port_is_started"
        print "----------------------------------------------"
        counter = 1
        while True:
            counter+=1

            # if self.communication_protocol.sp_packetAvailable:
            #     self.communication_protocol.sp_packetAvailable = False
            package_info = self.communication_protocol.read()
            if package_info:
                self.packet_received(package_info)


    def send_file_to_the_server(self, addr, name):
        ftp_thread = FTP_thread(self.communication_protocol, addr, name)
        QThreadPool.globalInstance().start(ftp_thread)


    def send_file_to_the_web_server(self, address, params):
        web_thread = WEB_request_thread(address, params)
        QThreadPool.globalInstance().start(web_thread)
