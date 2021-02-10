import numpy as np
import util

# Numpy Array 1차원 배열 생성 -------------------------------
array = np.array([1, 2, 3, 4, 5])
util.display('array', array)
print("\n")

# Numpy Array 2차원 배열 생성 -------------------------------
array = np.array([[1, 2, 3], [4, 5, 6]])
util.display('array', array)
print("\n")

# Numpy Array 메소드 ---------------------------------------
print("array.max() -> ", array.max())
print("array.min() -> ", array.min())
print("array.sum() -> ", array.sum())
print("array.sum(axis=0) -> ", array.sum(axis=0))
print("array.sum(axis=1) -> ", array.sum(axis=1))
print("array.mean() -> ", array.mean())
print("array.std() -> ", array.std())  # 표준편차
print("\n")

# 타입 변경 astype -----------------------------------------
array = array.astype(np.float64)
print("dtype -> ", array.dtype)
print("data -> \n", array)
print("\n")

# 배열을 모두 0으로 생성 ==> zeros()
array2 = np.zeros(5, dtype=int)
array3 = np.zeros((2,3), dtype=int)
util.display('array2', array2)
util.display('array3', array3)

# 사용자 지정한 값 ==> full()
array2 = np.full(4, 7)
array3 = np.full((2, 5), 3.1)
util.display('array2', array2)
util.display('array3', array3)

# 단위 행렬 생성하기 ==> eye()
array2 = np.eye(3)
util.display('array2', array2)