# ---------------------------------------------------
# 선형 회귀 실습
# ---------------------------------------------------

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt

# 데이터 준비 -----------------------------------------
X = [1, 2, 3, 4, 5, 6, 7, 8, 9]             # 공부시간
Y = [0, 0, 0, 0, 0, 1, 1, 1, 1]    # 합격 여부

# 모델 구성 & 생성 ------------------------------------
model = Sequential()

# 레이어 추가
# 출력노드 갯수, 입력 데이터 갯수, 1차원 입력 -> 1차원 출력 =~ linear
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# sgd 경사 하강법 / 학습률(learing rate, lr) : 0.01
sgd = optimizers.SGD(lr=0.05)

# 모델 생성
model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['mse', 'accuracy'])

# 모델 학습 -------------------------------------------
model.fit(X, Y, batch_size=1, epochs=300, shuffle=False)

# 검증 및 시각화 ---------------------------------------
plt.plot(X, model.predict(X), 'b', X, Y, 'ro')
plt.show()
