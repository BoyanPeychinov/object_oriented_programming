class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


bubcho = Dog()
print(bubcho.eat())
print(bubcho.bark())