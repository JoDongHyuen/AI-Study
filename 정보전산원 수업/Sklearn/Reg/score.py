# --------------------------------------
# Linear Regression - (1) data 준비
# --------------------------------------
# 모듈 로딩 ------------------------------
import matplotlib.pyplot as plt  # 그래프 모듈

# 데이터 준비 ----------------------------
x = [2, 4, 6, 8, 10]  # 시간 (feature, 데이터)
y = [81, 89, 93, 91, 97]  # 점수 (label, 타겟)

# 그래프로 데이터보기 ---------------------
plt.plot(x, y, 'ro')
plt.xlabel("Hour")
plt.ylabel("Score")
plt.grid()
plt.show()
