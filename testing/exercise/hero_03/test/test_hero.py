from unittest import TestCase, main

from hero_03.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero("Gosho", 5, 100, 10)
        self.enemy_hero = Hero("Tosho", 10, 80, 20)

    def test_check_attr_are_set(self):
        self.assertEqual("Gosho", self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle_raises_if_fight_self(self):
        same_hero = Hero("Gosho", 4, 90, 9)

        with self.assertRaises(Exception)as ex:
            self.main_hero.battle(same_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_is_zero_raises(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)

        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_is_less_than_zero_raises(self):

        self.main_hero.health = -5
        self.assertEqual(-5, self.main_hero.health)

        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_enemy_hero_is_zero_raises(self):
        self.enemy_hero.health = 0
        self.assertEqual(0, self.enemy_hero.health)

        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight Tosho. He needs to rest", str(ex.exception))

    def test_health_enemy_hero_is_less_than_zero_raises(self):

        self.enemy_hero.health = -5
        self.assertEqual(-5, self.enemy_hero.health)

        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight Tosho. He needs to rest", str(ex.exception))

    def test_fight_draw_case(self):
        # Bring down enemy hero to 50 so that it could be equal to the dmg of main hero
        self.enemy_hero.health = 50

        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_main_hero_wins(self):
        self.main_hero.damage = 200
        self.main_hero.health = 300
        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(205, self.main_hero.damage)
        self.assertEqual(6, self.main_hero.level)
        self.assertEqual(105, self.main_hero.health)

    def test_enemy_wins(self):
        result = self.main_hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(35, self.enemy_hero.health)
        self.assertEqual(25, self.enemy_hero.damage)
        self.assertEqual(11, self.enemy_hero.level)

        self.assertTrue(self.main_hero.health < 0)

    def test_string_represent(self):
        self.assertEqual("Hero Gosho: 5 lvl\nHealth: 100\nDamage: 10\n", str(self.main_hero))
        # result = str(self.main_hero).split("\n")
        # self.assertEqual("Hero Gosho: 5 lvl", result[0])
        # self.assertEqual("Health: 100", result[1])
        # self.assertEqual("Damage: 10", result[2])


if __name__ == "__main__":
    main()