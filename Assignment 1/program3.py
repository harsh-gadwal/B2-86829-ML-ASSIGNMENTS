# 3.  Write a NumPy program to create an array of 10 zeros, 10 ones,
# 10 fives, 10 tens, 10 twentys and 10 fiftys.

import numpy as np

a1 = np.zeros(10, dtype=np.int8)
print(f"a1 = {a1}")

a2 = np.ones(10, dtype=np.int8)
print(f"a2 = {a2}")

print(f"a3 = {a1 + 5}")

print(f"a4 = {a1 + 10}")

print(f"a5 = {a1 + 20}")

print(f"a6 = {a1 + 50}")