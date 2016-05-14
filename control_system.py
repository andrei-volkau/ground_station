# -*- coding: utf-8 -*-
from PyQt4.QtCore import QObject
import KISS_thread
import ReaderThread
import WriterThread
from communication_protocol_kernel import sp_kernel


class ControlSystem(QObject):
    """  """

    def __init__(self, event_manager):
        QObject.__init__(self)
        communication_protocol = sp_kernel.SerialProtocol()
        writer_thread = WriterThread.WriterThread(communication_protocol)
        reader_thread = ReaderThread.ReaderThread(control_program, communication_protocol)
        reader_thread.set_telemetry_decoder(telemetry_decoder)
        reader_thread.set_control_program(control_program)
        kiss_thread = KISS_thread.KISS_thread(reader_thread)
        reader_thread.start()
        writer_thread.start()
        kiss_thread.start()

