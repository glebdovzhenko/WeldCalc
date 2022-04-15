import numpy as np


def parabola(a, b, c):
    xs = np.linspace(-10, 10, 100)
    ys = a * xs ** 2 + b * xs + c
    return xs.tolist(), ys.tolist()


parabola_kwargs = {'a': 1, 'b': 0, 'c': -1}
