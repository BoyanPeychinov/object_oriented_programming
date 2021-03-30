from unittest import TestCase, main

from mammal_01.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.wolf = Mammal("Kumcho Vulcho", "predator", "auuuuu")

    def test_init_attr_are_correctly_initialized(self):
        self.assertEqual("Kumcho Vulcho", self.wolf.name)
        self.assertEqual("predator", self.wolf.type)
        self.assertEqual("auuuuu", self.wolf.sound)

    def test_private_attr_kingdom(self):
        actual = self.wolf._Mammal__kingdom
        expected = "animals"
        self.assertEqual(expected, actual)

    def test_change_value_of_kingdom__expect_exception(self):
        with self.assertRaises(AttributeError) as ex:
            self.wolf.__kingdom = "wolfs"
            self.assertNotEqual("wolfs", self.wolf.get_kingdom())
            self.assertEqual("Mammal' object has no attribute '__kingdom", str(ex.exception))

    def test_get_kingdom_value_directly__expect_exception(self):
        with self.assertRaises(AttributeError) as ex:
            kingdom = self.wolf.__kingdom
            self.assertEqual("Mammal' object has no attribute '__kingdom", str(ex.exception))

    def test_make_sound__correct_string(self):
        expected = "Kumcho Vulcho makes auuuuu"
        actual = self.wolf.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom__correct_kingdom_info(self):
        expected = "animals"
        actual = self.wolf.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info_is_equal(self):
        expected = "Kumcho Vulcho is of type predator"
        actual = self.wolf.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()