"""Tests for ICA0004 Test Automation Project"""
import pytest
import sys
sys.path.insert(0, "..")
from tests.common_calls_for_tests import *


def test_city_report_class_report_creation_returns_dict():
    """
    City report class function create_city_report() must return answer in not empty dictionary
    """
    test_city_report = basic_report_for_test()
    test_report = test_city_report.create_city_report()
    assert type(test_report) == dict
    assert len(test_report) > 0


def test_city_report_class_report_creation_fill_weather_variable():
    """
    City report class function create_city_report() must create a weather report
    """
    test_city_report = basic_report_for_test()
    assert type(test_city_report.weather_report) == dict
    assert len(test_city_report.weather_report) > 0


def test_city_report_class_report_creation_fill_forecast_variable():
    """
    City report class function create_city_report() must create a forecast report
    """
    test_city_report = basic_report_for_test()
    assert type(test_city_report.forecast_report) == dict
    assert len(test_city_report.forecast_report) > 0


def test_city_report_class_returns_200_status_for_existing_city_weather_report():
    """
    City report class must return 200 status code for weather report,
    if operation is successful and city exist
    """
    test_city_report = basic_report_for_test()
    assert test_city_report.weather_report['cod'] == 200


def test_city_report_class_returns_200_status_for_existing_city_forecast_report():
    """
    City report class must return 200 status code for forecast report,
    if operation is successful and city exist
    """
    test_city_report = basic_report_for_test()
    assert test_city_report.forecast_report['cod'] == "200"


def test_city_report_class_report_creation_have_true_attribute_for_existing_city():
    """
    City report class must have is_exist = True, if city exist
    """
    test_city = City("Tallinn")
    CityReport(test_city)
    assert test_city.is_exist is True


def test_city_report_class_returns_404_status_for_existing_city_weather_report():
    """
    City report class must return 404 status code for weather report,
    if operation is successful but city not exist
    """
    test_city_report = basic_report_for_test("Tallinnackl")
    assert test_city_report.weather_report['cod'] == '404'


def test_city_report_class_returns_404_status_for_existing_city_forecast_report():
    """
    City report class must return 404 status code for forecast report,
    if operation is successful but city not exist
    """
    test_city_report = basic_report_for_test("Tallinnackl")
    assert test_city_report.forecast_report['cod'] == '404'


def test_city_report_class_report_creation_returns_not_found_msg_for_not_existing_city():
    """
    City report class func create_city_report() must return "not found" message,
    if operation is successful but city not exist
    """
    test_city_report = basic_report_for_test("Tallinnackl")
    assert test_city_report.weather_report['message'] == "city not found"


def test_city_report_class_report_not_found_msg_for_not_existing_city_weather_report():
    """
    City report class func create_city_report() must return "not found" message,
    if operation is successful but city not exist
    """
    test_city_report = basic_report_for_test("Tallinnackl")
    assert test_city_report.forecast_report['message'] == "city not found"


def test_city_report_class_report__not_found_msg_for_not_existing_city_forecast_report():
    """
    City report class must have is_exist = False, if city not exist
    """
    test_city = City("Tallinnackl")
    CityReport(test_city)
    assert test_city.is_exist is False


# Reports is ready. Process them to filter unusable information and prepare report for output


def test_city_report_gets_correct_weather_report_information():
    """
    Application class CityReport must fill weather variable with correct and current weather report from OWM API
    """
    test_city_report = basic_report_for_test()
    example_owm_report = example_owm_request("Tallinn", "weather")

    # Except time difference between process of requests
    test_weather_report = test_city_report.weather_report
    example_owm_report['dt'] = 0
    test_weather_report['dt'] = 0

    assert test_weather_report == example_owm_report


def test_city_report_gets_correct_forecast_report_information():
    """
    Application class CityReport must fill forecast variable with correct
    and current forecast 3 days report from OWM API
    """
    test_city_report = basic_report_for_test()
    example_owm_report = example_owm_request("Tallinn", "forecast")

    # Except time difference between process of requests
    test_forecast_report = test_city_report.forecast_report
    example_owm_report['dt'] = 0
    test_forecast_report['dt'] = 0

    assert test_forecast_report == example_owm_report


def test_report_process_returns_error_is_city_not_exist():
    """
    Class CityReportProcess raises error, if trying to process not existing city
    """
    with pytest.raises(CityNotExistError) as exc:
        test_city = City("Tallinnackl")
        test_city_report = CityReport(test_city)
        CityReportProcess(test_city_report)
    assert "This city cannot be found from our application. " \
           "Provide the existing or correct city name." in str(exc.value)


def test_processed_main_details_report_process_returns_not_empty_dict():
    """
    Class CityReportProcess function process_main_details must return dict of filtered main details
    """
    test_report_process = basic_report_process_for_test()
    test_main_d_report_pr = test_report_process.process_main_details()
    assert type(test_main_d_report_pr) == dict
    assert len(test_main_d_report_pr) > 0


def test_processed_weather_report_process_returns_not_empty_dict():
    """
    Class CityReportProcess function process_current_weather must return dict of filtered current weather information
    """
    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()
    assert type(test_weather_report_pr) == dict
    assert len(test_weather_report_pr) > 0


def test_processed_forecast_report_process_returns_not_empty_dict():
    """
    Class CityReportProcess function process_forecast must return list of dicts of filtered 3 days forecast information
    """
    test_report_process = basic_report_process_for_test()
    test_forecast_report_pr = test_report_process.process_forecast()
    assert type(test_forecast_report_pr) == list
    assert len(test_forecast_report_pr) > 0


