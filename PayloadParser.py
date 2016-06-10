import json

CAT_NONE = 'NONE'
CAT_ELECTRIC_POWER_SYS = 'electric_power_sys'
CAT_COMMUNICATION_SYS = 'communication_sys'
CAT_ONBOARD_COMP_SYS = 'onboard_comp_sys'
CAT_ATTITUDE_CONTROL_SYS = 'attitude_control_sys'
CAT_PAYLOAD_SYS = 'payload_sys'

SENSOR_TIMESTAMP = 'tel_Timestamp'
SENSOR_OS_CPU0 = 'tel_os_info_cpu_0'
SENSOR_OS_CPU1 = 'tel_os_info_cpu_1'
SENSOR_CPU_TEMP = 'tel_cpu_temp_c'
SENSOR_OS_RAM = 'tel_os_info_ram'
SENSOR_OS_DISK = 'tel_os_info_disk'
SENSOR_BOARD_TEMP = 'tel_cpu_temp_p'
SENSOR_LIGHT1 = 'tel_light_1'
SENSOR_LIGHT2 = 'tel_light_2'
SENSOR_LIGHT3 = 'tel_light_3'
SENSOR_LIGHT4 = 'tel_light_4'
SENSOR_MAGNET_X = 'tel_hmc5883l_x'
SENSOR_MAGNET_Y = 'tel_hmc5883l_y'
SENSOR_MAGNET_Z = 'tel_hmc5883l_z'
SENSOR_ACCELEROMETER_GYROSCOPE_TEMP = 'tel_ms5611_temp'
SENSOR_PAYLOAD_TEMP = 'tel_ds1621'
SENSOR_GYRO_X = 'tel_mpu6050_gyro_x'
SENSOR_GYRO_Y = 'tel_mpu6050_gyro_y'
SENSOR_GYRO_Z = 'tel_mpu6050_gyro_z'
SENSOR_ACCEL_X = 'tel_mpu6050_accel_x'
SENSOR_ACCEL_Y = 'tel_mpu6050_accel_y'
SENSOR_ACCEL_Z = 'tel_mpu6050_accel_z'



SENSOR_TYPES = {
    SENSOR_OS_CPU0: CAT_ONBOARD_COMP_SYS,
    SENSOR_OS_CPU1: CAT_ONBOARD_COMP_SYS,
    SENSOR_CPU_TEMP: CAT_ONBOARD_COMP_SYS,
    SENSOR_OS_RAM: CAT_ONBOARD_COMP_SYS,
    SENSOR_OS_DISK: CAT_ONBOARD_COMP_SYS,
    SENSOR_BOARD_TEMP: CAT_ONBOARD_COMP_SYS,
    SENSOR_LIGHT1: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_LIGHT2: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_LIGHT3: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_LIGHT4: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_MAGNET_X: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_MAGNET_Y: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_MAGNET_Z: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_ACCELEROMETER_GYROSCOPE_TEMP: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_PAYLOAD_TEMP: CAT_PAYLOAD_SYS,
    SENSOR_GYRO_X: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_GYRO_Y: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_GYRO_Z: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_ACCEL_X: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_ACCEL_Y: CAT_ATTITUDE_CONTROL_SYS,
    SENSOR_ACCEL_Z: CAT_ATTITUDE_CONTROL_SYS
}


def traverse_tree(name, data, output):
    if isinstance(data, dict):
        for key in data:
            item = data[key]
            traverse_tree(name + "_" + key, item, output)
    else:
        output[name] = data


def get_category(key):
    if key in SENSOR_TYPES:
        return SENSOR_TYPES[key]
    return CAT_NONE


def parse_ax25_payload(packet):
    raw_telemetry = {}
    print packet
    traverse_tree("tel", json.loads(packet), raw_telemetry)
    payload = {}
    for key in raw_telemetry:
        payload[key] = {"cat": get_category(key), "val": raw_telemetry[key]}
    return payload
