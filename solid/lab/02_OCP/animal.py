from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = "meow"

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = "woof-woof"

    def get_sound(self):
        return self.sound


class Dragon(Animal):
    sound = "rawr"

    def get_sound(self):
        return self.sound


class Donkey(Animal):
    sound = "I am a talking donkey"

    def get_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.sound)


animals = [Cat(), Dog(), Dragon(), Donkey()]
animal_sound(animals)

