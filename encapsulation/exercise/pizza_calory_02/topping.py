class Topping:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, new_type):
        self.__topping_type = new_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight