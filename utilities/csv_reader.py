import csv

from data_structures.hash_map import Map
from data_structures.package import Package
from data_structures.graph import Vertex, Graph


def load_package_data(data):
    """
    Loads package data into hash map and returns it

    :param data: The csv file to parse package data from
    :return: A Map object representing package data as Package objects
    """

    # Initialize hash map to store package data
    packages = Map()

    # Read packages from csv
    with open(data, 'r') as package_file:
        reader = csv.reader(package_file, delimiter=',')
        for index, row in enumerate(reader):
            # Skip the column headers
            if index != 0:
                # Key: Package ID, Value: Package object
                packages.add(
                    int(row[0]),
                    Package(int(row[0]), row[1], row[2], row[3], row[4], row[6], int(row[8]), row[5], row[7])
                )

    return packages


def load_address_data(data):
    """
    Loads address data into a dictionary and returns it

    :param data: The csv file to parse address data from
    :return: A dictionary with addresses as keys and Vertex objects representing the addresses as values
    """

    # Initialize dictionary to store vertices
    addresses = {}

    with open(data, 'r') as distance_file:
        reader = csv.DictReader(distance_file)
        row_1 = next(reader)
        for j, location in enumerate(row_1):
            if j != 0:
                addresses[location] = Vertex(location)

    return addresses


def load_distance_data(data, addresses):
    """
    Loads distance data into a Graph and returns it

    :param data: The csv file to parse distance data from
    :param addresses: A dictionary of addresses returned from load_address_data()
    :return: A Graph object with addresses as Vertices and distances as edges
    """

    # Initialize Graph to store distance data
    distances = Graph()

    # Add address Vertex objects to Graph
    for address in addresses:
        vertex = addresses[address]
        distances.add_vertex(vertex)

    # Read distances from csv
    with open(data, 'r') as distance_file:
        reader = csv.DictReader(distance_file)
        for i, row in enumerate(reader):
            # Skip column headers
            if i != 0:
                for j, col in enumerate(row):
                    if j == 0:
                        # The current row's location
                        vertex_a = addresses[row[col]]
                    else:
                        # The current columns location
                        vertex_b = addresses[col]
                        # Adds the distance between the two hubs as an edge
                        distances.add_edge(vertex_a, vertex_b, row[col])

        return distances
