import datetime
import sys


class Truck:
    """This class represents a Truck which holds and delivers Package objects"""

    def __init__(self, id, package_data, distance_graph):
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
        for package in package_arr:
            if package.notes == 'Wrong address listed':
                if self.current_time > datetime.timedelta(hours=10, minutes=20):
                    package.notes = ''
                    package.address = '410 S State St'
                    package.zip = '84111'
                    print('Package #', package.id, 'Address Updated @', self.current_time)
                else:
                    return False
        return True

    def load_truck(self, time_loaded):
        self.current_time = time_loaded

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
                    return False
        return True

    def find_next_delivery(self):
        min_distance = sys.maxsize
        for address in self.distance_data.adjacency_list[self.current_location]:
            distance = float(self.distance_data.distances[(address, self.current_location)])
            if distance < min_distance and address in self.on_board and self.has_correct_address(self.on_board[address]):
                min_distance = float(self.distance_data.distances[(self.current_location, address)])
                next_address = address

        time_took = min_distance / 18 * 3600
        self.deliver_package(next_address, min_distance, time_took)

    def deliver_package(self, address, distance_traveled, time_took):
        self.current_location = address
        self.distance_traveled += distance_traveled
        self.current_time += datetime.timedelta(seconds=time_took)
        while len(self.on_board[address]) > 0:
            print(self.on_board[address][-1].deadline, self.current_time)
            self.on_board[address][-1].time_delivered = self.current_time
            self.on_board[address].pop()
        del self.on_board[address]

    def deliver_packages(self):
        self.departure_time = self.current_time
        while len(self.on_board) > 0:
            self.find_next_delivery()

        # Go back to HUB
        self.return_to_hub()

    def return_to_hub(self):
        distance = float(self.distance_data.distances[(self.current_location, 'HUB')])
        self.current_time += datetime.timedelta(distance / 18 / 3600)
        self.distance_traveled += distance
        self.return_time = self.current_time
        self.current_location = 'HUB'

