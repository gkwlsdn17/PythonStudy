class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))

    @classmethod
    def next_day(cls, today):
        return cls(today.y, today.m, today.d + 1)

class KDate(Date):
    def show(self):
        print('KOR: {0}, {1}, {2}'.format(self.y, self.m, self.d))

class JDate(Date):
    def show(self):
        print('JPN: {0}, {1}, {2}'.format(self.y, self.m, self.d))

def main():
    d1 = Date(2025, 4, 5)
    d1.show()
    d2=Date.next_day(d1)
    d2.show()

    kd1 = KDate(2025, 4, 12)
    kd1.show()
    kd2 = KDate.next_day(kd1)
    kd2.show()

    jd1 = JDate(2027, 5, 19)
    jd1.show()
    jd2 = JDate.next_day(jd1)
    jd2.show()

main()