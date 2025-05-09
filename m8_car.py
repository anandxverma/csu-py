class Car:

    # Class constructor
    def __init__(self, owner, vin, color, brand, model, year, drivetrain, transmission, engine, mileage):
        # Class attributes
        self.owner = owner
        self.vin = vin
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year
        self.drivetrain = drivetrain
        self.transmission = transmission
        self.engine = engine
        self.mileage = mileage

    # Start the car
    def start():
        print("Start the car")

    # Stop the car
    def stop():
        print("Stop the car")

    # Drive the car
    def drive(speed):
        print("Drive the car at", speed, "mph")

    # Turn the car
    def turn():
        print("Turn the car")

    # Reverse the car
    def reverse():
        print("Reverse the car")

johns_car = Car("John", "23564867", "Blue", "VW", "Jetta", 2025, "AWD", "Automatic", "4 Cylinder", 2500)
janes_car = Car("Jane", "43563758", "Red", "Dodge", "Durango", 2019, "AWD", "Automatic", "8 Cylinder", 47800)
sophies_car = Car("Sophie", "23457674", "Grey", "Honda", "CRV", 2011, "FWD", "Automatic", "4 Cylinder", 98050)