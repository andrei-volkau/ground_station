import csv

from PayloadParser import *


FIELD_NAMES = {
    CAT_ELECTRIC_POWER_SYS: [
        SENSOR_TIMESTAMP
    ],
    CAT_COMMUNICATION_SYS: [
        SENSOR_TIMESTAMP
    ],
    CAT_ONBOARD_COMP_SYS: [
        SENSOR_TIMESTAMP,
        SENSOR_OS_CPU0,
        SENSOR_OS_CPU1,
        SENSOR_CPU_TEMP,
        SENSOR_OS_RAM,
        SENSOR_OS_DISK,
        SENSOR_BOARD_TEMP
    ],
    CAT_ATTITUDE_CONTROL_SYS: [
        SENSOR_TIMESTAMP,
        SENSOR_LIGHT1,
        SENSOR_LIGHT2,
        SENSOR_LIGHT3,
        SENSOR_LIGHT4,
        SENSOR_MAGNET_X,
        SENSOR_MAGNET_Y,
        SENSOR_MAGNET_Z,
        SENSOR_ACCELEROMETER_GYROSCOPE_TEMP
    ],
    CAT_PAYLOAD_SYS: [
        SENSOR_TIMESTAMP,
        SENSOR_PAYLOAD_TEMP
    ]
}

CSV_TEL_DIRECTORY = "./log_files/telemetry_log_files/"

def get_csv_filename(category):
    return CSV_TEL_DIRECTORY + category + ".csv"


def write_to_csv(time, cat, telemetry):
    # print "write_to_csv", time, cat, telemetry
    if cat not in FIELD_NAMES:
        return
    fieldnames = FIELD_NAMES[cat]
    with open(get_csv_filename(cat), 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        tel = {}
        tel[SENSOR_TIMESTAMP] = time
        for key in telemetry:
            if key in fieldnames:
                tel[key] = telemetry[key]
        if len(tel) == 0:
            return
        writer.writerow(tel)


def push_to_csv(payload):
    time = payload[SENSOR_TIMESTAMP]["val"]
    telemetry = {}
    for key in payload:
        cat = payload[key]["cat"]
        val = payload[key]["val"]
        if cat in telemetry:
            telemetry[cat][key] = val
        else:
            telemetry[cat] = {key: val}
    for cat in telemetry:
        write_to_csv(time, cat, telemetry[cat])
