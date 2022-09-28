def deco(func):
    def df():
        print('emotion!')
        func()
        print('emotion!')
    return df

@deco
def smile():
    print("^_^")

smile()

def adder_deco(func):
    def ad(*args):
        print(*args, sep=' + ', end=' ')
        print("= {0}".format(func(*args)))
    return ad

@adder_deco
def adder2(n1, n2):
    return n1 + n2

@adder_deco
def adder3(n1, n2, n3):
    return n1 + n2 + n3

def main():
    adder2(3, 4)
    adder3(3, 5, 7)

main()

