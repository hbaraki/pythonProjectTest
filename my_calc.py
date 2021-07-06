import doctest

import numpy as np


def product_of_two(a: int, b: int):
    """
    Return product of two integers.
    >>> product_of_two(5,10)
    array([50])
    >>> product_of_two(-5,10)
    array([-50])
     >>> product_of_two("5","10")
     Traceback (most recent call last):
     ...
     TypeError: Expect integer
    """
    if type(a) != int or type(b) != int:
        raise TypeError("Expect integer")
    np_a = np.array([a])
    np_b = np.array([b])
    return np_a * np_b


def sum_of_two(a: int, b: int):
    np_a = np.array([a])
    np_b = np.array([b])
    return np_a + np_b


if __name__ == '__main__':
    doctest.testmod()
