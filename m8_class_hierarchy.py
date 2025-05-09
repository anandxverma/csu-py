class Vehicle:

    def __init__(self, body_style):
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    
    def __init__(self, engine_type):
        super().__init__(body_style="Car")
        self.engine_type = engine_type
        self.num_doors = 4
        self.num_wheels = 4

    def drive(self, speed):
        super().drive(speed)
        print("Driving a ", self.engine_type, " car at", self.speed, "mph")

class MotorCycle(Vehicle):

    def __init__(self, engine_type, has_sidecar):
        super().__init__("Motor Cycle")
        self.engine_type = engine_type
        if has_sidecar:
            self.num_wheels = 3
        else:
            self.num_wheels = 2

car1 = Car("Gas")
car2 = Car("Electric")
mc1 = MotorCycle("Gas", True)
mc2 = MotorCycle("Gas", False)

car1.drive("30")