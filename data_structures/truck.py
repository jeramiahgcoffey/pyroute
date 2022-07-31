from datetime import timedelta
import sys

from utilities.pretty_time import pretty_time


class Truck:
    """Stores Package objects and distance Graph. Deliver Packages. Track time and distance."""

    def __init__(self, id, package_data, distance_graph):
        """
        Initialize Truck object.

        :param id: Integer. The Truck ID.
        :param package_data: Map. Hash map of package data.
        :param distance_graph: Graph. Graph of addresses and distance data.
        """

        self.capacity = 16
        self.current_location = 'HUB'
        self.current_time = None
        self.departure_time = None
        self.distance_data = distance_graph
        self.distance_traveled = 0
        self.id = id
        self.on_board = {}
        self.package_data = package_data
        self.return_time = None

    def has_correct_address(self, package_arr):
        """
        Check if Packages in an array have a note warning of an incorrect listed address.
        Update address if incorrect and a time constraint is met.

        :param package_arr: List. Array of packages to check.
        :return: Boolean. False if no warning or address was updated. True otherwise.
        """

        for package in package_arr:
            if package.notes == 'Wrong address listed':
                if self.current_time > timedelta(hours=10, minutes=20):
                    # Ask user if the address should be updated
                    should_update = input(f'\nThe time is {pretty_time(self.current_time)}.\n'
                                          f'Would you like to update the address for Package #{package.id}'
                                          f' to 410 S State St., Salt Lake City, UT 84111?\nY/N: ').lower()
                    if should_update != 'n':
                        package.notes = f'Address updated at {pretty_time(self.current_time)}'
                        package.address = '410 S State St'
                        package.zip = '84111'
                        print(f'\nPackage #{package.id} address updated at {pretty_time(self.current_time)}.')
                else:
                    return False
        return True

    def load_truck(self, timestamp):
        """
        Add respective Package objects to self.on_board, based on Package's truck attribute.

        :param timestamp: Timedelta. The time the truck is loaded at.
        """

        self.current_time = timestamp

        for i in range(1, self.package_data.count + 1):
            package = self.package_data.get(i)
            if package.truck == self.id:
                if len(self.on_board) < self.capacity:
                    package.time_loaded = self.current_time
                    if package.address not in self.on_board:
                        self.on_board[package.address] = [package]
                    else:
                        self.on_board[package.address].append(package)
                else:
                    print('PACKAGE LOADING ERROR')

    def find_next_delivery(self):
        """
        Nearest Neighbor Algorithm implementation.
        Find next closest delivery address.
        Calls deliver_package with the next closest address.
        """

        min_distance = sys.maxsize
        for address in self.distance_data.adjacency_list[self.current_location]:
            distance = float(self.distance_data.distances[(address, self.current_location)])
            if distance < min_distance and address in self.on_board and \
                    self.has_correct_address(self.on_board[address]):
                min_distance = float(self.distance_data.distances[(self.current_location, address)])
                next_address = address

        time_took = min_distance / 18 * 3600

        # Call self.deliver_package with the next closest address
        self.deliver_package(next_address, min_distance, time_took)

    def deliver_package(self, address, distance_traveled, time_took):
        """
        Deliver Packages associated with the address passed in.

        :param address: String. Address which Packages are associated with.
        :param distance_traveled: Float. Miles traveled to get to this address.
        :param time_took: Float. Seconds taken to travel to address.
        """

        self.current_location = address
        self.distance_traveled += distance_traveled
        self.current_time += timedelta(seconds=time_took)
        while len(self.on_board[address]) > 0:
            self.on_board[address][-1].time_delivered = self.current_time
            self.on_board[address].pop()
        del self.on_board[address]

    def deliver_packages(self):
        """Start loop to deliver all Package objects. Calls return_to_hub when self.on_board has no more Packages"""

        self.departure_time = self.current_time
        while len(self.on_board) > 0:
            self.find_next_delivery()

        # Go back to HUB
        self.return_to_hub()

    def return_to_hub(self):
        """Return to HUB after all deliveries."""

        distance = float(self.distance_data.distances[(self.current_location, 'HUB')])
        self.current_time += timedelta(distance / 18 / 3600)
        self.distance_traveled += distance
        self.return_time = self.current_time
        self.current_location = 'HUB'
