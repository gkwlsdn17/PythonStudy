import timeit

class Point3D:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

def main():
    start = timeit.default_timer()
    p = Point3D(1, 1, 1)

    for i in range(3000):
        for i in range(3000):
            p.x += 1
            p.y += 1
            p.z += 1
    print(p)

    stop = timeit.default_timer()
    print(stop - start)

main()