import json

CAT_TIME                = 'time'
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


def assign_category(key, val):
    category = CAT_ATTITUDE_CONTROL_SYS
    if key == "tel_Timestamp":
        category = CAT_TIME
    if key.startswith("tel_ds1621"):
        category = CAT_PAYLOAD_SYS
    if key.startswith("tel_ms5611"):
        category = CAT_ATTITUDE_CONTROL_SYS
    if key.startswith("tel_os_info.py"):
        category = CAT_ONBOARD_COMP_SYS
    if key.startswith("tel_cpu_temp"):
        category = CAT_ONBOARD_COMP_SYS
    return (category, val)


def parse_ax25_payload(payload):
    out = {}
    traverse_tree("tel", json.loads(payload), out)
    return {k: assign_category(k, out[k]) for k in out}
