# -*- coding: utf-8 -*-
import codecs
from PyQt4.QtGui import QSound
import tempfile

#CMD_IS_SENT = "./sound_files/command_is_sent.wav"
#CMD_IS_DONE = "./sound/files/command_is_done.wav"
#TELEMETRY_RECEIVED = "./sound/files/telemetry_information_is_received.wav"
import time

CMD_IS_SENT = u"команда отправлена"
CMD_IS_DONE = u"команда выполнена"
TELEMETRY_RECEIVED = u"телеметрия принята"



def play(text_to_read):
    print("sound ", text_to_read)
    #QSound(file_address).play()
    with codecs.open("./files_for_play/" + str(time.time()) + ".txt", "w", "utf8") as a:
        a.write(text_to_read)


def parse_data(data):
    print("PARSE DATA ")
    template = u"Температура  {0} градусов, давление {1} бар."
    try:
        ms5611 = data['ms5611']
        play(template.format(ms5611['temp'], ms5611['pressure']))
    except:
        pass

def format_message(data, *args):
    if data == None:
        return
    #for arg in args:

