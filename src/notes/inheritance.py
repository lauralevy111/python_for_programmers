#inheritance

class Transportation:
    def __init__(wheels):
        self.wheels = wheels

class Car(transportation):
    def __init__(self,year, make, model, miles):
        self.year = year
        self.make = make
        self.model = model
        self.miles = miles
    def start_car():
        let position = 0
