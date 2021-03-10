import random


class RandomList(list):
    def get_random_element(self):
        random_el = random.choice(self)
        self.remove(random_el)
        return random_el


elements = RandomList([1, 2, 3, 4, 5, 6, 7])
print(elements.get_random_element())
print(list(elements))