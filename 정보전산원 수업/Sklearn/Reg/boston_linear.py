# --------------------------------------
# 보스턴 집값 데이터
# --------------------------------------

# 모듈 로딩 ----------------------------------------------
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import datasets
import matplotlib.pyplot as plt
# 데이터 준비 ---------------------------------------------
bdata = datasets.load_boston()
x_data = bdata.data
y_data = bdata.target

# 학습용 문제-라벨 & 테스트용 문제 - 라벨 데이터 분리
x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size = 0.3)

print(f"x_train = {len(x_train)}, x_test = {len(x_test)}")

# 모델링 ---------------------------------------------------

# (1) 학습 모델 객체 생성
model = LinearRegression()

# (2) 학습 => 기울기랑 절편 추출
model.fit(x_train, y_train)

# (3) 테스트 y = ax + b <- x_train
y_predict = model.predict(x_test)

# (4) 성능 평가
score = metrics.r2_score(y_test, y_predict)
print(f"r2 score => {score}")

# # 그래프 그리기 ----------------------------------------------
# plt.plot(x_test, y_test)
# plt.grid()
# plt.show()