from dataclasses import dataclass


class singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


@singleton
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = id(Person("Gosho", 11))
p2 = id(Person("Gosho", 17))
print(p1 == p2)
print(id(p1))
print(id(p2))


@dataclass
class Person2:
    name: str
    age: int


print(Person2("Maria", 11))