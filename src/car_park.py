class Carpark:
    def __init__(self, location, capcity, plates=None, displays=None):
        self.location = location
        self.capacity = capcity
        self.displays = displays if displays is not None else []
        self.plates = plates if plates is not None else []

    def __str__(self):
        return (f"Car park location: {self.location!r}, "
                f"capacity: {self.capacity}, "
                f"plates: {self.plates}, "
                f"displays: {self.displays})")
