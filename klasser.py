import math

class Car:
    def __init__(self, color, car_type, horsepower, x=0, y=0):
        self.color = color
        self.car_type = car_type
        self.horsepower = horsepower
        self.running = False
        self.x = x
        self.y = y

    def start(self):
        if not self.running:
            print("Starting the car...")
            self.running = True
        else:
            print("The car is already running.")

    def stop(self):
        if self.running:
            print("Stopping the car...")
            self.running = False
        else:
            print("The car is already stopped.")

    def drive_to(self, x, y):
        if not self.running:
            print("Start the car first.")
            return

        distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        print(f"Driving to position ({x}, {y})... Distance: {distance:.2f}")
        self.x = x
        self.y = y

    def read_position(self):
        print(f"Current position: ({self.x}, {self.y})")


# Testprogram
def main():
    # Skapa några bilar
    car1 = Car("Red", "Sedan", 200)
    car2 = Car("Blue", "Pickup", 150)
    car3 = Car("Green", "Van", 180)

    # Visa startposition för bilarna
    print("Initial positions:")
    car1.read_position()
    car2.read_position()
    car3.read_position()

    # Starta några bilar
    car1.start()
    car2.start()
    car3.start()

    # Kör bilarna till olika positioner
    car1.drive_to(5, 3)
    car2.drive_to(-2, 7)
    car3.drive_to(10, -5)

    # Avläs bilarnas positioner
    print("\nFinal positions after driving:")
    car1.read_position()
    car2.read_position()
    car3.read_position()

    # Stanna bilarna
    car1.stop()
    car2.stop()
    car3.stop()


if __name__ == "__main__":
    main()

