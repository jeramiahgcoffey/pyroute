class Package:
    def __init__(self, id, address, city, state, zip, mass, deadline=None, notes=None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
