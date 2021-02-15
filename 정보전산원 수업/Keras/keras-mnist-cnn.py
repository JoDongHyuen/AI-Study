# ------------------------------
# MNIST & CNN (합성곱 신경망)
# ------------------------------
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from keras.datasets import mnist
from keras.utils import np_utils

# 입력과 출력 지정하기
im_rows = 28  # 이미지 높이
im_cols = 28  # 이미지 너비
im_color = 1  # 이미지 색공간
in_shape = (im_rows, im_cols, im_color)  # 데이터 포맷 설정
out_size = 10  # One_Hot_Encoding 0 ~ 9 까지 숫자패턴이 필요해서 10개가 필요함

# (1) 데이터 준비 ------------------------------------------------------
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()  # 튜플 타입으로 리턴해 줌

# 데이터 28*28=784를 1차원 배열 변환
X_train = X_train.reshape(-1, im_rows, im_cols, im_color).astype('float32') / 255
X_train = X_train.astype('float32') / 255

X_test = X_test.reshape(-1, im_rows, im_cols, im_color).astype('float32') / 255
X_test = X_test.astype('float32') / 255

# 레이블 데이터를 One-hot 형식으로 변환
Y_train = np_utils.to_categorical(Y_train.astype('int32'), 10)
Y_test = np_utils.to_categorical(Y_test.astype('int32'), 10)

# ---------------------------------------------------------------------------------------------------------
# (2) CNN 모델 정의
model = Sequential()
model.add(Conv2D(32,
                 kernel_size=(3, 3),
                 activation='relu',
                 input_shape=in_shape))
model.add(Conv2D(32, (3, 3), activation='relu'))


# 특징맵 축소
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())

# 2차원 특징맵 => 1차원 배열로 변환
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.5))

# 출력 레이어
model.add(Dense(out_size, activation='softmax'))

# 모델 정보 확인
model.summary()

# ---------------------------------------------------------------------------------------------------------
# (3) 모델 생성
model.compile(loss='categorical_crossentropy',
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
