"""Logs creation and error generation for weather app"""
import datetime


def logging(log_level_code: int, msg: str):
    timestamp = datetime.datetime.now()
    log_level = ["FATAL", "ERROR", "INFO"]
    log = str(timestamp) + "  " + log_level[log_level_code - 1] + "  " + msg + "\n"

    print(log)
    with open(f"../output/log.txt", 'a') as log_file:
        log_file.write(log)


class CityNotExistError(Exception):
    """Raised when the not existing city is tried to process in CityReportProcess"""

    def __init__(self):
        self.message = "This city cannot be found from our application. Provide the existing or correct city name."
        logging(1, self.message)
        super().__init__(self.message)


class NotSupportedExtensionError(Exception):
    """Raised when the file format is not supported my application --> not .txt file extension"""

    def __init__(self):
        self.message = "Wrong file extension. Input file must have .txt extension."
        logging(1, self.message)
        super().__init__(self.message)
