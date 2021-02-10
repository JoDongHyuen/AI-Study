# ------------------------------------
# array 형태 변경
#-------------------------------------

import numpy as np
import util

# array 생성 ---------------------------------------
array = np.arange(8)
util.display('array', array)

# 형태 변경 reshape( (행, 열) ) ----------------------
# 0, 1, 2, 3, 4, 5, 6, 7 => (2, 4)
matrix = array.reshape((2, 4))
util.display('matrix', matrix)

# 0, 1, 2, 3, 4, 5, 6, 7 => (-1, 2)
matrix = array.reshape((-1, 2))
util.display('matrix', matrix)

# 트랜스포즈
matrixT = matrix.T
util.display('matrixT', matrixT)

# 1차원으로 변환
array2 = matrix.reshape(-1)
util.display('array2', array2)

