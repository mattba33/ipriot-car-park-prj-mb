class Sensor:
    def __init__(self, id, is_active=False, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}:active = {self.is_active} car park={self.car_park}"

class EntrySensor(Sensor):
    def __str__(self):
        return f"EntrySensor {self.id}, active={self.is_active}, car park={self.car_park})"
class ExitSensor(Sensor):
    def __str__(self):
        return f"ExitSensor {self.id}, active={self.is_active}, car park={self.car_park})"