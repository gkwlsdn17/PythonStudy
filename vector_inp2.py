class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)
    def __str__(self):
        return 'Vector({0}, {1})'.format(self.x ,self.y)
    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        return self

def main():
    v1 = Vector(2, 2)
    v2 = Vector(7, 7)
    print(v1, id(v1))
    v1 += v2
    print(v1, id(v1))

main()