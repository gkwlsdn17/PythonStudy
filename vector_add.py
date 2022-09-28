class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)
    def __call__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

def main():
    v1 = Vector(3, 3)
    v2 = Vector(7, 7)
    v3 = v1 + v2
    print(v1())
    print(v2())
    print(v3())

main()