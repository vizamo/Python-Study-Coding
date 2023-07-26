"""Tests complete weather app with generation of full report and output into file"""
import pytest
import sys
sys.path.insert(0, "..")
from tests.common_calls_for_tests import *


def test_generate_report_from_file_creates_a_output_file_for_one_city():
    """
    Function generate_report_from_file() must read the input file,
    generate and process report and put it into output file
    """
    example_city = ["Narva"]
    create_sample_file(1, example_cities=example_city)
    generate_report_from_file()
    assert os.path.exists(f"../output/weather_report_for_{example_city[0].lower()}.json") is True


def test_generate_report_from_file_creates_nothing_for_not_existing_city():
    """
       Function generate_report_from_file() must read the input file,
       and if it have not existing city - ignore it
       """
    example_city = ["Tallinakl"]
    create_sample_file(1, example_cities=example_city)
    generate_report_from_file()
    assert os.path.exists(f"../output/weather_report_for_{example_city[0].lower()}.json") is False


def test_generate_report_from_file_creates_a_output_file_for_list_of_cities():
    """
    Function generate_report_from_file() must read every city in the input file,
    generate and process reports and put them into output file
    """
    example_city = ["Oslo", "London", "New York", "Prague", "Paris"]
    create_sample_file(5, example_cities=example_city)

    generate_report_from_file()

    for t_city in example_city:
        assert os.path.exists(f"../output/weather_report_for_{t_city.lower()}.json") is True


def test_generate_report_from_file_creates_a_output_file_for_list_of_cities_and_ignore_not_existing():
    """
    Function generate_report_from_file() must read every city in the input file,
    generate and process reports and put them into output file
    If city in the list of cities does not exist - drop it
    """
    example_city = ["Seoul", "Bangkok", "Dubai", "Harry Potter", "Istanbul", "Tokyo", "TalTech",
                    "New Bagabung", "Singapore"]
    create_sample_file(9, example_cities=example_city)

    generate_report_from_file()

    must_process = ["Seoul", "Bangkok", "Dubai", "Istanbul", "Tokyo", "Singapore"]
    must_drop = ["Harry Potter", "TalTech", "New Bagabung"]
    for pro_city in must_process:
        assert os.path.exists(f"../output/weather_report_for_{pro_city.lower()}.json") is True
    for dro_city in must_drop:
        assert os.path.exists(f"../output/weather_report_for_{dro_city.lower()}.json") is False


def test_generate_report_from_not_default_file_creates_a_output_file_for_list_of_cities_and_ignore_not_existing():
    """
    Function generate_report_from_file() must read every city in the input file,
    generate and process reports and put them into output file
    If city in the list of cities does not exist - drop it
    Must read the cities filename in the parameter
    """
    example_city = ["Osaka", "Moscow", "Phuket", "Gogogonia", "Milan", "Barcelona", "Piaterochka",
                    "Shmoston", "Bali"]
    create_sample_file(9, "../app/test_cities.txt", example_city)

    generate_report_from_file("../app/test_cities.txt")

    must_process = ["Osaka", "Moscow", "Phuket", "Milan", "Barcelona", "Bali"]
    must_drop = ["Gogogonia", "Piaterochka", "Shmoston"]
    for pro_city in must_process:
        assert os.path.exists(f"../output/weather_report_for_{pro_city.lower()}.json") is True
    for dro_city in must_drop:
        assert os.path.exists(f"../output/weather_report_for_{dro_city.lower()}.json") is False


if __name__ == '__main__':
    pytest.main()
