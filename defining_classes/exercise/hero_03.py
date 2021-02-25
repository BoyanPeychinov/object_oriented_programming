class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def check_health(self, health):
        if self.health <= 0:
            self.health = 0
            return True
        return False

    def defend(self, damage):
        self.health -= damage
        if self.check_health(self.health):
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
