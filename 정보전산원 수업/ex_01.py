"""
기본은 언제나 이롭다.
"""

'''
파이썬 기본 데이터 타입

1. 기본 자료형 ---- 숫자 ---- 정수 실수 복소수  
            ㄴ---- 문자열
            ㄴ---- 논리형
            ㄴ---- 바이트
            
2. 컬렉션 자료형 ---- 순서자료형 --- list, tuple, str
            ㄴ----- 맵핑자료형 -- dict
            ㄴ----- 집합자료형 --- set
'''

# 기본 데이터 타입 출력
print(10, type(10))
print(3.45, type(3.45))
print('good', "good", type('good'))
print(True, type(True))

# --------------------------------------------------------------------- #

'''
데이터 타입 변환
'''

# 정수로 변환하기 -> int (다른 데이토 타입)
print(10.45, type(10.45), int(10.45), type(int(10.45)))
print('10', type('10'), int('10'), type(int('10')))
# print('10%', type('10%'), int('10%'), type(int('10%')))

# --------------------------------------------------------------------- #

'''
str 타입 객체
'''

# str 타입 객체 생성 방법

data1 = 'Happy'
data2 = "Happy"
data3 = '''
Good Luck
Your Best
'''

print(data1, data2, data3)

# 인덱스(Index) 파이썬에서 자동으루 부여하는 번호, 왼쪽에서 오른쪽은 0부터 , 오른쪽에서 왼쪽은 -1부터 시작함
# 요소(원소) 접근 방법 : [인덱스

print(data1[0], data2[1], data3[-2])  # 인덱싱
print(data1, data1[0:2], data1[:2], data1[2:])  # 슬라이싱

# 데이터 일부 변경
# data1[0] = 'h' # 바꾸기 불가능..!
print(data1)

# --------------------------------------------------------------------- #

'''
str 클래스 메서드 사용
'''

msg = 'moring'
msg.find('m')  # 해당 문자 / 문자열 시작 인덱스 반환
msg.index('ing')  # 해당 문자 / 문자열 시작 인덱스 반환, 존재하지 않으면 ERROR 반환

msg = "Happy,New,Year"
print(msg.split(','))  # 기본 공백으로 문자열 나누기 => 리스트로 반환
print("*".join(msg))  # 해당 문자열에 지정된 문자 삽입

print(msg.upper(), "\n", msg.lower(), "\n", msg, "\n")  # 대문자, 소문자 변환

# --------------------------------------------------------------------- #
# 시퀸스(순서)가 있는 데이터 타입
# - 컬렉션 타입으로 기본 데이터를 여러개 저장하는 타입
# - 인덱싱, 슬라이싱
# --------------------------------------------------------------------- #

'''
 (1) class 'list' 타입
 [데이터, 데이터, ... , 데이터]
'''
data = [10, 3.45, False, "Happy"]

# 인덱싱
print(f"{data} , type => {type(data)}")
print(f"data[0] = {data[0]}")
print(f"data[-1] = {data[-1]}")
print("\n")

# 슬라이싱
print(f"data[0:2] = {data[0:2]}")
print(f"data[1:-1] = {data[1:-1]}")
print("\n")

# 데이터 변경
data[0] = "TEN"
print(f"data = {data}")
print("\n")

data[:3] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"data = {data}")
print("\n")

data[:3] = [0]
print(f"data = {data}")
print("\n")

'''
파이썬 내장 함수
'''

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 데이터 길이 갯수 구하기 => len()
print(f"data Len => {len(data)}")

# 데이터 합계 구하기 => sum()
print(f"data sum => {sum(data)}")

# 데이터 최대값, 최소값 구하기 => max(), min()
print(f"data max => {max(data)}, min => {min(data)}")

# class 'list' 메서드 살펴보기
my_data = []  # 빈 리스트 객체 생성

# 빈 리스트에 데이터 넣기, 이미 존재하는 인덱스 값 변경하는 것과 헷갈리지 말기
# my_data[0] = 10  # 이러면 추가 안됨
my_data.append(10)
print(f"my_data => {my_data}")
my_data.append("A")
my_data.append(False)
print(f"my_data => {my_data}")

my_data.insert(1, 20)  # 지정 인덱스에 데이터 삽입
print(f"my_data => {my_data}")

# 정렬 X, 역순(거꾸로)으로 변경
my_data.reverse()
print(f"my_data => {my_data}")

# 정렬 sort() : 디폴트는 오름차순 정렬
my_data = [3, 5, 3, 4, 6, 10]
my_data.sort()
print(f"my_data => {my_data}")
my_data.sort(reverse=True)
print(f"my_data => {my_data}")

'''
 (2) class 'tuple' 타입
 (데이터, 데이터, ... , 데이터)
 인자가 하나인 경우에는 data = (1,) 이런 식으로 정해주어야 함
'''

data = (1, 11, 21, 31, 41)
data2 = (1)  # 이러면 인트 타입으로 들어감
data3 = (1,)

print(f"type(data) = {type(data)}")
print(f"type(data2) = {type(data2)}")
print(f"type(data3) = {type(data3)}")

# 인덱싱, 슬라이싱
print(f"data[2] = {data[2]}")
print(f"data[2:] = {data[2:]}")

# 원소 변경
# data[0] = 2021  # 변경 못함..!

'''
 (3) class 'range' 타입
 지정된 범위를 나타내는 객체
 range(start, end, step) start부터 end까지 end는 포함하지 않고 step만큼 증가함
'''

rdata = range(10)  # 0~9 범위의 range 객체
print(f"rdata = {rdata}")

rdata2 = range(1, 10)  # 1 ~ 9 범위의 range 객체
print(f"rdata2 = {rdata2}")

rdata3 = range(1, 10, 2)  # 1 ~ 9 범위의 2step 으로 증가
print(f"rdata3 = {rdata3}")

# ldata = [range(1, 1001)]  # 이렇게하면 range타입 객체가 list의 하나의 요소로 들어감
ldata = list(range(1, 1001))
print(ldata[999])

# --------------------------------------------------------------------- #
#  Mapping Type : 데이터 의미 : 데이터를 쌍으로 저장하는 방식
#                   key : value 형태
# --------------------------------------------------------------------- #

# class 'dict' 타입 객체 생성
data = {'id': '1234', 'name': 'Jo', 'age': '25'}
data2 = {1: 10, 2: "TEST", 3.5: "Value", 'pw': 111, 2: 222}

print(f"data = {type(data)}, {data}")
print(f"data2 = {type(data2)}, {data2}")

# 요소 (원소) 데이터 읽기
print(f"data['id'] => {data['id']}")
print(f"data2['3.5'] => {data2[3.5]}")

# 요소 (원소) 데이터 변경
data['id'] = "HappyNew"  # 변경가능
data['birth'] = "1225"  # 없는 키는 추가함
print(f"data = {type(data)}, {data}")

# class 'dict' 메서드
data.keys()  # dict의 key 값들을 반환
print(f"data.keys() = {type(data.keys())}, {data.keys()}")
print(f"data.values() = {type(data.values())}, {data.values()}")
print(f"data.items() = {type(data.items())}, {data.items()}")

# 전역 변수(Global Variable) : python 파일 안에서 선언된 변수
#                            python 파일 안에서 어디서나 사용 가능함

# 지역 변수 (Local Variable) : 함수 안에서 선언된 함수
#                            함수 안에서만 사용 가능

count = 10

print(f"count = {count}")


# 사용자 정의 함수
def display():
    count = 12
    print(f"display() : count = {count}")


display()
print(f"count = {count}")
