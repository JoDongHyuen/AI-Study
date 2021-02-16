# ---------------------------------------
# 저장된 모델(h5) 로딩하여 활용하기
# ---------------------------------------

# 모듈 로딩 ------------------------------------------------------
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import load_model
import numpy as np
import os

import os

MODEL_PATH = "./Model/mnist_dnn_model.h5"

# (1) 데이터 준비 -------------------------------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
y_test = np_utils.to_categorical(y_test)

# 테스트 데이터 임의의 4개 선택
xsample_idx = np.random.choice(x_test.shape[0], 5)
xsample = x_test[xsample_idx]
print(f"xsample_idx = {xsample_idx}, xsample = {xsample}")

# (2) 모델 불러오기 -----------------------------------------------
if not os.path.exists(MODEL_PATH):
    print("해당 모델이 존쟇지 않습니다")
else:
    model = load_model(MODEL_PATH)

    # 모델 사용하기
    ySAM_Label = model.predict_classes(xsample)
    ySAM_Data = model.predict(xsample)

    for i in range(5):
        print(str(np.argmax(y_test[xsample_idx[i]])) + ', predict_classes : ' + str(ySAM_Label[i]))
        print(str(np.argmax(y_test[xsample_idx[i]])) + ', predict : ' + str(ySAM_Data[i]))
        print("")
