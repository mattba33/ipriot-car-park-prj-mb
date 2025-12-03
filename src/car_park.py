from .display import Display
from .sensor import Sensor
from pathlib import Path


class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None, log_file=None):
        self.location = location
        self.capacity = capacity
        self.displays = displays if displays is not None else []
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []

        if log_file is None:
            self.log_file = Path("log.txt")
        else:
            self.log_file = Path(log_file)

        self.log_file.touch(exist_ok=True)

    def _log(self, plate, action):
        with self.log_file.open("a") as file:
            file.write(f"{plate} {action}\n")
            file.flush()

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)

    def update_displays(self):
        data = {"available_bays": self.available_bays,
                "Location": self.location,
                "temperature": 25
                }
        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        if len(self.plates) < self.capacity and plate not in self.plates:
            self.plates.append(plate)
            self._log(plate, "entered")

        self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self._log(plate, "exited")
        elif len(self.plates) >= self.capacity:
            pass
        else:
            raise ValueError("Car not in car park")

        self.update_displays()

    @property
    def available_bays(self):
        if self.capacity < len(self.plates):
            return 0
        else:
            return self.capacity - len(self.plates)

    def __str__(self):
        return (f"Car park location: {self.location!r}, "
                f"capacity: {self.capacity}, "
                f"plates: {self.plates}, "
                f"displays: {self.displays})")
