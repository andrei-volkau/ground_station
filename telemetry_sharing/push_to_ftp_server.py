from PyQt4.QtCore import QThreadPool
from PayloadParser import CAT_ATTITUDE_CONTROL_SYS, CAT_PAYLOAD_SYS, CAT_ONBOARD_COMP_SYS
from telemetry_sharing.FTP_ServerAPI import FTP_ServerAPI
from telemetry_sharing.push_to_csv import CSV_TEL_DIRECTORY


def push_file_to_ftp_server(file_address, file_name):
    api = FTP_ServerAPI(file_address, file_name)
    QThreadPool.globalInstance().start(api)

def push_to_ftp_server():
        push_file_to_ftp_server(CSV_TEL_DIRECTORY, CAT_PAYLOAD_SYS + ".csv")
        push_file_to_ftp_server(CSV_TEL_DIRECTORY, CAT_ATTITUDE_CONTROL_SYS + ".csv")
        push_file_to_ftp_server(CSV_TEL_DIRECTORY, CAT_ONBOARD_COMP_SYS + ".csv")

