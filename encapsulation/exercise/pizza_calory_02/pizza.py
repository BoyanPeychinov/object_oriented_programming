class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_capacity):
        self.__toppings_capacity = new_capacity

    def add_topping(self, topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum([value for value in self.toppings.values()])
        total_weight = self.__dough.weight + toppings_weight
        return total_weight



