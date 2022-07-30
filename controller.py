from datetime import timedelta
from prettytable import PrettyTable

from utilities.csv_reader import *
from utilities.pretty_time import pretty_time
from data_structures.truck import Truck


class Controller:
    def __init__(self):
        # Read package data file and return a hash map with Package ID as keys and Package objects as values
        self.package_data = load_package_data('data/Package File.csv')

        # Read distance data file and return a Graph object with addresses as vertices and distances as edges
        self.distance_graph = load_distance_data('data/distances.csv', load_address_data('data/distances.csv'))

        self.trucks = {}

    def start_day(self):
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

        # Load Truck 3 when Truck 1 returns to HUB
        self.trucks[3].load_truck(self.trucks[1].return_time)

        # Start Truck 2 and 3 routes
        self.trucks[2].deliver_packages()
        self.trucks[3].deliver_packages()

    def print_package(self, id):
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
        truck = self.trucks[id]
        print(f'ID: {truck.id}\n'
              f'Capacity:          {truck.capacity}\n'
              f'Departure Time:    {pretty_time(truck.departure_time)}\n'
              f'Return Time:       {pretty_time(truck.return_time)}\n'
              f'Distance Traveled: {truck.distance_traveled} miles')

    def print_all_statuses(self, timestamp='9:00'):
        hour = int(timestamp.split(':')[0])
        minute = int(timestamp.split(':')[1])
        time = timedelta(hours=hour, minutes=minute)

        table = PrettyTable()
        table.field_names = ['ID', 'TRUCK ID', 'STATUS', 'ADDRESS', 'DEADLINE', 'TIME DELIVERED']

        print(f'\n------------------------------------------------ PACKAGE STATUSES AS OF {pretty_time(time)} '
              f'------------------------------------------------')
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
        total_distance = 0
        for truck in self.trucks:
            truck = self.trucks[truck]
            if truck.return_time is None:
                print(f'TRUCK {truck.id} HAS NOT RETURNED')
                return
            total_distance += truck.distance_traveled

        print(f'TOTAL DISTANCE TRAVELED: {round(total_distance)} MILES')

    def print_total_time(self):
        earliest = None
        latest = None
        for truck in self.trucks:
            truck = self.trucks[truck]
            if earliest is None:
                earliest = truck
            elif truck.departure_time < earliest.departure_time:
                earliest = truck

            if latest is None:
                latest = truck
            elif truck.return_time > latest.return_time:
                latest = truck

        total = round((latest.return_time - earliest.departure_time).total_seconds() / 3600, 2)

        print(f'TOTAL TIME TAKEN: {total} HOURS')
