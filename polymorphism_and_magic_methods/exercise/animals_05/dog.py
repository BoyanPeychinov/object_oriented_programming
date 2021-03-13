from animals_05.animal import Animal


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a " \
               f"{self.age} year old {self.gender} {self.__class__.__name__}"
