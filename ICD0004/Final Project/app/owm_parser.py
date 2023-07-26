"""OWM API parser for creating weather report of different cities"""
from app.input_file_handler import *
from app.logging_and_error_handler import *
import requests


class CityReport:
    """Get report from OWM for current city and process it"""

    def __init__(self, city: City):
        """
        :param city: city class, for which we want to have report
        """
        self.city = city
        self.api_key = "81f4883e62f5ec5c7ec74e04ebb662ed"  # Unique API key for our client
        self.base_url = "http://api.openweathermap.org/data/2.5/"  # OpenWeatherAPI basic url for requests of data
        self.weather_report = {}
        self.forecast_report = {}

        self.create_city_report()
        self.create_city_report("forecast")
        self.validate_status_code()

    def create_city_report(self, service="weather", params="&units=metric"):
        """
        Send request to OWM API for weather report and save it as json
        :param params: Add to OWM API request some parameters. Useful for forecast days limitation, temperature units.
        :param service: Which OWM API service is use - Weather report or Forecast Report
        """
        complete_url = self.base_url + service + "?appid=" + self.api_key + "&q=" + self.city.city + params
        owm_report = requests.get(complete_url)
        owm_report_json = owm_report.json()
        if service == "weather":
            logging(3, f"Weather report for city {self.city} is successfully generated")
            self.weather_report = owm_report_json
        elif service == "forecast":
            logging(3, f"Forecast report for city {self.city} is successfully generated")
            self.forecast_report = owm_report_json
        else:
            logging(1, "Faulty report creation service parameter")
            raise AttributeError
        return owm_report_json

    def validate_status_code(self):
        """
        Check a report for status code of creation
        HTTP Status Code 200 means, that request is successfully created and returned
        HTTP Status Code 404 means, that city is not found
        """
        if self.weather_report['cod'] == 200 and self.forecast_report['cod'] == '200':
            self.city.is_exist = True
            logging(3, f"City {self.city} existence is confirmed")
            return True
        elif self.weather_report['cod'] == '404' or self.forecast_report['cod'] == '404':
            self.city.is_exist = False
            logging(2, f"City {self.city} does not exist and reports are unusable")
            return False


class CityReportProcess:
    """Process created full report for filtering and formatting variables until required condition"""

    def __init__(self, report: CityReport):
        """
        :param report: CityReport class, where is created a full report
        """
        self.report = report
        self.validate_report_for_existing_city()

        self.main_details_ready_report = {}
        self.weather_ready_report = {}
        self.forecast_ready_report = {}

        self.process_main_details()
        self.process_current_weather()
        self.process_forecast()
        logging(3, f"Report for city {self.report.city} is successfully processed")

    def process_main_details(self):
        """
        Process full report for saving only required details about city and report itself
        Required: city, coordinates, temperatureUnit
        :return: filtered main details report dictionary
        """
        full_report = self.report.weather_report

        city = full_report['name']
        temperature_unit = "Celsius"
        coordinates = str(full_report['coord']['lat']) + "," + str(full_report['coord']['lon'])

        report = {"city": city, "coordinates": coordinates, "temperatureUnit": temperature_unit}
        self.main_details_ready_report = report
        return report

    def process_current_weather(self):
        """
        Process full report for saving only required details about current weather information
        Required: date, temperature, humidity, pressure
        :return: filtered current weather report dictionary
        """
        full_report = self.report.weather_report
        full_report_weather = self.process_main_weather_details(full_report)

        # Convert epoch timestamp to the date
        date = datetime.datetime.fromtimestamp(full_report['dt']).strftime("%d-%m-%Y")

        report = {"date": date}
        report.update(full_report_weather)
        self.weather_ready_report = report
        return report

    def process_forecast(self):
        """
        Process full report for saving only required details about 3 days forecast
        Required for each day: date, temperature, humidity, pressure
        :return: filtered forecast report dictionary
        """
        full_report = self.report.forecast_report
        full_report_all_msg = full_report['list']

        today_date = datetime.date.today().strftime("%Y-%m-%d") + " 12:00:00"
        day_num = 0
        report = []

        for forecast_msg in full_report_all_msg:
            forecast_timestamp = forecast_msg['dt_txt']
            timestamp_check = re.search("....-..-.. 12:00:00", forecast_timestamp)  # Use only launch forecasts
            if day_num < 3 and timestamp_check is not None and forecast_timestamp != today_date:
                forecast_for_day = self.process_forecast_day(forecast_msg)
                report.append(forecast_for_day)
                day_num += 1
            if day_num == 3:
                break

        self.forecast_ready_report = report
        return report

    def process_forecast_day(self, forecast_msg):
        """
        Process forecast report for saving only required details about one day forecast
        Required for each day: date, temperature, humidity, pressure
        :type forecast_msg: dict of full report for that day
        :return: filtered forecast day report dictionary
        """
        weather_report = self.process_main_weather_details(forecast_msg)

        # Convert epoch timestamp to the date
        date = datetime.datetime.fromtimestamp(forecast_msg['dt']).strftime("%d-%m-%Y")

        report = {"date": date, "weather": weather_report}
        return report

    @staticmethod
    def process_main_weather_details(report_to_process) -> dict:
        """
        Process weather report for saving only required details about weather
        Required: date, temperature, humidity, pressure
        :type report_to_process: dict of full report for that day
        :return: filtered only weather day report dictionary
        """
        weather_report = report_to_process['main']

        temperature = weather_report['temp']
        humidity = weather_report['humidity']
        pressure = weather_report['pressure']

        report = {"temperature": temperature, "humidity": humidity, "pressure": pressure}
        return report

    def validate_report_for_existing_city(self):
        """City, which is not exist --> doesn't have report to process --> must not be processed"""
        if self.report.city.is_exist is not True:
            raise CityNotExistError
        return True
