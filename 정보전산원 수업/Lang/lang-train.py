import pandas as pd
import joblib
from sklearn import svm, metrics

# 데이터 불러오기
data = pd.read_json("./DATA/freq.json")

train_freqs = data.iloc[0, 0]
train_labels = data.iloc[0, 1]
test_freqs = data.iloc[1, 0]
test_labels = data.iloc[1, 1]

# 모델에 학습시키기
lang = svm.SVC()
lang.fit(train_freqs, train_labels)

# 모델 예측하기
predict = lang.predict(test_freqs)

ac_score = metrics.accuracy_score(test_labels, predict)
if ac_score * 100 > 98:
    savename = "./DATA/lang_model.pkl"
    joblib.dump(lang, savename)
    print("Mode save OK")
