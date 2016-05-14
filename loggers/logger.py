# -*- coding: utf-8 -*-


def log_the_data(file_address, data):
    """Log given data to the file, which have given address.

    Args:
     file_address (str): Destination address of the log file.
     data (str): Data that that will be logged to the log file.
    """
    log_file = open(file_address, "a")
    log_file.write(data)
    log_file.close()