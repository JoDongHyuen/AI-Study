import pandas as pd
from sklearn.svm import SVC

# XOR
xor_input = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]

# 데이터 분류
xor_df = pd.DataFrame(xor_input)
# print(xor_df)
xor_data = xor_df.iloc[:, 0:2]
# print(xor_data)
xor_label = xor_df.iloc[:, 2]
# print(xor_label)

# 데이터 학습과 예측하기
clf = SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
