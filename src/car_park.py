from sensor import Sensor
from display import Display


class Carpark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.displays = displays if displays is not None else []
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)

    def __str__(self):
        return (f"Car park location: {self.location!r}, "
                f"capacity: {self.capacity}, "
                f"plates: {self.plates}, "
                f"displays: {self.displays})")
