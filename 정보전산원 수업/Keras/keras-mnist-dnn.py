# ------------------------------
# MNIST & DNN (심층 신경망)
# ------------------------------
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.datasets import mnist
from keras.utils import np_utils

# 입력과 출력 지정하기
in_size = 28*28  # 784개의 feature, 28*28의 픽셀사이즈이기 때문에
out_size = 10  # One_Hot_Encoding 0 ~ 9 까지 숫자패턴이 필요해서 10개가 필요함

# (1) 데이터 준비 ------------------------------------------------------
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()  # 튜플 타입으로 리턴해 줌

# 데이터 28*28=784를 1차원 배열 변환
X_train = X_train.reshape(-1, 784).astype('float32') / 255
X_test = X_test.reshape(-1, 784).astype('float32') / 255

# 레이블 데이터를 One-hot 형식으로 변환
Y_train = np_utils.to_categorical(Y_train.astype('int32'), 10)
Y_test = np_utils.to_categorical(Y_test.astype('int32'), 10)

# ---------------------------------------------------------------------------------------------------------
# (2) DNN 모델 정의
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(out_size, activation='softmax'))

# 모델 정보 확인
model.summary()

# ---------------------------------------------------------------------------------------------------------
# (3) 모델 생성
model.compile( loss='categorical_crossentropy',
               optimizer='adam',
               metrics=['accuracy'])

# ---------------------------------------------------------------------------------------------------------
# (4) 학습 & 평가
model.fit(X_train, Y_train,
          batch_size=128,
          epochs=50,
          verbose=1,
          validation_data=(X_train, Y_train))  # verbose는 진행 상황을 보겠다는 뜻임

# ----------------------------------------------------------------------------------------------------------
score = model.evaluate(X_test, Y_test, verbose=1)
print(f"정답률 = {score[1]}, loss = {score[0]}")
