from wild_animals_04.animals.animal import Bird
from wild_animals_04.food import Meat


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(0.25, food.quantity)


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(0.35, food.quantity)