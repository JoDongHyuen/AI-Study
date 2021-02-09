# 모듈 세팅
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd

# 데이터 세팅
FILE_PATH = "./DATA/mushroom.csv"
data = pd.read_csv(FILE_PATH, header=None)
# 받아온 데이터를 atoi 처리해줌
data = data.applymap(lambda x: ord(x))

# label과 feature 분리
labels = data.iloc[:, 0]
feature = data.iloc[:, 1:]

# 훈련 데이터와 평가 데이터 나누기
train_feature, test_feature, train_label, test_label = train_test_split(feature, labels)

# 모델 훈련
model = RandomForestClassifier()
model.fit(train_feature, train_label)

# 모델 예측
predict = model.predict(test_feature)

# 모델 평가
ac_score = metrics.accuracy_score(test_label, predict)

print(ac_score)