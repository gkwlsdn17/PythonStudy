from Car import Car, Truck

class Father:
    def run(self):
        print("so fast!!!")

class Mother:
    def dive(self):
        print("so deep!!")

class Son(Father, Mother):
    def jump(self):
        print("so high!!!")
    def run(self):
        print("so fast, son style")
    def run2(self):
        super().run()

def main():
    s = Son()
    s.run()
    s.run2()
    s.jump()
    s.dive()

    t = Truck("64바5959", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()



main()