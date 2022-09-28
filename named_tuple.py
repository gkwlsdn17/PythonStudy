from collections import namedtuple
Tri = namedtuple('triangle', ['bottom', 'height'])
t = Tri(3, 7)
print(t[0], t[1])
print(t.bottom, t.height)


Tri = namedtuple('Tri', 'bottom height')
t = Tri(5,8)
print(t[0], t[1])
print(t.bottom, t.height)

a, b = Tri(78, 30)
print(a, b)

def show(n1, n2):
    print(n1, n2)

t = Tri(5, 6)
show(*t)