names = ['윤나은', '김현주', '장현지', '이지선', '박선주']
names.sort()
dnames = {}
i = 0
for name in names:
    dnames[i] = name
    i += 1
print(dnames)

names = ['윤나은', '김현주', '장현지', '이지선', '박선주']
eo = enumerate(names, 10)
for n in eo:
    print(n)

dnames = {k: v for k, v in enumerate(sorted(names))}
print(dnames)