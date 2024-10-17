# 23. Write a NumPy program to get the element-wise remainder of an array
# of numbers from 20 to 50 which are divisible by 3.

import numpy as np

num = np.arange(20,51)

div_3 = num[num % 3 == 0]

print(np.mod(div_3,3))