ns = [3,1,4,2]
ns.sort()
print(ns)
ns.sort(reverse=True)
print(ns)

ns = [('Yoon',33), ('Lee',12), ('Park',29)]
def age(t):
    return t[1]
ns.sort(key= age)
print(ns)
ns.sort(key=age, reverse=True)
print(ns)

def name(t):
    return t[0]

ns.sort(key=name)
print(ns)
ns.sort(key=name, reverse=True)
print(ns)

names = ['Julia', 'Yoon', 'Steven']
names.sort(key=len)
print(names)

nums = [(3,1), (2,9), (0,5)]
nums.sort(key = lambda t : t[0] + t[1], reverse=True)
print(nums)

org = [('Yoon',33), ('Lee',12), ('Park',29)]
cpy = sorted(org, key=lambda t : t[1], reverse=True)
print(org)
print(cpy)