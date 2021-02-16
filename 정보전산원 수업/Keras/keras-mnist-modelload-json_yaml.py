# ---------------------------------------
# JSON & YAML 모델 아키텍쳐 + Weight + compile() => 모델 재구성
# ---------------------------------------

# 모듈 로딩 ------------------------------------------------------
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import model_from_json
import numpy as np

import os


MODEL_PATH = "./Model/mnist_dnn_model.h5"
JSON_ARCH_FILE = "./Model/mnist_dnn_model.json"
YAML_ARCH_FILE = "./Model/mnist_dnn_model.yaml"
WEIGHT_FILE = "./Model/mnist_dnn_weight.h5"

# (1) 데이터 준비 -------------------------------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
y_test = np_utils.to_categorical(y_test)

# 테스트 데이터 임의의 4개 선택
xsample_idx = np.random.choice(x_test.shape[0], 5)
xsample = x_test[xsample_idx]
print(f"xsample_idx = {xsample_idx}, xsample = {xsample}")

# (2) 모델 불러오기 -----------------------------------------------
if not os.path.exists(JSON_ARCH_FILE):
    print("해당 모델이 존재하지 않습니다")
else:
    # 1.json 모델 아키텍처 재구성
    with open(JSON_ARCH_FILE, "r") as json_file:
        loaded_model_json = json_file.read()
    json_model = model_from_json(loaded_model_json)

    # 2.로드한 model에 weight 로드
    json_model.load_weights(WEIGHT_FILE)
    print("Loaded complete")

    # 3.모델 컴파일
    json_model.compile(loss='categorical_crossentropy',
                       optimizer='adam',
                       metrics=['accuracy'])

    # 모델 사용하기
    ySAM_Label = json_model.predict_classes(xsample)
    ySAM_Data = json_model.predict(xsample)

    for i in range(5):
        print(str(np.argmax(y_test[xsample_idx[i]])) + ', predict_classes : ' + str(ySAM_Label[i]))
        print(str(np.argmax(y_test[xsample_idx[i]])) + ', predict : ' + str(ySAM_Data[i]))
        print("")
