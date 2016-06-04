from PyQt4.QtCore import QThreadPool

from PayloadParser import CAT_TIME

from telemetry_sharing.SatelliteAPI import SatelliteAPI


WEB_HOST = 'sputnik-bsu.herokuapp.com'
WEB_PASSWORD = 'abc'


def push_to_website(linearPayload):
    time = linearPayload["tel_Timestamp"][1]
    for key in linearPayload:
        category = linearPayload[key][0]
        value = linearPayload[key][1]

        if category == CAT_TIME:
            continue

        api = SatelliteAPI()
        api.set_password(WEB_PASSWORD)
        api.set_host(WEB_HOST)
        api.set_data(category, key, value, time)
        QThreadPool.globalInstance().start(api)

