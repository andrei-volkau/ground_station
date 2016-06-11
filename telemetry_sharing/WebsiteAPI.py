import sys

import requests
from PyQt4 import QtCore

from loggers.error_logger import log_the_error


class WebsiteAPI(QtCore.QRunnable):
    def __init__(self):
        super(WebsiteAPI, self).__init__()

    # Example: server.set_password('abc')
    def set_password(self, password):
        self.password = password

    # Example: server.set_host('sputnik-bsu.herokuapp.com')
    def set_host(self, url):
        self.url = 'http://' + url + '/api/v1/sensors'

    # Example: server.push('payloads', 'humidity', 21, 10)
    def set_data(self, category, sensor, value, time):
        self.data = {'password': self.password, 'category_name': category, 'sensor_name': sensor, 'value': value,
                     'time': time}

    def run(self):
        try:
            webRequest = requests.post(self.url, data=self.data)
            resp = webRequest.content
            if "error" in resp:
                print "web request content is: ", resp
        except:
            error_message = "It is impossible to access to the WEB-server" + ";" + str(sys.exc_info())
            log_the_error(error_message)
