class Simple:
    pass

s = Simple()
print(isinstance(s, Simple))

print(isinstance([1,2], list))

class Fruit:
    pass

class Apple(Fruit):
    pass

class SuperApple(Apple):
    pass

sa = SuperApple()
print(isinstance(sa, SuperApple))
print(isinstance(sa, Apple))
print(isinstance(sa, Fruit))

print(issubclass(SuperApple, Fruit))
print(issubclass(SuperApple, object))