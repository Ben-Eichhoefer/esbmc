import numpy as np

x = np.add(1.0, 4.0)
assert x == 5.0

y = np.add(1, 2)
assert y == 3

z = np.add(127, 1, dtype=np.int8)
assert z == -128