"""
기본은 언제나 이롭다, 알고 있는거라고 소홀하지 말자
"""


# --------------------------------------------------------------------- #
#  파이썬 함수 살펴보기
#  사용자 정의 함수 : 개발자가 만드는 함수
# --------------------------------------------------------------------- #

# 함수 생성 방법 (1) ----------------------------------------------------- #
# 기 능 : 2 개의 정수 더하기 결과를 반환
# 함수명 : add
# 인 자 : num1, num2
# 결 과 : 더하기한 결과
# --------------------------------------------------------------------- #

def add(num1, num2):
    return num1 + num2


# 함수 사용하기 => 함수 호출
result = add(10, 2)
print(f"result = {result}")
print(f"add(10, 2) = {add(10, 2)}")


# 함수 생성 방법 (2) ----------------------------------------------------- #
# 기 능 : 2 개의 정수 뺀 결과를 반환
# 함수명 : sub
# 인 자 : num1, num2
# 결 과 : 없음
# --------------------------------------------------------------------- #

def sub(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")


sub(12, 3)


# 함수 생성 방법 (3) ----------------------------------------------------- #
# 기 능 : 코드 동작여부 확인용
# 함수명 : check
# 인 자 : 없음
# 결 과 : 없음
# --------------------------------------------------------------------- #

def check():
    print("Testing...")


check()


# 함수 생성 방법 (4) ----------------------------------------------------- #
# 기 능 : 0개 ~ 여러개 정수를 더하기 후 결과 반환
# 함수명 : getSum
# 인 자 : 0개 ~ 여러개 정수
# 결 과 : 더하기 결과
# --------------------------------------------------------------------- #

# 가변인자 활용
def getSum(*datas):
    value = 0
    for i in datas:
        value += i
    return value


print(f"getSum() = {getSum()}")
print(f"getSum(1,3,5) = {getSum(1, 3, 5)}")
print(f"getSum(2,6,8,10,12,14) = {getSum(2, 6, 8, 10, 12, 14)}")

# 1 ~ 100까지 더하기
data = list(range(1, 101))
# print(f"getSum(1 ~ 100) = {getSum(data)}")  # data는 리스트 타입이라 에러가남
print(f"getSum(1 ~ 100) = {getSum(*data)}")  # *data는 리스트를 unpacking 해준다는 뜻임


# 함수 생성 방법 (5) ----------------------------------------------------- #
# 기 능 : 0개 ~ 여러개 정수를 더하기 후 결과 반환
# 함수명 : getMaxMin
# 인 자 : 0개 ~ 여러개 정수
# 결 과 : 최대값, 최소값
# --------------------------------------------------------------------- #

def getMaxMin(*datas):
    return max(datas), min(datas)  # 튜플로 반환됨


_max, _min = getMaxMin(1, 5, 2, 3, 7246, 1, 325, 325)
print(f"_max = {_max}, _min = {_min}")

_maxmin = getMaxMin(2, -3, 4, 10, 0)
print(f"_maxmin = {_maxmin}")


# 함수 생성 방법 (6) ----------------------------------------------------- #
# 기 능 : 0개 ~ 여러개 아이디와 비밀번호 처리
# 함수명 : setIDPW
# 인 자 : 0개 ~ 여러개 아이디와 비밀번호 처리
# 결 과 : 없음
# --------------------------------------------------------------------- #


def setIDPW(**idpw):
    print(idpw, type(idpw))


setIDPW(id1="a123", id2='Jo', id3="spring")

tdata = {'name': 'jdh', 'age': 25}
setIDPW(**tdata)  # dict 데이터를 언패킹하여 전달

# 함수 생성 방법 (7) ----------------------------------------------------- #
# 기 능 : 2개 정수 더하기 후 결과 반환
# 함수명 : 없음
# 인 자 : 2개 정수
# 결 과 : 더하기 결과
# --------------------------------------------------------------------- #

data = [1, 3, 5, 7, 9]
data2 = list(map(lambda x: x + x, data))
print(data2)

# --------------------------------------------------------------------- #
# map 함수에 대해서

data = ['1', '2', '3', '4']
for idx in range(len(data)):
    data[idx] = int(data[idx])
print(data)

data2 = ['1', '2', '3', '4']
data2 = list(map(int, data2))
print(data2)


print(f"__name__ = {__name__}")
