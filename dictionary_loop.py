d = dict(a=1, b=2, c=3)
for k in d:
    print(d[k], end=',')

for key in d.keys():
    print(key, end=',')

for value in d.values():
    print(value, end=',')

for item in d.items():
    print(item, end=',')

print()
for a, b in d.items():
    print(a,b)

r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1]
d1 = dict(a=1, b=2, c=3)
d2 = {k : v*2 for k, v in d1.items()}
d3 = {k : v*2 for k, v in d2.items()}
print(d1)
print(d2)
print(d3)

ks = ['a', 'b', 'c', 'd']
vs = {1, 2, 3, 4}
d = {k: v for k, v in zip(ks, vs)}
print(d)

d2 = {k: v for k, v in zip(ks, vs) if v % 2}
print(d2)