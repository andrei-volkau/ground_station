# -*- coding: utf-8 -*-
from time import gmtime, strftime
from loggers.logger import  log_the_data

ERROR_LOG_ADR = ".\log_files\exception_log_files\exception_log.csv"


def log_the_error(error_message):
    log_the_data(ERROR_LOG_ADR, strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ';' + error_message + '\n')