"""Application for providing output of weather reports for customer"""
from app.owm_parser import *
import json
import os


class ReportOutputManager:
    """Process created full report for filtering and formatting variables until required condition"""

    def __init__(self, processed_report: CityReportProcess):
        """
        :param processed_report: CityReportProcess class, where is saved a processed reports
        """
        self.pr_reports = processed_report
        self.merged_report = {}

    def generate_merged_report(self):
        """
        Merge main details, current weather, forecast reports into one complete report
        And add it to class variable
        :return: merged ready report
        """
        main_details_report = {"mainDetails": self.pr_reports.main_details_ready_report}
        current_weather_report = {"currentWeatherReport": self.pr_reports.weather_ready_report}
        forecast_report = {"forecastReport": self.pr_reports.forecast_ready_report}

        ready_report = {}
        ready_report.update(main_details_report)
        ready_report.update(current_weather_report)
        ready_report.update(forecast_report)

        logging(3, f"Report for city {self.pr_reports.report.city} is ready")
        self.merged_report = ready_report
        return ready_report

    def create_json_report(self):
        """
        Write an output file with city name in it and json format and with pretty line ident
        :return: report formatted in json
        """
        city = self.merged_report['mainDetails']['city']
        report_in_json = json.dumps(self.merged_report, indent=2)
        output_file = f"../output/weather_report_for_{city.lower()}.json"
        if os.path.exists(output_file) is True:
            logging(3, f"{output_file} file will be overwritten")
        with open(output_file, 'w') as json_output_file:
            json_output_file.write(report_in_json)
        logging(3, f"Report for city {city} is sent to the {output_file}")
        return report_in_json


def generate_report_from_file(input_filename: str = "../app/cities_for_owm.txt", print_final: str = "yes"):
    """
    Function to provide app functionality
    Reads input file, generates and processes reports and writes them to the output files
    If city does not exist - ignores it
    :param print_final: If True - print output not only into files, but also in stdout
    :param input_filename: name of the file, where from must be taken city names
    :return: list of the generated reports
    """
    input_manager = OWMFileManagement(input_filename)
    cities_list = input_manager.process_cities_file()
    cities_output = []
    for city in cities_list:
        city_report = CityReport(city)
        if city.is_exist is True:
            city_report_processed = CityReportProcess(city_report)
            city_output = ReportOutputManager(city_report_processed)
            final_report = city_output.generate_merged_report()
            city_output.create_json_report()
            cities_output.append(final_report)
        else:
            logging(2, f"City {city.__repr__()} is dropped from generation")
    logging(3, "Output generation is finished. Check application output directory")
    if print_final.lower() == "yes" or print_final.lower() == "y":
        print(json.dumps(cities_output, indent=2))
    return cities_output


if __name__ == '__main__':
    # Application running from cmd line
    print("Enter path and filename to the file of the cities for the report")
    print("If you wish to use default cities_for_owm.txt - press enter")
    customer_filename = input("File: ")
    print("Do you want to see report in stdout?")
    print("If you wish to use default - press enter")
    print_to_stdout = input("Y(es)/N(o): ")

    if print_to_stdout == "":
        print_to_stdout = "y"
    if customer_filename == "":
        customer_filename = "../app/cities_for_owm.txt"

    generate_report_from_file(customer_filename, print_to_stdout)
    print("Job is done. Bye. Bye.")
