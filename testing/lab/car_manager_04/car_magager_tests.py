from unittest import TestCase, main

from lab.car_manager_04.car_manager import Car


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("make", "model", 10, 100)

    def test_init_for_correct_attr_initialization(self):
        self.assertEqual("make", self.car.make)
        self.assertEqual("model", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_setter__when_None__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.make = None

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_make_setter__with_empty_string__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_make_setter__with_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.make = 0

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_make_setter__with_correct_value__expect_new_value(self):
        self.car.make = "new_make"

        self.assertEqual("new_make", self.car.make)

    def test_car_model_setter__when_None__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.model = None

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_model_setter__with_empty_string__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_model_setter__with_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.model = 0

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_model_setter__with_correct_value__expect_new_value(self):
        self.car.model = "new_model"

        self.assertEqual("new_model", self.car.model)

    def test_car_fuel_consumption_setter__when_equal_to_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_consumption_setter__when_below_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_consumption_setter__with_correct_value__expect_new_value(self):
        self.car.fuel_consumption = 11

        self.assertEqual(11, self.car.fuel_consumption)

    def test_car_fuel_capacity_setter__when_equal_to_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity_setter__when_below_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity_setter__with_correct_value__expect_new_value(self):
        self.car.fuel_capacity = 101

        self.assertEqual(101, self.car.fuel_capacity)

    def test_car_fuel_amount_setter__when_below_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_car_fuel_amount_setter__with_correct_value__expect_new_value(self):
        self.car.fuel_amount = 1

        self.assertEqual(1, self.car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_0__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_provided_fuel(self):
        fuel = 50
        self.car.refuel(fuel)

        self.assertEqual(fuel, self.car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_fuel_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(self):
        self.car.refuel(self.car.fuel_capacity * 2)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_car_drive__if_needed_fuel_is_more_than_fuel_amount__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.car.refuel(7)
            self.car.drive(80)
            self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_car_drive__if_fuel_is_enough__expect_fuel_amount_to_decrease(self):
        self.car.fuel_amount = self.car.fuel_capacity
        self.car.drive(80)

        self.assertEqual(92.0, self.car.fuel_amount)


if __name__ == '__main__':
    main()