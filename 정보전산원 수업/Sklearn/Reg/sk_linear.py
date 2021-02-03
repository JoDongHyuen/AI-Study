# --------------------------------------
# Scikit-learn Linear Regression 실습
# --------------------------------------
# 모듈 로딩 -----------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터 준비 ----------------------------------
x = np.array([2, 4, 6, 8, 10])
y = np.array([81, 89, 93, 91, 97])

print(f"type(x) => {type(x)}, x.shape =>{x.shape}")

# 2차원으로 변경 - 항상 2차원 배열에 담아야함
x = x.reshape(-1, 1)  # (행, 열), -1, 1 은 열개수만큼 행을 맞추라는 뜻
print(f"type(x) => {type(x)}, x.shape =>{x.shape}")

# 학습 모델 객체 생성 ----------------------------------
model = LinearRegression()  # 모델 객체 생성
model.fit(x, y)  # 데이터 학습 후 모델 생성
print(f"W = {model.coef_}\nb = {model.intercept_}")

# 예측 및 모델 평가 ------------------------------------
y2 = model.predict(x)  # 가설에 의한 예측값
print(f"y => {y}")
print(f"y2 => {y2}")
y2 = y2.reshape(-1, 1)

# 생성된 가설 모델에 데이터 적용 후 성능평가
print("성능평가 moodel.score(x, y) =>", model.score(x, y))

# 그래프 출력
plt.plot(x, y, "ro")

plt.grid()
plt.show()