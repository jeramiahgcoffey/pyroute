from hash_map import Map
from graph import Graph, Vertex
from package import Package
from truck import Truck
import csv


def load_package_data(data):
    """
    Loads package data into hash map and returns it

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
                packages.add(
                    int(row[0]),
                    Package(row[0], row[1], row[2], row[3], row[4], row[6], row[8], row[5], row[7])
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
                print(location)
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
                        # The current row's hub
                        vertex_a = addresses[row[col]]
                    else:
                        # The current columns hub
                        vertex_b = addresses[col]
                        # Adds the distance between the two hubs as an edge
                        distances.add_edge(vertex_a, vertex_b, row[col])

        return distances


def add_packages(truck_a, truck_b, truck_c):
    for i in range(1, 41):
        package = package_data.get(i)
        truck_number = int(package.truck)
        if truck_number == 1:
            truck_a.add(package)
        elif truck_number == 2:
            truck_b.add(package)
        else:
            truck_c.add(package)


package_data = load_package_data('data/Package File.csv')
address_data = load_address_data('data/Distance Table reformatted.csv')
distance_data = load_distance_data('data/Distance Table reformatted.csv', address_data)

truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()

add_packages(truck_1, truck_2, truck_3)