def test_processed_main_details_report_func_fill_main_details_variable():
    """
    Class CityReportProcess function process_main_details must add filtered main details into class variable
    """
    test_report_process = basic_report_process_for_test()
    test_report_process.process_main_details()
    assert type(test_report_process.main_details_ready_report) == dict
    assert len(test_report_process.main_details_ready_report) > 0


def test_processed_weather_report_func_fill_weather_variable():
    """
    Class CityReportProcess function process_current_weather must add filtered current weather info into class variable
    """
    test_report_process = basic_report_process_for_test()
    test_report_process.process_current_weather()
    assert type(test_report_process.weather_ready_report) == dict
    assert len(test_report_process.weather_ready_report) > 0


def test_processed_forecast_report_func_fill_forecast_variable():
    """
    Class CityReportProcess function process_forecast must add filtered forecast info into class variable
    """
    test_report_process = basic_report_process_for_test()
    test_report_process.process_forecast()
    assert type(test_report_process.forecast_ready_report) == list
    assert len(test_report_process.forecast_ready_report) > 0


def test_processed_main_details_report_variable_have_correct_city_name():
    """
    Class CityReportProcess main details processing function output
    must have same name as given city name
    """
    test_report_process = basic_report_process_for_test()
    test_main_d_report_pr = test_report_process.process_main_details()
    assert test_main_d_report_pr['city'] == "Tallinn"


def test_processed_main_details_report_variable_have_correct_coordinates():
    """
    Class CityReportProcess main details processing function output
    must have same name as given city latitude and longitude
    """
    test_report_process = basic_report_process_for_test()
    test_main_d_report_pr = test_report_process.process_main_details()
    assert test_main_d_report_pr['coordinates'] == "59.437,24.7535"


def test_processed_main_details_report_variable_have_celsius_temperature_units():
    """
    Class CityReportProcess main details processing function output
    must have temperature units in celsius
    """
    test_report_process = basic_report_process_for_test()
    test_main_d_report_pr = test_report_process.process_main_details()
    assert test_main_d_report_pr['temperatureUnit'] == "Celsius"


def test_processed_main_details_report_variable_equal_to_main_details_process_return():
    """
    Class CityReportProcess main details processing function output
    must be equal to filtered main details report variable
    """
    test_report_process = basic_report_process_for_test()
    test_main_d_report_pr = test_report_process.process_main_details()
    assert test_main_d_report_pr == test_report_process.main_details_ready_report


def test_processed_weather_report_returns_actual_temperature():
    """
    Class CityReportProcess current weather processing function output
    must have actual temperature information
    """
    example_owm_report = example_owm_request("Tallinn", "weather")
    example_owm_report_temperature = example_owm_report['main']['temp']

    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()

    assert test_weather_report_pr['temperature'] == example_owm_report_temperature


def test_processed_weather_report_returns_actual_humidity():
    """
    Class CityReportProcess current weather processing function output
    must have actual humidity information
    """
    example_owm_report = example_owm_request("Tallinn", "weather")
    example_owm_report_humidity = example_owm_report['main']['humidity']

    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()

    assert test_weather_report_pr['humidity'] == example_owm_report_humidity


def test_processed_weather_report_returns_actual_pressure():
    """
    Class CityReportProcess current weather processing function output
    must have actual pressure information
    """
    example_owm_report = example_owm_request("Tallinn", "weather")
    example_owm_report_pressure = example_owm_report['main']['pressure']

    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()

    assert test_weather_report_pr['pressure'] == example_owm_report_pressure


def test_processed_weather_report_returns_actual_date():
    """
    Class CityReportProcess current weather processing function output must have actual date
    """
    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()
    today = datetime.date.today().strftime("%d-%m-%Y")

    assert test_weather_report_pr['date'] == today


def test_processed_weather_report_variable_equal_to_weather_process_return():
    """
    Class CityReportProcess weather processing function output must be equal to filtered weather report variable
    """
    test_report_process = basic_report_process_for_test()
    test_weather_report_pr = test_report_process.process_current_weather()
    assert test_weather_report_pr == test_report_process.weather_ready_report


def test_processed_forecast_report_returns_list_of_dicts():
    """
    Class CityReportProcess forecast processing function output is list of three dictionaries
    """
    test_report_process = basic_report_process_for_test()
    test_forecast_report_pr = test_report_process.process_forecast()

    assert len(test_forecast_report_pr) == 3

    assert type(test_forecast_report_pr[0]) == dict
    assert type(test_forecast_report_pr[1]) == dict
    assert type(test_forecast_report_pr[2]) == dict


def test_processed_forecast_report_variable_equal_to_forecast_process_return():
    """
    Class CityReportProcess forecast processing function output must be equal to filtered forecast report variable
    """
    test_report_process = basic_report_process_for_test()
    test_forecast_report_pr = test_report_process.process_forecast()
    assert test_forecast_report_pr == test_report_process.forecast_ready_report


def test_processed_forecast_report_have_actual_dates():
    """
    Class CityReportProcess forecast processing function output have forecast for three next days
    """
    test_report_process = basic_report_process_for_test()
    test_forecast_report_pr = test_report_process.process_forecast()
    for n in range(0, 3):
        date = datetime.date.today() + datetime.timedelta(days=n + 1)
        assert test_forecast_report_pr[n]['date'] == date.strftime("%d-%m-%Y")


if __name__ == '__main__':
    pytest.main()
