import sys

from PyQt4 import QtCore
import requests
from loggers.error_logger import log_the_error


class SputnikAPI(QtCore.QRunnable):
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
            r = requests.post(self.url, data=self.data)
            print r.content
        except:
            error_message = "It is impossible to access to the WEB-server" + ";" + str(sys.exc_info())
            log_the_error(error_message)
