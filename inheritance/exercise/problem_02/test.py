from problem_02.bear import Bear
from problem_02.lizard import Lizard
from problem_02.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
bear = Bear("Meca")
print(bear.name)
print(bear._Animal__name)
