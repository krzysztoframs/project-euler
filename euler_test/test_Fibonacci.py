from nose.tools import assert_equal
from parameterized import parameterized

from euler.Fibonacci import Fibonacci


class TestFibonacci(object):

    @parameterized([
        (0, 0, 0),
        (1, 1, 1),
        (2, 1, 1),
        (3, 2, 1),
        (4, 3, 2),
        (5, 5, 3),
        (6, 8, 5),
        (7, 13, 8),
        (8, 21, 13),
        (9, 34, 21),
        (10, 55, 34),
        (11, 89, 55),
    ])
    def test_next_should_return_correct_result_current_and_previous_items(self, item_index: int,
                                                                          expected_result: int,
                                                                          previous_result: int):
        test_fibonacci: Fibonacci = Fibonacci()
        test_fibonacci.reset()
        result: int = 0
        for n in range(0, item_index + 1):
            result = test_fibonacci.next()

        assert_equal(expected_result, result)
        assert_equal(expected_result, test_fibonacci.get_current())
        assert_equal(previous_result, test_fibonacci.get_previous())

    def test_should_reset_to_init_state(self):
        test_fibonacci: Fibonacci = Fibonacci()
        result: int = test_fibonacci.get_item(5)
        assert_equal(5, result)

        test_fibonacci.reset()
        assert_equal(0, test_fibonacci.get_current())
        assert_equal(-1, test_fibonacci.get_current_item())
        assert_equal(0, test_fibonacci.get_previous())

    def test_should_return_selected_item_value(self):
        test_fibonacci: Fibonacci = Fibonacci()

        result: int = test_fibonacci.get_item(7)

        assert_equal(13, result)

    def test_should_return_current_item_index(self):
        test_fibonacci: Fibonacci = Fibonacci()

        test_fibonacci.get_item(6)

        assert_equal(6, test_fibonacci.get_current_item())
