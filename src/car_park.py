from src.display import Display
from src.sensor import Sensor
from pathlib import Path
from datetime import datetime
import json


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

    # Car park Functions
    def _log(self, plate, action):
        """
            Logs a vehicle action to the log file with a timestamp.

            This method appends a new line to the log file in the format:
            "<plate> <action> at <YYYY-MM-DD HH:MM:SS>"

            Parameters
            ----------
            plate : str
                The license plate of the vehicle.
            action : str
                The action performed by the vehicle (e.g., "entered", "exited").

            Returns
            -------
            None
            """
        with self.log_file.open("a") as file:
            file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            file.flush()

    def write_config(self, filename="config.json"):
        with open(filename, "w") as f:
            json.dump({
                "location": self.location,
                "capacity": self.capacity,
                "log_file": str(self.log_file)
            }, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as file:
            config = json.load(file)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)

    def update_displays(self):
        data = {
                "available_bays": self.available_bays,
                "Location": self.location,
                "temperature": 25
                }

        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        if len(self.plates) < self.capacity and plate not in self.plates:
            self.plates.append(plate)
            self.update_displays()
            self._log(plate, "entered")

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
