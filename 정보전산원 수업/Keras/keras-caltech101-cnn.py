from keras.models import Sequential
from keras.layers import  Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

categories = ['chair', 'camera', 'butterfly', 'elephant', 'flamingo']
nb_classes = len(categories)

# 이미지 크기 정학기
image_w = 64
image_h = 64

# 데이터 열기
X_train, X_test, Y_train, Y_test = np.load("./DATA/5obj.npy", allow_pickle=True)

# 데이터 정규화하기
X_train = X_train.astype('float32') / 256
X_test = X_test.astype('float32') / 256
print('X_train shape:', X_train.shape)

# 모델 구축하기
model = Sequential()
model.add( Conv2D(32,
                  kernel_size=(3, 3),
                  padding='same',
                  activation='relu',
                  input_shape=X_train.shape[1:]))
model.add( MaxPooling2D(pool_size=(2, 2)))
model.add( Dropout(0.25))

model.add(Conv2D(64,
                 kernel_size=(3, 3),
                 padding='same',
                 activation='relu'))
model.add(Conv2D(64, kernel_size=(3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 일차원 데이터 변환하기
model.add(Flatten())

# 데이터 전결합 처리
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

# 출력층
model.add(Dense(nb_classes, activation='softmax'))

# 모델 정보 확인
model.summary()

# 모델 생성하기 --------------------------------------------
model.compile(loss = 'categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델 훈련하기 --------------------------------------------
model.fit(X_train, Y_train, batch_size=32, epochs=50)

# 모델 평가하기
score = model.evaluate(X_test, Y_test)
print("loss=", score[0])
print("accuracy=", score[1])