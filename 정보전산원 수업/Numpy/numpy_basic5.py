# ------------------------------------
# array 행렬 곱연산
#-------------------------------------

import numpy as np
import util

x1 = np.arange(4).reshape((2, 2))
x2 = np.full((2, 2), 2)
print(x1)
print(x2)

# 곱하기 연산 --------------------------
print("np.matnul(x1, x2)\n", np.matmul(x1, x2), "\n")
print("np.dot(x1, x2)\n", np.dot(x1, x2), "\n")
print("x1.dot(x2)\n", x1.dot(x2), "\n")
print("x1@x2\n", x1@x2, "\n")
print("x1*x2\n", x1*x2, "\n")  # 얘는 위치에 대칭되는 값끼리 곱하는 연산임, 행렬 곱 연산이 아님!!!
