# ------------------------------------
# array 기본 연산
#-------------------------------------

import numpy as np
import util

# 1차원 array 연산 ---------------------------
x1 = np.arange(8)
print(f"x1 + 5\n{x1 + 5}")

# 2차원 array 연산 ---------------------------
x2 = x1.reshape((2, 4))
print(f"x2 + 5\n{x2 * 5}")

# array 끼리 연산 ----------------------------
x1 = np.arange(4).reshape((2, 2))
x2 = np.full((2, 2), 2)
print(f"x1 + x2\n{x1 + x2}")
