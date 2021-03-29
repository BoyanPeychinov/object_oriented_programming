import unittest


def validate_type(value, types):
    if type(value) not in types:
        raise ValueError("numbers should be ints or floats")


def my_sum(numbers):
    [validate_type(x, [int, float]) for x in numbers]
    return sum(numbers)


class SampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("SetUPClass")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_my_sum_when_ints_expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        actual_result = my_sum(numbers)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_my_sum_when_floats_expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        actual_result = my_sum(numbers)
        expected_result = 10.1

        self.assertEqual(expected_result, actual_result, "Actual result is not equal")

    def test_my_sum_when_strings_expect_value_exception(self):
        numbers = ["a", "b", "c"]
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)

        expected_msg = "numbers should be ints or floats"
        actual_msg = context.exception.args[0]

        self.assertEqual(expected_msg, actual_msg)