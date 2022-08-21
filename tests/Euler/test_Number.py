from unittest import TestCase

from euler.Number import Number


class TestNumberIsEven(TestCase):
    def test_is_even(self):
        result: bool = Number.is_even(2)

        self.assertTrue(result)

    def test_is_odd(self):
        result: bool = Number.is_odd(2)

        self.assertFalse(result)

    def test_is_not_even(self):
        result: bool = Number.is_even(3)

        self.assertFalse(result)

    def test_is_not_odd(self):
        result: bool = Number.is_odd(1)

        self.assertTrue(result)

    def test_is_multiplication_of_both_factors(self):
        factors: list[int] = [2, 3]

        result: bool = Number.is_multiplication_of_any_factor(factors, 6)

        self.assertTrue(result)

    def test_is_multiplication_of_any_factors(self):
        factors: list[int] = [2, 3]

        result: bool = Number.is_multiplication_of_any_factor(factors, 9)

        self.assertTrue(result)

    def test_is_not_multiplication_of_any_factor(self):
        factors: list[int] = [2, 3]

        result: bool = Number.is_multiplication_of_any_factor(factors, 7)

        self.assertFalse(result)

    def test_throws_type_error_when_factors_list_is_none(self):
        with self.assertRaises(TypeError):
            Number.is_multiplication_of_any_factor([], 6)
