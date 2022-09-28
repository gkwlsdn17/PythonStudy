A = set(['a','c','d','f'])
B = set('fdca')
print(A)
print(B)
print(A==B)
print('a' in A)
print('b' not in B)
for c in A & B:
    print(c, end=' ')

d = {}
print(type(d))

s = set()
print(type(s))

t = [3, 3, 3, 7, 7, 'z', 'z']
t = list(set(t))
print(t)

# set - mutable
# frozenset - immutable

os = {1, 2, 3, 4, 5}
os.add(6)
os.discard(1)
print(os)
os.update({7,8,9})
print(os)
os &= {2,4,6,8}
print(os)
os -= {2,4}
print(os)
os ^= {1,3,6}
print(os)
s1 = {x for x in range(1, 11)}
s2 = {x**2 for x in s1}
s3 = {x for x in s2 if x < 50}
print(f'{s1}\n{s2}\n{s3}')