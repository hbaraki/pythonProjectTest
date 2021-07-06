import numpy as np


def product_of_two(a: int, b: int):
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
    print("Hello World, I'm a calculator for sums")
    a = int(input("First number: "))
    b = int(input("Second number:"))
    print("Result:", sum_of_two(a, b))
    input("Press Enter to close.")
