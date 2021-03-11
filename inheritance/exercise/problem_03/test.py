from problem_03.blade_knight import BladeKnight
from problem_03.elf import Elf
from problem_03.hero import Hero
from problem_03.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
soul_master = SoulMaster("S", 10)
print(soul_master.username)
print(soul_master.level)
print(str(soul_master))
print(soul_master.__class__.__base__.__name__)
print(soul_master.__class__.__bases__[0].__name__)
print(SoulMaster.__mro__)
print(help(soul_master))
blade_knight = BladeKnight("B", 12)
print(blade_knight.username)
print(blade_knight.level)
print(str(blade_knight))
print(blade_knight.__class__.__bases__[0].__name__)