# 13. Write a NumPy program to find the number of rows and columns in a given  matrix.

import numpy as np

a1 = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

print(a1.shape[0])
print(a1.shape[1])

