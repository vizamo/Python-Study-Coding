"""Functions for generation of sample preparation, which is used in other tests"""
import sys

sys.path.insert(0, "..")
from app.weather_app import *


def create_sample_file(cities_count: int, filename: str = "cities_for_owm.txt", example_cities=True):
    """
    Create a sample file for testing application, where will be names of cities
    :param example_cities: example cities list
    :param cities_count: hom many cities add in file
    :param filename: name of the file with cities
    :return: True, if file is created. False if creation failed
    """
    if example_cities is True:
        example_cities = ["Tallinn", "London", "New York", "Prague", "Paris", "Brussels", "Amsterdam"]
    file_path = f"../app/{filename}"
    with open(file_path, 'w') as file:
        for t_city in example_cities[0:cities_count]:
            file.write(t_city)
            if len(t_city) > 0:
                file.write("\n")


def example_owm_request(t_city, service):
    """
    Use OWM API and create simple data request for compare with out application output
    :param t_city: name of example city
    :param service: does it weather or forecast data
    :return: output from owm api
    """
    api_key = "81f4883e62f5ec5c7ec74e04ebb662ed"  # Unique API key for our client
    base_url = "http://api.openweathermap.org/data/2.5/"  # OpenWeatherAPI basic url for requests of data
    complete_url = base_url + service + "?appid=" + api_key + "&q=" + t_city + "&units=metric"
    owm_report = requests.get(complete_url)
    return owm_report.json()


def basic_report_for_test(t_city: str = "Tallinn"):
    """
    Reduce code for tests with similar city
    :param t_city: name of testing city
    :return: CityReportProcess class for defined city
    """
    test_city = City(t_city)
    test_city_report = CityReport(test_city)
    return test_city_report


def basic_report_process_for_test(t_city: str = "Tallinn"):
    """
    Reduce code for tests with similar city
    :param t_city: name of testing city
    :return: CityReportProcess class for defined city
    """
    test_report_process = CityReportProcess(basic_report_for_test(t_city))
    return test_report_process


def basic_output_manager_for_test(t_city: str = "Tallinn"):
    """
    Reduce code for tests with similar city
    :param t_city: name of testing city
    :return: ReportOutputManager class for defined city
    """
    test_output_mgr = ReportOutputManager(basic_report_process_for_test(t_city))
    return test_output_mgr
