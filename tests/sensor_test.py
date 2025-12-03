import unittest
from src.car_park import CarPark
from src.sensor import EntrySensor, ExitSensor


class SensorTest(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="Perth", capacity=100)
        self.entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        self.exit_sensor = ExitSensor(id=2, is_active=True, car_park=self.car_park)

    def test_entry_sensor(self):
        initial_bays = self.car_park.available_bays
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, initial_bays - 1)
        self.assertEqual(len(self.car_park.plates), 1)
        plate = self.car_park.plates[0]
        self.assertTrue(plate.startswith("FAKE-"))

    def test_exit_sensor(self):
        self.car_park.add_car("FAKE-001")
        initial_bays = self.car_park.available_bays
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, initial_bays + 1)
        self.assertNotIn("FAKE-001", self.car_park.plates)
