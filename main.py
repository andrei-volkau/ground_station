# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from communication_protocol_kernel import sp_kernel
import ReaderThread
import WriterThread
from GUI_for_telemetry_decoder import GUI_for_telemetry_decoder
from GUI_for_control_program import GUI_for_control_program
import KISS_thread


communication_protocol = sp_kernel.SerialProtocol()
app = QtGui.QApplication(sys.argv)
writer_thread = WriterThread.WriterThread(communication_protocol)
telemetry_decoder = GUI_for_telemetry_decoder()
control_program = GUI_for_control_program(writer_thread)

reader_thread = ReaderThread.ReaderThread(control_program, communication_protocol)
reader_thread.set_telemetry_decoder(telemetry_decoder)
reader_thread.set_control_program(control_program)

kiss_thread = KISS_thread.KISS_thread(reader_thread)

telemetry_decoder.show()
control_program.show()

reader_thread.start()
writer_thread.start()
kiss_thread.start()

app.exec_()



