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

        self.address = address
        self.city = city
        self.deadline = deadline
        self.id = id
        self.mass = mass
        self.notes = notes
        self.state = state
        self.time_delivered = None
        self.time_loaded = None
        self.truck = truck
        self.zip = zip

    def set_notes(self, new_note):
        self.notes = new_note

    def get_status(self):
        return self.status

