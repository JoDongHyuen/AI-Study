# --------------------------------------
# Linear Regression - (2) 최소제곱법
# --------------------------------------
# 모듈 로딩 ------------------------------
import matplotlib.pyplot as plt  # 그래프 모듈
import numpy as np

# 데이터 준비 ----------------------------
x = [2, 4, 6, 8, 10]  # 시간 (feature, 데이터)
y = [81, 89, 93, 91, 97]  # 점수 (label, 타겟)

# 전역 변수 선언 -------------------------
mx = np.mean(x)
my = np.mean(y)
print("x 평균값 : ", mx, " y 평균값 : ", my)

# 기울기 공식 => 분자
# (x1 - x 평균) * (y1- y 평균) + .. + (xn - x 평균) * (yn - y 평균)
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

# 기울기 공식 => 분모
# (x 평균 - x1)2 + ... + (x 평균 - xn)2
divisor = sum([(mx - i) ** 2 for i in x])
dividend = top(x, mx, y, my)
print("분모 : ", divisor, " 분자 : ", dividend)

# 기울기와 절편 구하기
w = dividend / divisor
b = my - (mx * w)

# 가설 공식에 x 데이터 적용 후 예측 y2 rkqt cncnf
y2 = [(w*i)+b for i in x]

# 출력으로 확인
print("기울기 w = ", w, " y 절편 b = ", b)
print(f"가설(일차함수) y = {w}x + {b}")


# 그래프로 데이터보기 ---------------------
plt.title(f"y = {w}x + {b}")
plt.plot(x, y, 'ro')
plt.plot(x, y2, "b--")
plt.plot(x, y2, "b^")
plt.xlabel("Hour")
plt.ylabel("Score")
plt.grid()
plt.show()
