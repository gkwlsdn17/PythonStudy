from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

d1 = dict(a=1, b=2, c=3)
d2 = dict(c=3, a=1, b=2)
print(d1==d2)

od1 = OrderedDict(a=1, b=2, c=3)
od2 = OrderedDict(c=3, a=1, b=2)
print(od1==od2)

for kv in od.items():
    print(kv, end=' ')
print()
od.move_to_end('b')
for kv in od.items():
    print(kv, end=' ')
print()

od.move_to_end('b',last = False) # 맨 앞 이동
for kv in od.items():
    print(kv, end = ' ')
