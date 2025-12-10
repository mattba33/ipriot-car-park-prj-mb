class Display:
    def __init__(self, id, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    # Display Functions
    def update(self, data):
        print(f"Display {self.id}: {self.message}")
        for key, value in data.items():
            print(f"{key}: {value}")

            if key == "message":
                self.message = value
        print("\n")

    def __str__(self):
        return f"Display {self.id}: {self.message}"
