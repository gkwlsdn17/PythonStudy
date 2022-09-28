def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(2)
f2 = maker(3)

print(f1(7))
print(f2(7))