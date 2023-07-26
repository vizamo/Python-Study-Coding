"""Parse and process input file. Generate a list of cities for report creation"""
from app.logging_and_error_handler import *
import re


class OWMFileManagement:
    """Read and process input files with city names"""

    def __init__(self, filename: str = "../app/cities_for_owm.txt"):
        """
        :param filename: Name of input cities file where stored cities names for weather report
        """
        self.filename = filename
        self.owm_cities = []

        self.validate_cities_file_extension()

    def process_cities_file(self):
        """."""
        cities = []
        with open(self.filename, "r") as city_file:
            for city in city_file:
                city = city.strip()
                city_class = City(city)
                if city not in cities:
                    self.owm_cities.append(city_class)
                    cities.append(city)
        logging(3, "File is processed without errors")
        return self.owm_cities

    def validate_cities_file_extension(self):
        """
        Validate that cities file is in .txt format
        and have some at least one letter filename
        """
        not_only_extension = len(self.filename)
        if re.search("\\.txt$", self.filename) is not None \
                and not_only_extension > 4:
            logging(3, "File extension is validated and correct")
            return True
        raise NotSupportedExtensionError()


class City:
    """Define, keep data of the one city"""

    def __init__(self, city: str):
        """
        :param city: Name of the city for which will be created a weather report
        """
        self.city = city
        self.is_exist = None

    def __repr__(self):
        """String representation of the city is the city name"""
        return self.city
