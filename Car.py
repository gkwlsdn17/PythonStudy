class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f

    def drive(self):
        self.fuel -= 10

    def add_fuel(self, f):
        self.fuel += f

    def show_info(self):
        print("id: " + self.id)
        print("fuel: {0}".format(self.fuel))

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c

    def add_cargo(self, c):
        self.cargo += c

    def show_info(self):
        super().show_info()
        print("cargo: {0}".format(self.cargo))