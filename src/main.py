from src.car_park import CarPark
from src.sensor import EntrySensor, ExitSensor
from src.display import Display

# Configuration
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")
car_park.write_config("moondalup_config.json")
car_park = CarPark.from_config("moondalup_config.json")

# Instances
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

# Register
car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

# Simulation
print("\n--- Driving 10 cars in ---")
for _ in range(10):
    entry_sensor.detect_vehicle()

print("\n--- Driving 2 cars out ---")
for _ in range(2):
    exit_sensor.detect_vehicle()
