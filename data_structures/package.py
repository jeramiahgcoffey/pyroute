class Package:
    """Models Package objects"""

    def __init__(self, id, address, city, state, zip, mass, truck, deadline=None, notes=None):
        """
        Initialize Package objects.

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param id: Integer. The package ID.
        :param address: String. The delivery street address.
        :param city: String. The delivery city.
        :param state: String. The delivery state.
        :param zip: String. The delivery zip code.
        :param mass: String. The package mass in kilograms.
        :param truck: Integer. The corresponding truck ID.
        :param deadline: String. The delivery deadline.
        :param notes: String. Special notes associated with the package.
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


