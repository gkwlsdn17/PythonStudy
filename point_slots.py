class Point3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

def main():
    p1 = Point3D(1, 1, 1)
    p2 = Point3D(24, 17, 31)
    print(p1)
    print(p2)

main()