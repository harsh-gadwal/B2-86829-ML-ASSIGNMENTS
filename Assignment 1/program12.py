# 12. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

import numpy as np

ans = np.arange(10,22).reshape(3,4)

print(ans)