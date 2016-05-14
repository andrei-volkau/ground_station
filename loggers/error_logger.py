# -*- coding: utf-8 -*-
from time import gmtime, strftime
from loggers.logger import  log_the_data


def log_the_error(error_message):
    log_the_data("./exception_log_files\exception_log.csv",
                         strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ';' + error_message + '\n')