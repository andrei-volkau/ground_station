from telemetry_sharing.SputnikAPI import SputnikAPI

__author__ = 'User'
from PyQt4.QtCore import QThreadPool

WEB_HOST = 'sputnik-bsu.herokuapp.com'
WEB_PASSWORD = 'abc'

CAT_PAYLOADS = "payloads"
CAT_ATTITUDE_CONTROL = "attitude-control"

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
        category = CAT_ATTITUDE_CONTROL
        if key.startswith("tel_ds1621"):
            category = CAT_PAYLOADS
        if key.startswith("tel_ms5611_pressure"):
            category = CAT_PAYLOADS
        if key.startswith("tel_ms5611_temp"):
            category = CAT_PAYLOADS

        api = SputnikAPI()
        api.set_password(WEB_PASSWORD)
        api.set_host(WEB_HOST)
        api.set_data(category, key, out[key], time)
        QThreadPool.globalInstance().start(api)

