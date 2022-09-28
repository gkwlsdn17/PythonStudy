from collections import defaultdict

s = 'robbot'
d = {}
for k in s:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

print(d)


# setdefault
d1 = {}
for k in s:
    d1[k] = d1.setdefault(k, 0) + 1
print(d1)

# defaultdict
d2 = defaultdict(int)
for k in s:
    d2[k] += 1
print(d2)