# --------------------------------------
# Scikit - learn SVM - 데이터 분류
# --------------------------------------

from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비 ------------------------------------------
training_points = [[1, 2], [1, 5], [2, 2], [7, 5], [9, 4], [8, 2]]
labels = [1, 1, 1, 0, 0, 0]

one_x = [training_points[:3][i][0] for i in range(3)]
one_y = [training_points[:3][i][1] for i in range(3)]

zero_x = [training_points[3:][i][0] for i in range(3)]
zero_y = [training_points[3:][i][1] for i in range(3)]

# 데이터 시각화 ------------------------------------------

plt.plot(one_x, one_y, "ro")
plt.plot(zero_x, zero_y, "bo")
plt.grid()

# 모델링 ------------------------------------------------
classifier = SVC(kernel='linear')
classifier.fit(training_points, labels)  # 학습

# 학습 후 W, b, Support_Vector 확인 ----------------------
print(f"w => {classifier.coef_}, b => {classifier.intercept_}")
print(f"classifier.support_vectors_ =>\n{classifier.support_vectors_}")

# 임의 데이터 테스트 --------------------------------------
newData = [[3, 4]]
pre_value = classifier.predict(newData)
print(f"pre_value => {pre_value}")

# 결정 경계선과 새로운 데이터 표시
plt.plot(3, 4, 'r^') if pre_value == 1 else plt.plot(3, 4, "b^")

# 결정 경계선 (= 초평면) 그리기
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# linrspace (start, stop, num, endpoint, dtype)
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
print(f"xx => {xx}\nyy = {yy}")

YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = classifier.decision_function(xy).reshape(XX.shape)
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Support Vector 표현
ax.scatter(classifier.support_vectors_[:,0],
           classifier.support_vectors_[:,1],
           s=60, facecolors='y')
plt.show()

