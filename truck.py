import sys


class Truck:
    """This class represents a Truck which holds and delivers Package objects"""

    def __init__(self, id, package_data, distance_data):
        self.capacity = 16
        self.current_location = 'HUB'
        self.distance_data = distance_data
        self.id = id
        self.on_board = {}
        self.package_data = package_data

    def load_truck(self):
        for i in range(1, self.package_data.count + 1):
            package = self.package_data.get(i)
            if package.truck == self.id:
                if len(self.on_board) < self.capacity:
                    package.status = "ON TRUCK"
                    self.on_board[package.address] = package
                else:
                    print('PACKAGE LOADING ERROR')
                    return False
        return True

    def find_next_delivery(self):
        min_distance = sys.maxsize
        for address in self.distance_data.adjacency_list[self.current_location]:
            if float(self.distance_data.distances[(address, self.current_location)]) < min_distance \
                    and address in self.on_board:
                min_distance = float(self.distance_data.distances[(self.current_location, address)])
                self.deliver_package(address)

    def deliver_package(self, address):
        if address in self.on_board:
            self.current_location = address
            self.on_board[address].status = "DELIVERED"
            del self.on_board[address]
            return True
        else:
            return False

    def deliver_packages(self):
        while len(self.on_board) > 0:
            self.find_next_delivery()

