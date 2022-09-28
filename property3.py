class Natural:
    def __init__(self, n):
        self.n = n
    @property
    def n(self):
        return self.__n
    @n.setter
    def n(self, n):
        if(n<1):
            self.__n = 1
        else:
            self.__n = n

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n+n3.n
    print(n1.n)

main()
