from datetime import timedelta
from prettytable import PrettyTable

from utilities.csv_reader import *
from utilities.pretty_time import pretty_time
from data_structures.truck import Truck


class Controller:
    """UI and delivery controller. Contains methods to be called from the main loop."""

    def __init__(self):
        """Initialize Controller object"""

        # Read package data file and return a hash map with Package ID as keys and Package objects as values
        self.package_data = load_package_data('data/Package File.csv')

        # Read distance data file and return a Graph object with addresses as vertices and distances as edges
        self.distance_graph = load_distance_data('data/distances.csv', load_address_data('data/distances.csv'))

        # Dictionary for storing Truck objects
        self.trucks = {}

    def start_day(self):
        """
        Initializes Truck objects and adds them to the self.trucks dictionary with their IDs as keys.
        Load Trucks with Packages from self.package_data.
        Starts each Truck's route.
        """

        # Create truck objects, passing in departure time, the ID, package data and distance graph
        self.trucks[1] = Truck(1, self.package_data, self.distance_graph)
        self.trucks[2] = Truck(2, self.package_data, self.distance_graph)
        self.trucks[3] = Truck(3, self.package_data, self.distance_graph)

        # Load Truck 1 at 8:00am
        self.trucks[1].load_truck(timedelta(seconds=28800))

        # Load Truck 2 at 9:05am
        self.trucks[2].load_truck(timedelta(seconds=32700))

        # Start Truck 1 route
        self.trucks[1].deliver_packages()

        # Start Truck 2 route
        self.trucks[2].deliver_packages()

        # Load Truck 3 when Truck 1 returns to HUB
        self.trucks[3].load_truck(self.trucks[1].return_time)

        # Start Truck 3 route
        self.trucks[3].deliver_packages()

    def print_package(self, id):
        """
        Print Package data.

        :param id: Integer. Package ID.
        """

        # Get Package object from the package_data hash map by ID.
        package = self.package_data.get(id)
        print(f'ID:             {package.id}\n'
              f'Address:        {package.address}, {package.city}, {package.state} {package.zip}\n'
              f'Mass(Kilo):     {package.mass}\n'
              f'Deadline:       {package.deadline}\n'
              f'Truck ID:       {package.truck}\n'
              f'Time Loaded:    {pretty_time(package.time_loaded)}\n'
              f'Time Delivered: {pretty_time(package.time_delivered)}',
              f'\nNotes:          {package.notes}' if package.notes != '' else '')

    def print_truck(self, id):
        """
        Print Truck data.

        :param id: Integer. Truck ID.
        """

        # Get Truck object from the self.trucks dictionary
        truck = self.trucks[id]
        print(f'ID: {truck.id}\n'
              f'Capacity:          {truck.capacity}\n'
              f'Departure Time:    {pretty_time(truck.departure_time)}\n'
              f'Return Time:       {pretty_time(truck.return_time)}\n'
              f'Distance Traveled: {truck.distance_traveled} miles')

    def print_all_statuses(self, timestamp='9:00'):
        """
        Print all Package statuses at the given time.

        :param timestamp: String. 24-hour timestamp. HH:MM
        """

        # Create timedelta object from timestamp parameter
        hour = int(timestamp.split(':')[0])
        minute = int(timestamp.split(':')[1])
        time = timedelta(hours=hour, minutes=minute)

        # Create table to display Package data
        table = PrettyTable()
        table.field_names = ['ID', 'TRUCK ID', 'STATUS', 'ADDRESS', 'DEADLINE', 'TIME DELIVERED']

        print(f'\n------------------------------------------------ PACKAGE STATUSES AS OF {pretty_time(time)} '
              f'------------------------------------------------')

        # Loop through every bucket in self.package_data hash map and add each Package as a row in the table
        for bucket in self.package_data.map:
            if bucket is not None:
                for pair in bucket:
                    package = pair[1]
                    address = f'{package.address}, {package.city}, {package.state} {package.zip}'
                    time_delivered = None
                    if package.time_loaded is None:
                        status = 'AT HUB'
                    elif package.time_delivered is None:
                        status = 'EN ROUTE'
                    elif time >= package.time_delivered:
                        status = 'DELIVERED'
                        time_delivered = pretty_time(package.time_delivered)
                    elif time >= package.time_loaded:
                        status = 'EN ROUTE'
                    else:
                        status = 'AT HUB'

                    table.add_row([package.id,
                                   package.truck,
                                   status,
                                   address,
                                   package.deadline,
                                   time_delivered])

        print(table)

    def print_total_distance(self):
        """Print total distance traveled between all Trucks in self.trucks dictionary."""

        total_distance = 0
        # Loop through self.trucks dictionary and add distance_traveled to the total_distance
        for truck in self.trucks:
            truck = self.trucks[truck]
            if truck.return_time is None:
                print(f'TRUCK {truck.id} HAS NOT RETURNED')
                return
            total_distance += truck.distance_traveled

        print(f'TOTAL DISTANCE TRAVELED: {round(total_distance)} MILES')

    def print_total_time(self):
        """Print the duration from when the first Truck left the HUB to when the last Truck returned to the HUB"""

        earliest = None
        latest = None
        # Loop through self.trucks dictionary
        for truck in self.trucks:
            truck = self.trucks[truck]

            # Assign the earliest Truck based on departure_time
            if earliest is None:
                earliest = truck
            elif truck.departure_time < earliest.departure_time:
                earliest = truck

            # Assign the latest Truck based on return_time
            if latest is None:
                latest = truck
            elif truck.return_time > latest.return_time:
                latest = truck

        # The difference between latest and earliest in hours
        total = round((latest.return_time - earliest.departure_time).total_seconds() / 3600, 2)

        print(f'TOTAL TIME TAKEN: {total} HOURS')
