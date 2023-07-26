"""Tests output manager, where report is completely merged and generated json file"""
import pytest
import sys
sys.path.insert(0, "..")
from tests.common_calls_for_tests import *


def test_merged_report_func_output_exists():
    """
    Class ReportOutputManager function generate_merged_report() must merge the reports to one global report for city
    """
    test_output_mgr = basic_output_manager_for_test()
    merged_report = test_output_mgr.generate_merged_report()
    assert merged_report != {}


def test_merged_report_variable_exists():
    """
    Class ReportOutputManager function generate_merged_report() must save output in the class variable
    """
    test_output_mgr = basic_output_manager_for_test()
    test_output_mgr.generate_merged_report()
    assert test_output_mgr.merged_report != {}


def test_merged_report_variable_same_as_merge_func_output():
    """
    Class ReportOutputManager function generate_merged_report() output and merged report class variable must be same
    """
    test_output_mgr = basic_output_manager_for_test()
    merged_report = test_output_mgr.generate_merged_report()
    assert test_output_mgr.merged_report == merged_report


def test_merged_report_var_have_main_details_data():
    """
    Merged report dictionary must have a dictionary of main details information
    """
    test_output_mgr = basic_output_manager_for_test()
    test_output_mgr.generate_merged_report()
    test_output_mgr_main_d = test_output_mgr.merged_report['mainDetails']
    assert type(test_output_mgr_main_d) == dict
    assert len(test_output_mgr_main_d) > 0


def test_merged_report_var_have_current_weather_data():
    """
    Merged report dictionary must have a dictionary of current weather information
    """
    test_output_mgr = basic_output_manager_for_test()
    test_output_mgr.generate_merged_report()
    test_output_mgr_cr_weather = test_output_mgr.merged_report['currentWeatherReport']
    assert type(test_output_mgr_cr_weather) == dict
    assert len(test_output_mgr_cr_weather) > 0


def test_merged_report_var_have_forecast_data():
    """
    Merged report dictionary must have a list of forecast information for 3 days
    """
    test_output_mgr = basic_output_manager_for_test()
    test_output_mgr.generate_merged_report()
    test_output_mgr_cr_weather = test_output_mgr.merged_report['forecastReport']
    assert type(test_output_mgr_cr_weather) == list
    assert len(test_output_mgr_cr_weather) == 3


def test_create_json_report_func_returns_creates_specific_for_city_file():
    """
    Class ReportOutputManager function create_json_report() must use merged report
    and generate a file weather_report_for_some-city.json
    """
    t_city = "Tallinn"
    test_output_mgr = basic_output_manager_for_test(t_city)
    test_output_mgr.generate_merged_report()
    test_output_mgr.create_json_report()
    assert os.path.exists(f"../output/weather_report_for_{t_city.lower()}.json") is True


def test_json_report_file_is_same_as_merged_report():
    """
    weather_report_for_some-city.json must have same content as merged_report
    """
    t_city = "Tallinn"
    test_output_mgr = basic_output_manager_for_test(t_city)
    test_output_mgr.generate_merged_report()
    test_output_mgr.create_json_report()

    report_file = f"../output/weather_report_for_{t_city.lower()}.json"
    test_report = ""
    with open(report_file, "r") as r_file:
        for line in r_file:
            test_report += line
    test_report_in_dict = json.loads(test_report)

    assert test_output_mgr.merged_report == test_report_in_dict


if __name__ == '__main__':
    pytest.main()
