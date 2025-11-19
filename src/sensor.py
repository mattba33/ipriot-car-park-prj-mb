class Sensor:
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return (f"Sensor {self.id}:active = {self.is_active} "
                f"car park={self.car_park}")


class EntrySensor(Sensor):
    def __str__(self):
        return (f"EntrySensor {self.id}, "
                f"active={self.is_active}, "
                f"car park={self.car_park})")


class ExitSensor(Sensor):
    def __str__(self):
        return (f"ExitSensor {self.id}, "
                f"active={self.is_active}, "
                f"car park={self.car_park})")
