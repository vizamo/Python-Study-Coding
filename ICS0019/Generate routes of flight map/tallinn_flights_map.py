import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib import pyplot as plt
import pandas as pd


def create_europe_map():
    """
    Create a europe landscape map
    """
    proj = ccrs.Miller()
    bg_map = plt.subplot(1, 1, 1, projection=proj)
    bg_map.set_extent([-23, 52, 18, 65])  # east west south north
    bg_map.stock_img()
    bg_map.add_feature(cf.COASTLINE, lw=2)
    bg_map.add_feature(cf.BORDERS)
    # Make figure larger
    plt.gcf().set_size_inches(20, 10)

    bg_map.set_title('Flights from Tallinn \n '
                     'Author: Vitali Zamorski \n')

    print("Europe map is created successfully")

    return bg_map


def add_flight_points(bg_map, lon, lat, color, size=90):
    """
    Add airports points where is ended direct flights from Tallinn
    :param bg_map: a map background for points to place
    :param lon: Longitude, first coordinate
    :param lat: Latitude, second coordinate
    :param color: Color of a flight point
    :param size: Size of a flight point
    """
    bg_map.scatter(lon, lat, s=size, c=color, edgecolor='black', alpha=0.75, transform=ccrs.PlateCarree())
    print("Flight points is added successfully")


def add_flight_points_names(bg_map, cities, lon, lat, control_list):
    """
    Add to airports points names of connected cities
    :param bg_map: a map background for points to place
    :param cities: Name of city
    :param lon: Longitude, first coordinate
    :param lat: Latitude, second coordinate
    :param control_list: List for excluding repeating values
    """
    for i, city in enumerate(cities):
        if city not in control_list:
            bg_map.text(lon.values[i], lat.values[i], city,
                        horizontalalignment='right',
                        transform=ccrs.PlateCarree(),
                        fontsize=8,
                        weight='bold',
                        )
    print("Flight points names is added successfully")


def add_flight_routes_from_tallinn(cities, lon, lat, color):
    """
    Creates a colored curve routes from Tallinn to fight points
    Coordinates of Tallinn is 24.8327999115 59.41329956049999
    :param cities: Name of city is used only for enumeration
    :param lon: Longitude, first coordinate
    :param lat: Latitude, second coordinate
    :param color: Color of a route
    """
    for i, _ in enumerate(cities):
        plt.plot([24.8327999115, lon.values[i]],
                 [59.41329956049999, lat.values[i]],
                 color=color,
                 transform=ccrs.Geodetic())
    print("Routes is added successfully")


def import_airports_locations(filename):
    """
    Import airports location from OpenFlights Airports Database
    :param filename: csv file, contains airports locations
    :return: pandas DataFrame which contains
    city, IATA and coordinates of every airport
    """
    airports = pd.read_csv(
        filename, sep=",",
        usecols=["City", "Latitude", "Longitude", "IATA"])
    return airports


def import_flights_points(filename):
    """
    Import IATA, where from was direct flight from Tallinn
    :param filename: csv file, contains Cities with IATA codes
    :return: list of IATA airports codes
    """
    direct_flights = pd.read_csv(filename,
                                 sep=";",
                                 usecols=["IATA"])
    direct_flights_list = sum(direct_flights.values.tolist(), [])
    return direct_flights_list


def filter_airports(airports_df, list_of_iata):
    """
    Filter all airports only for selected airports
    :param airports_df: pandas DataFrame
    with airports names and coordinates
    :param list_of_iata: list of IATA codes,
    which indicated airports for search
    :return: filtered pandas DataFrame
    """
    filtered_airports = airports_df.query(f'IATA in {list_of_iata}')
    return filtered_airports


if __name__ == "__main__":
    # Import direct flights locations
    pre_covid_iata = import_flights_points("pre-covid-flight.csv")
    after_covid_iata = import_flights_points("after-covid-flight.csv")

    # Import world airopts coordinates
    all_airopts_locations = import_airports_locations("airports.dat")

    # Filter for only required airports coordinates
    pre_covid_airports = filter_airports(all_airopts_locations, pre_covid_iata)
    after_covid_airports = filter_airports(all_airopts_locations, after_covid_iata)

    pre_covid_city = pre_covid_airports.City
    pre_covid_lon = pre_covid_airports.Longitude
    pre_covid_lat = pre_covid_airports.Latitude

    after_covid_city = after_covid_airports.City
    after_covid_lon = after_covid_airports.Longitude
    after_covid_lat = after_covid_airports.Latitude

    # Create a Europe landscape background for flights points
    euro_map = create_europe_map()

    # Add flight points to the Europe map
    add_flight_points(euro_map, pre_covid_lon, pre_covid_lat, 'r')
    add_flight_points(euro_map, after_covid_lon, after_covid_lat, 'b')

    # Add flight points names to the Europe map
    pre_covid_city_list = pre_covid_city.values.tolist()
    add_flight_points_names(euro_map, pre_covid_city, pre_covid_lon, pre_covid_lat, [])
    add_flight_points_names(euro_map, after_covid_city, after_covid_lon, after_covid_lat, pre_covid_city_list)

    # Add routes from Tallin to selected airports
    add_flight_routes_from_tallinn(pre_covid_city, pre_covid_lon, pre_covid_lat, 'r')
    add_flight_routes_from_tallinn(after_covid_city, after_covid_lon, after_covid_lat, 'b')

    plt.savefig("tallinn_flights_map.jpg")
    plt.show()
