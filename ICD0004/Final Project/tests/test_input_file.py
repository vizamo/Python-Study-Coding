"""Tests for input file reading, processing and returning of cities class"""
import pytest
import sys
sys.path.insert(0, "..")
from tests.common_calls_for_tests import *


def test_input_file_reading_function_returns_list_of_cities_classes():
    """
    process_cities_file() must return a list of City classes for each city in the list
    """
    create_sample_file(1)
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    assert type(test_cities) == list


def test_input_file_reading_function_return_same_count_that_got():
    """
    process_cities_file() must give same count of cities, what is provided in input file
    """
    create_sample_file(5)
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    assert len(test_cities) == 5


def test_input_file_reading_function_empty_file_empty_list():
    """
    process_cities_file() must give same count of cities, what is provided in input file
    """
    create_sample_file(1, example_cities=[""])
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    assert test_cities == []


def test_input_file_reading_function_return_right_cities():
    """
    process_cities_file() must create classes for same cities, what is present in the file
    """
    create_sample_file(5, example_cities=["Tallinn", "Lissabon", "Guata Mala", "Tallinn", "Moscow"])
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    x = 0
    assert len(test_cities) == 4
    output_cities = ["Tallinn", "Lissabon", "Guata Mala", "Moscow"]
    for t_city in test_cities:
        assert t_city.__repr__() == output_cities[x]
        x += 1


def test_input_file_reading_function_with_double_cities_return_without_doubles():
    """
    process_cities_file() must drop a duplicated cities names from the input file
    """
    create_sample_file(5, example_cities=["Tallinn", "Tallinn", "New York", "Prague",
                                          "Prague", "Brussels", "Amsterdam"])
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    assert len(test_cities) == 3


def test_input_file_reading_function_changes_class_variable_to_cities_classes_list():
    """
    process_cities_file() must write a class variable where is kept cities classes
    """
    create_sample_file(1)
    process_cities = OWMFileManagement()
    test_cities = process_cities.process_cities_file()
    assert process_cities.owm_cities == test_cities


def test_input_file_reading_function_when_file_is_missing_raise_error():
    """
    process_cities_file() must raise an FileNotFound error, if there is not found given input file
    """
    sample_filename = "owm_parserqqwert.txt"
    with pytest.raises(FileNotFoundError):
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()


def test_input_file_reading_function_not_process_csv():
    """
    process_cities_file() must process only .txt format, not .csv
    """
    sample_filename = "owm_parser.csv"
    create_sample_file(1, sample_filename)
    with pytest.raises(NotSupportedExtensionError) as exc:
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()
    assert "Wrong file extension. Input file must have .txt extension." in str(exc.value)


def test_input_file_reading_function_not_process_json():
    """
    process_cities_file() must process only .txt format, not .json
    """
    sample_filename = "owm_parser.json"
    create_sample_file(1, sample_filename)
    with pytest.raises(NotSupportedExtensionError) as exc:
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()
    assert "Wrong file extension. Input file must have .txt extension." in str(exc.value)


def test_input_file_reading_function_not_process_docx():
    """
    process_cities_file() must process only .txt format, not .docx
    """
    sample_filename = "owm_parser.docx"
    create_sample_file(1, sample_filename)
    with pytest.raises(NotSupportedExtensionError) as exc:
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()
    assert "Wrong file extension. Input file must have .txt extension." in str(exc.value)


def test_input_file_reading_function_not_process_pdf():
    """
    process_cities_file() must process only .txt format, not .pdf
    """
    sample_filename = "owm_parser.pdf"
    create_sample_file(1, sample_filename)
    with pytest.raises(NotSupportedExtensionError) as exc:
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()
    assert "Wrong file extension. Input file must have .txt extension." in str(exc.value)


def test_input_file_reading_function_not_process_file_without_extension():
    """
    process_cities_file() must process only .txt format, not files without extension
    """
    sample_filename = "owm_parser"
    create_sample_file(1, sample_filename)
    with pytest.raises(NotSupportedExtensionError) as exc:
        process_cities = OWMFileManagement(f"../app/{sample_filename}")
        process_cities.process_cities_file()
    assert "Wrong file extension. Input file must have .txt extension." in str(exc.value)


def test_city_class_have_city_name_attribute():
    """
    City class must have corresponding city name attribute
    """
    test_city = City("Tallinn")
    assert test_city.city == "Tallinn"


def test_city_class_have_city_name_representation():
    """
    City class must have representation function corresponding with city name attribute
    """
    test_city = City("Tallinn")
    assert test_city.__repr__() == "Tallinn"


if __name__ == '__main__':
    pytest.main()
