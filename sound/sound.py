# -*- coding: utf-8 -*-
import codecs
import time
import config
from PyQt4.QtGui import QSound
import tempfile

#CMD_IS_SENT = "./sound_files/command_is_sent.wav"
#CMD_IS_DONE = "./sound/files/command_is_done.wav"
#TELEMETRY_RECEIVED = "./sound/files/telemetry_information_is_received.wav"

CMD_IS_SENT = u"команда отправлена"
CMD_IS_DONE = u"команда выполнена"
TELEMETRY_RECEIVED = u"телеметрия принята"



def play(text_to_read):
    if not config.SOUND_ENABLED:
        return
    print("sound ", text_to_read)
    #QSound(file_address).play()
    with codecs.open("./files_for_play/" + str(time.time()) + ".txt", "w", "utf8") as a:
        a.write(text_to_read)


def parse_data(data):
    if not config.SOUND_ENABLED:
        return
    text =''
    print("PARSE DATA ")
    try:
        text += u'Напряжение  аккумуляторных батарей равно {0} Вольта. \n'.format(data['power']['vs'])

    except:
        pass

    try:
        text += u'Загруженность ОЗУ бортового компьютера равна {0} процента. \n'.format(data['os_info']['cpu'][1])

    except:
        pass

    try:
        text += u'Температура  процессора {0} градусов Цельсия. \n '.format(data['cpu_temp']['c'])

    except:
        pass

    try:
        text += u'Температур полезной нагрузки {0} градусов Цельсия.. \n '.format(data['ds1621'])

    except:
        pass

    try:
        text += u'Температуры внешней среды равна {0} градусов Цельсия.\n '.format(data['ms5611']['temp'])

    except:
        pass

    try:
        magn = data['hmc5883l']
        text += u'Значение магнитометра в мили Гаусах: икс  {0}, игрек  {1}, зет  {2}.\n '.format(round(magn['x'],2),
                                                                                                 round(magn['y'],2),
                                                                                                 round(magn['z'],2))

    except:
        pass
    try:
       gyro = data['mpu6050']['gyro']
       text += u'Значение гироскопа в градусов d c. : икс {0}, игрек  {1}, зет  {2}. \n '.format(round(gyro['x'],2),
                                                                                                 round(gyro['y'],2),
                                                                                                 round(gyro['z'],2))

       accel = data['mpu6050']['accel']
       text += u'Значение акселерометра в метрах в секунду в квадрате. : икс  {0}, игрек  {1}, зет  {2}\n. '.format(round(accel['x'],2),
                                                                                                 round(accel['y'],2),
                                                                                                 round(accel['z'],2))

    except:
        pass

    try:
        light = data['light']
        #text += u'Cолнечные датчики 1  {0}, 2  {1}, 3  {2} ватт на метр в квадрате.\n '.format(light['1'],
        #        light['2'],
        #        light['3'],
        #        light['4'])

    except:
        pass

    play(text)

def format_message(data, *args):
    if data == None:
        return
    #for arg in args:

