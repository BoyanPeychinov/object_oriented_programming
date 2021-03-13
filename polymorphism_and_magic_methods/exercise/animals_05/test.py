from animals_05.kitten import Kitten
from animals_05.tomcat import Tomcat
from animals_05.cat import Cat
from animals_05.dog import Dog


c = Cat("c", 2, "j")
print(repr(c))
print(c.make_sound())

d = Dog("d", 3, "j")
print(repr(d))
print(d.make_sound())

k = Kitten("k", 4)
print(repr(k))
print(k.make_sound())

t = Tomcat("t", 5)
print(repr(t))
print(t.make_sound())