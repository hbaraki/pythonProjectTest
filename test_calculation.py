from unittest import TestCase

import numpy as np

import calculation


class Test(TestCase):

    def test_product_of_two(self):
        expected_value = 50
        actual_value = calculation.product_of_two(5, 10)
        self.assertEqual(expected_value, actual_value)
        self.assertIsInstance(actual_value, np.ndarray)

    def test_product_of_two_type_error(self):
        self.assertRaises(TypeError, calculation.product_of_two, "1", "2")

