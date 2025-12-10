import random
from abc import abstractmethod


class Sensor:
    def __init__(self, id, car_park, is_active=False,):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    # Sensor Functions
    @abstractmethod
    def update_car_park(self, plate):
        pass

    def scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self.scan_plate()
        self.update_car_park(plate)

    def __str__(self):
        return (f"Sensor {self.id}:active = {self.is_active} "
                f"car park={self.car_park}")


class EntrySensor(Sensor):
    # Entry Sensor Functions

    def update_car_park(self, plate):
        print(f"Incoming vehicle detected. Plate: {plate}")
        self.car_park.add_car(plate)

    def __str__(self):
        return (f"EntrySensor {self.id}, "
                f"active={self.is_active}, "
                f"car park={self.car_park})")


class ExitSensor(Sensor):
    # Exit Sensor Functions

    def update_car_park(self, plate):
        print(f"Outgoing vehicle detected. Plate: {plate}")
        self.car_park.remove_car(plate)

    def scan_plate(self):
        return random.choice(self.car_park.plates)

    def __str__(self):
        return (f"ExitSensor {self.id}, "
                f"active={self.is_active}, "
                f"car park={self.car_park})")
