from PyQt4.QtGui import QSound

CMD_IS_SENT = "./sound_files/command_is_sent.wav"
CMD_IS_DONE = "./sound/files/command_is_done.wav"
TELEMETRY_RECEIVED = "./sound/files/telemetry_information_is_reseived.wav"


def play(file_address):
    QSound(file_address).play()
