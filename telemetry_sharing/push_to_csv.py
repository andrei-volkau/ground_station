import csv

from PayloadParser import CAT_ELECTRIC_POWER_SYS, CAT_COMMUNICATION_SYS, CAT_ONBOARD_COMP_SYS, CAT_PAYLOAD_SYS, \
    CAT_ATTITUDE_CONTROL_SYS


FIELD_NAMES = {
    CAT_ELECTRIC_POWER_SYS: [],
    CAT_COMMUNICATION_SYS: [],
    CAT_ONBOARD_COMP_SYS: [
        'tel_os_info.py_cpu_0',
        'tel_os_info.py_cpu_1',
        'tel_cpu_temp_c',
        'tel_os_info.py_ram',
        'tel_os_info.py_disk',
        'tel_cpu_temp_p'
    ],
    CAT_ATTITUDE_CONTROL_SYS: [
        'tel_light_1',
        'tel_light_2',
        'tel_light_3',
        'tel_light_4',
        'tel_hmc5883l_x',
        'tel_hmc5883l_y',
        'tel_hmc5883l_z',
        'tel_ms5611_temp'
    ],
    CAT_PAYLOAD_SYS: [
        'tel_ds1621'
    ]
}


def write_to_csv(cat, superLinearTelemetry):
    if cat not in FIELD_NAMES:
        return
    fieldnames = FIELD_NAMES[cat]
    with open("./log_files/telemetry_log_files/" + cat + '.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        tel = {}
        for key in superLinearTelemetry:
            if key in fieldnames:
                tel[key] = superLinearTelemetry[key]
        writer.writerow(tel)


def write_2(linearTelemetry):
    t = {}
    for key in linearTelemetry:
        cat = linearTelemetry[key][0]
        val = linearTelemetry[key][1]
        if cat in t:
            t[cat][key] = val
        else:
            t[cat] = {key: val}
    for cat in t:
        print t[cat]
        write_to_csv(cat, t[cat])


def push_to_csv(linearPayload):
    for key in linearPayload:
        category = linearPayload[key][0]
        value = linearPayload[key][1]
        write_2(linearPayload)
    print "ftp ", linearPayload



