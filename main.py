from hash_map import Map
from graph import Graph, Vertex
from package import Package
import csv


def load_package_data(data):
    """
    Loads package data into hash map and returns the hash map

    :param data: The csv file to parse package data from
    :return: A Map object representing package data with Package objects
    """

    # Initialize hash map to store package data
    packages = Map()

    # Read packages from csv
    with open(data) as package_file:
        reader = csv.reader(package_file, delimiter=',')
        for index, row in enumerate(reader):
            # Skip the column headers
            if index != 0:
                # Key: Package ID, Value: Package object
                packages.add(int(row[0]), Package(row[0], row[1], row[2], row[3], row[4], row[6], row[5], row[7]))

    return packages


def load_distance_data(data):

    # Initialize graph to store distance data
    distances = Graph()

    # Read distances from csv


package_data = load_package_data('data/Package File.csv')
