# 15. Write a NumPy program to create a 2x3x4 array filled with arbitrary values.

import numpy as np

ans = np.random.randint(0,100,size=(2,3,4))

print(ans)
