import joblib
from sklearn import model_selection, svm, metrics
import pandas as pd

# CSV 파일을 읽어 들이고 가공하기
# def load_csv(fname):
#     labels = []
#     images = []
#     df = pd.read_csv(fname, header=None)
#     label = df.iloc[:, 0]
#     data = df.iloc[:, 1:]
#     data = data / 256
#     print(data)
#     labels.append(label.items)

#
# load_csv("../Data/train.csv")
# load_csv("../Data/t10k.csv")

# 학습 및 테스트용 데이터 로딩
data = pd.read_csv("../Data/train.csv", header=None)
test = pd.read_csv("../Data/t10k.csv", header=None)

train_data = data.iloc[:, 1:] / 256
train_label = data.iloc[:, 0]

test_data = test.iloc[:, 1:] / 256
test_label = test.iloc[:, 0]

# 학습하기
clf = svm.SVC()
clf.fit(train_data, train_label)

# 예측하기
predict = clf.predict(test_data)

# 결과 확인하기
ac_score = metrics.accuracy_score(test_label, predict)
cl_report = metrics.classification_report(test_label, predict)
print("정답률 = ", ac_score)
print("리포트 = ")
print(cl_report)

# 학습 데이터 저장
if ac_score * 100 >= 96:
    savefile = "../Data/handdigit.pkl"

    # 모델 저장하여 파일로 생성
    joblib.dump(clf, savefile)
    print("Model Save OK")
