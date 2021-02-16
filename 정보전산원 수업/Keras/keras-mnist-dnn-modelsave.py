# ------------------------------
# MNIST & DNN (심층 신경망)
# ------------------------------
import os

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import np_utils
from keras.callbacks import EarlyStopping

# 입력과 출력 지정하기


in_size = 28 * 28  # 784개의 feature, 28*28의 픽셀사이즈이기 때문에
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
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 자동 중단 설정 --------------------------------------------------------------------------------------------
# 에포크 마다 val_loss 감소가 10회 연속 지속될 경우 조기 종료
early_stop_callback = EarlyStopping(monitor='val_loss', patience=10)

# ---------------------------------------------------------------------------------------------------------
# (4) 학습 & 평가
history = model.fit(X_train, Y_train,
                    batch_size=128,
                    epochs=50,
                    verbose=1,
                    validation_data=(X_train, Y_train),
                    callbacks=[early_stop_callback])  # verbose는 진행 상황을 보겠다는 뜻임

# -----------------------------------------------------------------------------------------------------------
fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

# 손실 데이터 축
loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='lower left')

# 정확도 데이터 축
acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')
# acc_ax.set_xlabel('epoch')
acc_ax.set_ylabel('accuracy')
acc_ax.legend(loc='upper left')

# 그래프 화면 출력
plt.show()

# ----------------------------------------------------------------------------------------------------------
score = model.evaluate(X_test, Y_test, verbose=1)
print(f"정답률 = {score[1]}, loss = {score[0]}")


# 모델 저장
if score[1] * 100 >= 96:
    MODEL_FILE = "./Model/mnist_dnn_model.h5"
    model.save(MODEL_FILE)
    if os.path.exists(MODEL_FILE):
        print("Model Save OK")

    # 모델 아키텍처 따로 저장 ----------------------------------------------------------------------------------
    # json 형태로 저장
    json_string = model.to_json()
    JSON_ARCH_FILE = "./Model/mnist_dnn_model.json"
    with open(JSON_ARCH_FILE, "w") as json_file:
        json_file.write(json_string)

    if os.path.exists(JSON_ARCH_FILE):
        print("JSON-Model Save OK")

    # yaml 형태로 저장
    yaml_string = model.to_yaml()
    YAML_ARCH_FILE = "./Model/mnist_dnn_model.yaml"
    with open(YAML_ARCH_FILE, "w") as yaml_file:
        yaml_file.write(yaml_string)

    if os.path.exists(YAML_ARCH_FILE):
        print("YAML-Model Save OK")

    # weight 따로 저장 ----------------------------------------------
    WEIGHT_FILE = "./Model/mnist_dnn_weight.h5"
    model.save_weights(WEIGHT_FILE)