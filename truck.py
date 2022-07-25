class Truck:
    """This class represents a Truck which holds and delivers Package objects"""

    def __init__(self):
        self.packages = []
        self.capacity = 16

    def add(self, package_object):
        """
        Add package object to the packages array

        :param package_object: A Package object representing package data
        :return: Boolean representing status of the addition
        """

        if len(self.packages) < self.capacity:
            self.packages.append(package_object)
            return True
        return False
