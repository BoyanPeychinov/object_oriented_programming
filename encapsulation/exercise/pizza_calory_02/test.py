# from project.dough import Dough
# from project.pizza import Pizza
# from project.topping import Topping

# top_1 = Topping("ketchup", 4.5)
# top_2 = Topping("mayonnaise", 3.6)
# top_3 = Topping("mustard", 3)
#
# dough = Dough("type_500", "simple", 10)
#
# pizza = Pizza("Prima Vera", dough, 3)
#
# pizza.add_topping(top_1)
# pizza.add_topping(top_2)
# pizza.add_topping(top_3)
#
# print(pizza.calculate_total_weight())

import unittest

from pizza_calory_02.dough import Dough
from pizza_calory_02.pizza import Pizza
from pizza_calory_02.topping import Topping


class Tests(unittest.TestCase):
    def test_topping_init(self):
        t = Topping("Tomato", 20)
        self.assertEqual(t._Topping__topping_type, "Tomato")
        self.assertEqual(t._Topping__weight, 20)

    def test_dough_init(self):
        d = Dough("Sugar", "Mixing", 20)
        self.assertEqual(d._Dough__flour_type, "Sugar")
        self.assertEqual(d._Dough__baking_technique, "Mixing")
        self.assertEqual(d._Dough__weight, 20)

    def test_pizza_init(self):
        d = Dough("Sugar", "Mixing", 20)
        p = Pizza("Burger", d, 5)

        self.assertEqual(p._Pizza__name, "Burger")
        self.assertEqual(p._Pizza__dough, d)
        self.assertEqual(len(p._Pizza__toppings), 0)
        self.assertEqual(p._Pizza__toppings_capacity, 5)

    def test_pizza_add_topping_error(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 0)
        with self.assertRaises(ValueError) as ctx:
            p.add_topping(t)
        self.assertEqual("Not enough space for another topping", str(ctx.exception))

    def test_pizza_add_topping_new(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 20)
        self.assertEqual(len(p.toppings), 1)

    def test_pizza_add_topping_update(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 40)

    def test_pizza_calculate_total_weight(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.calculate_total_weight(), 60)


if __name__ == '__main__':
    unittest.main()