class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


class Cat(Animal):
    def meow(self):
        return "meowing..."


maca = Cat()
sharo = Dog()
print(maca.meow())
print(maca.eat())
print(sharo.bark())
print(sharo.eat())