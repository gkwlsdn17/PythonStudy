def show_all(s):
    for i in s:
        print(i, end=' ')

g = (2 * i for i in range(1,10))
# show_all(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def two():
    print('two')
    return 2

g = (two() * i for i in range(1,10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

show_all(2*s for s in range(1,10))