# ------------------------------------
# array 요소 접근
#-------------------------------------

import numpy as np
import util

# Numpy Array 생성 (1) ------------------------------------
array1 = np.arange(5)  # array1 = [0 1 2 3 4]
# array1 = np.arange(1, 10, 2)  # array2 = [1 3 5 7 9]
util.display('array1', array1)

# 슬라이싱 [시작 : 끝] <= 끝 미포함 --------------------------
array2 = array1[2:4]
util.display("array2", array2)

# Numpy Array 2차원 배열 생성 ------------------------------
array3 = np.array([[1, 2, 3], [4, 5, 6]])
# 첫번째 0:1는 행의 범위, 두번째 1:3은 열의 범위
array4 = array3[0:1, 1:3]
util.display("array4", array4)