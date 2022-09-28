class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Person3:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

def main():
    p = Person('James', 22)
    print(p.__dict__)
    p2 = Person2('James', 22)
    print(p2.__dict__)
    p3 = Person3('James', 22)
    print(p3.__dict__)

main()