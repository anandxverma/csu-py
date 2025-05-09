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
        self.__mileage = mileage

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

    # Get Mileage
    def get_mileage(self, new_miles_driven):
        self.__mileage = self.__mileage + new_miles_driven
        return self.__mileage

johns_car = Car("John", "23564867", "Blue", "VW", "Jetta", 2025, "AWD", "Automatic", "4 Cylinder", 2500)
janes_car = Car("Jane", "43563758", "Red", "Dodge", "Durango", 2019, "AWD", "Automatic", "8 Cylinder", 47800)
sophies_car = Car("Sophie", "23457674", "Grey", "Honda", "CRV", 2011, "FWD", "Automatic", "4 Cylinder", 98050)

print(f"New mileage for {johns_car.owner}'s car is {johns_car.get_mileage(1000)} miles")
print(f"New mileage for {janes_car.owner}'s car is {janes_car.get_mileage(350)} miles")
print(f"New mileage for {sophies_car.owner}'s car is {sophies_car.get_mileage(2730)} miles")
