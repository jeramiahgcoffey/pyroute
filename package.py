class Package:
    """The class holds package data"""

    def __init__(self, id, address, city, state, zip, mass, truck, deadline=None, notes=None):
        """
        This is the constructor for the Package class

        :param id: The package ID
        :param address: The delivery street address
        :param city: The delivery city
        :param state: The delivery state
        :param zip: The delivery zip code
        :param mass: The package mass is kilograms
        :param truck: The corresponding truck number
        :param deadline: The delivery deadline
        :param notes: Special notes associated with the package
        """

        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.truck = truck
        self.mass = mass
        self.notes = notes
        self.status = ''

