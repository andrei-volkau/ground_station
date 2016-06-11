from PyQt4.QtCore import QThreadPool

from PayloadParser import SENSOR_TIMESTAMP, CAT_NONE
from telemetry_sharing.WebsiteAPI import WebsiteAPI


WEB_HOST = 'sputnik-bsu.herokuapp.com'
WEB_PASSWORD = 'abc'


def push_to_website(payload):
    time = payload[SENSOR_TIMESTAMP]["val"]
    for key in payload:
        category = payload[key]["cat"]
        value = payload[key]["val"]

        if category == CAT_NONE:
            continue

        api = WebsiteAPI()
        api.set_password(WEB_PASSWORD)
        api.set_host(WEB_HOST)
        api.set_data(category, key, value, time)
        QThreadPool.globalInstance().start(api)

