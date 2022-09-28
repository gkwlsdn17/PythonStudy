class Natural:
    def __init__(self, n):
        self.n = n
    def getn(self):
        return self.n
    @classmethod
    def add(cls, n1, n2):
        return cls(n1.getn() + n2.getn())

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural.add(n1, n2)
    print('{0} + {1} = {2}'.format(n1.getn(), n2.getn(), n3.getn()))

main()