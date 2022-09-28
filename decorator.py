def smile():
    print("^_^")

def confused():
    print("@_@")

smile()
confused()

def deco(func):
    def df():
        print('emoticon!')
        func()
        print('emoticon!')
    return df

smile = deco(smile)
smile()

confused = deco(confused)
confused()

def adder2(n1, n2):
    return n1 + n2

def adder3(n1, n2, n3):
    return n1 + n2 + n3

print(adder2(3, 4))
print(adder3(3, 5, 7))

def adder_deco(func):
    def ad(*args):
        print(*args, sep=' + ', end=' ')
        print("= {0}".format(func(*args)))
    return ad

adder2 = adder_deco(adder2)
adder3 = adder_deco(adder3)
adder2(3, 4)
adder3(3, 5, 7)