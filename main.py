from hash_map import Map
from package import Package
import csv


def load_package_data():
    """Loads package data into hash map and returns the hash map"""

    # Initialize hash map to store package data
    packages = Map()

    # Read packages from csv
    with open('Package File.csv') as package_file:
        reader = csv.reader(package_file, delimiter=',')
        for index, row in enumerate(reader):
            # Skip the column headers
            if index != 0:
                # Key: Package ID, Value: Package object
                packages.add(int(row[0]), Package(row[0], row[1], row[2], row[3], row[4], row[6], row[5], row[7]))

    return packages


package_data = load_package_data()
