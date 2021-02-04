# 모듈 로딩
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import urllib.request as req
import os.path

# 데이터 준비
DIR = "../Data/"
filename = DIR + "iris.csv"

if not os.path.exists(DIR):
    os.mkdir(DIR)

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
if not os.path.exists(filename):
    req.urlretrieve(url, filename)

# 데이터 읽어듥이기
with open(filename, "r", encoding='utf-8') as fp:
    iris_data = fp.read()

iris_df = pd.read_csv(filename)
iris_feature = iris_df.iloc[:, 0:4]
iris_label = iris_df.iloc[:, 4]

train_feature, test_feature, train_label, test_label = train_test_split(iris_feature, iris_label)

# 모델 학습 시키기
iris_model = SVC()
iris_model.fit(train_feature, train_label)

# 모델 예측시키기
predict = iris_model.predict(test_feature)

test_label_list = test_label.tolist()
print(test_label_list)

ok = 0
fail = 0
for i in range(len(predict)):
    print(f"{predict[i]} == {test_label_list[i]} ?")
