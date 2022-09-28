def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(101)
print(f1.__closure__[0].cell_contents)