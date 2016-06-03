from telemetry_sharing.SatelliteAPI import SatelliteAPI
from PyQt4.QtCore import QThreadPool

WEB_HOST = 'sputnik-bsu.herokuapp.com'
WEB_PASSWORD = 'abc'

CAT_ELECTRIC_POWER_SYS = 'electric_power_sys'
CAT_COMMUNICATION_SYS = 'communication_sys'
CAT_ONBOARD_COMP_SYS = 'onboard_comp_sys'
CAT_ATTITUDE_CONTROL_SYS = 'attitude_control_sys'
CAT_PAYLOAD_SYS = 'payload_sys'


def traverse_tree(name, data, output):
    if isinstance(data, dict):
        for key in data:
            item = data[key]
            traverse_tree(name + "_" + key, item, output)
    else:
        output[name] = data


def push_to_website(data):
    out = {}
    traverse_tree("tel", data, out)
    time = out.pop("tel_Timestamp")
    for key in out:
        category = CAT_ATTITUDE_CONTROL_SYS
        if key.startswith("tel_ds1621"):
            category = CAT_PAYLOAD_SYS
        if key.startswith("tel_ms5611_pressure"):
            category = CAT_PAYLOAD_SYS
        if key.startswith("tel_ms5611_temp"):
            category = CAT_PAYLOAD_SYS

        api = SatelliteAPI()
        api.set_password(WEB_PASSWORD)
        api.set_host(WEB_HOST)
        api.set_data(category, key, out[key], time)
        QThreadPool.globalInstance().start(api)

