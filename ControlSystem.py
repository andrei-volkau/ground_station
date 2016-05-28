from PyQt4.QtCore import QObject

CMD_EMERGENCY = "CMD_EMERGENCY"
CMD_NOMINAL = "CMD_NOMINAL"
CMD_OPERATING = "CMD_OPERATING"
CMD_ENABLE_TRANSMISSION = "CMD_ENABLE_TRANSMISSION"
CMD_DISABLE_TRANSMISSION = "CMD_DISABLE_TRANSMISSION"


class ControlSystem(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        # communication_protocol = sp_kernel.SerialProtocol()
        # writer_thread = WriterThread.WriterThread(self, communication_protocol)
        # reader_thread = ReaderThread.ReaderThread(self, communication_protocol)
        # kiss_thread = KISS_thread.KISS_thread(self, reader_thread)
        # reader_thread.start()
        # writer_thread.start()
        # kiss_thread.start()

    def send_command(self, cmd):
        print "Issued command:", cmd
