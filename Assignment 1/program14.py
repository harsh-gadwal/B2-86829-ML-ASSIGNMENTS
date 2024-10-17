# 14. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

import numpy as np

ans = np.random.randint(0,100,size=(3,3,3))

print(ans)

