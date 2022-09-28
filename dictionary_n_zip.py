# Dictionary
d = {'a':1, 'b':2, 'c':3}
e = dict([('a',1), ('b',2), ('c',3)])
f = dict(a=1, b=2, c=3)
print(d, e, f)

d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)

# Zip
z = zip(['a', 'b', 'c'], [1, 2, 3])
for i in z:
    print(i, end=', ')
print('')

z = zip(('a', 'b', 'c'), (1, 2, 3))
for i in z:
    print(i, end=', ')
print('')

z = zip('abc', (1,2,3))
for i in z:
    print(i, end=', ')
print('')

# Zip 활용
d = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)

t = tuple(zip('abc','123'))
print(t)

d = dict(zip(['a', 'b', 'c'], (1, 2, 3)))
print(d)

c = list(zip('abc', (1,2,3), ['one', 'two', 'three']))
print(c)