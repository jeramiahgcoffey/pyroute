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
    with open(data, 'r') as package_file:
        reader = csv.reader(package_file, delimiter=',')
        for index, row in enumerate(reader):
            # Skip the column headers
            if index != 0:
                # Key: Package ID, Value: Package object
                packages.add(int(row[0]), Package(row[0], row[1], row[2], row[3], row[4], row[6], row[5], row[7]))

    return packages


def load_address_data(data):
    # Initialize dictionary to store vertices
    addresses = {}

    with open(data, 'r') as distance_file:
        reader = csv.DictReader(distance_file)
        row_1 = next(reader)
        for j, location in enumerate(row_1):
            if j != 0:
                addresses[location] = Vertex(location)
                # distances.add_vertex(vertices[hub])

    return addresses


def load_distance_data(data, addresses):
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
                        # The current row's hub
                        vertex_a = addresses[row[col]]
                    else:
                        # The current columns hub
                        vertex_b = addresses[col]
                        # Adds the distance between the two hubs as an edge
                        distances.add_edge(vertex_a, vertex_b, row[col])

        return distances


package_data = load_package_data('data/Package File.csv')
address_data = load_address_data('data/Distance Table reformatted.csv')
distance_data = load_distance_data('data/Distance Table reformatted.csv', address_data)
