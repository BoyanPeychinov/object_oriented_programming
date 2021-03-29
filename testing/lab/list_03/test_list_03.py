import unittest

from lab.list_03.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def test_integer_list_add_when_int__should_add_it(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_integer_list_add_when_str__expect_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("asd")

    def test_integer_list_remove_index__when_valid_index__expect_to_remove_and_return_it(self):
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, value_to_be_removed, 4)

        result = integer_list.remove_index(2)
        self.assertEqual(value_to_be_removed, 3)
        self.assertListEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_remove_index__when_invalid_negative_index__expect_exception(self):
        index = -4
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_remove_index__when_invalid_positive_index__expect_exception(self):
        index = 3
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_init__when_integers__expect_to_create_it(self):
        IntegerList(1, 2, 3)

    def test_integer_list_init__when_not_only_integers__expect_exception(self):
        with self.assertRaises(Exception):
            IntegerList(1, 2, "asd")

    def test_integer_list_get_when_valid__expect_to_return_it(self):
        integer_list = IntegerList(1, 2, 3)
        index = 2
        actual = integer_list.get(index)
        expect = integer_list.get_data()[index]
        self.assertEqual(expect, actual)

    def test_integer_list_get__when_invalid_negative_index__expect_exception(self):
        index = -4
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_get__when_invalid_positive_index__expect_exception(self):
        index = 3
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_insert_when_valid_index_and_value__expect_to_insert_it(self):
        value_to_be_inserted = 3
        index = 2
        integer_list = IntegerList(1, 2, 4)

        integer_list.insert(index, value_to_be_inserted)
        self.assertListEqual([1, 2, 3, 4], integer_list.get_data())

    # def test_integer_list_insert__when_invalid_negative_index__expect_exception(self):
    #     integer_list = IntegerList(1, 2, 3)
    #     value_to_be_inserted = 0
    #     index = len(integer_list.get_data()) * -1
    #
    #     with self.assertRaises(Exception):
    #         integer_list.insert(index, value_to_be_inserted)

    def test_integer_list_insert__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 3
        value_to_be_inserted = 4

        with self.assertRaises(IndexError):
            integer_list.insert(index, value_to_be_inserted)

    def test_integer_list_insert__when_value_is_str__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 2
        value_to_be_inserted = "asd"

        with self.assertRaises(ValueError):
            integer_list.insert(index, value_to_be_inserted)

    def test__integer_list__get_biggest__expect_to_return_biggest(self):
        biggest = 17
        integer_list = IntegerList(1, 2, biggest, 3, 4)
        actual = integer_list.get_biggest()
        self.assertEqual(biggest, actual)

    def test_integer_list__get_index_when_value_in_list__expect_to_return_index(self):
        integer_list = IntegerList(1, 2, 3)
        expected = 2
        actual = integer_list.get_index(3)
        self.assertEqual(actual, expected)

    def test_integer_list__when_value_not_in_list__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        value = 4

        with self.assertRaises(Exception):
            integer_list.get_index(value)


if __name__ == "__main__":
    unittest.main()