# --------------------------------------------------------------------- #
#  URL 파싱(분석)
#  URL 구성 = 6개 요소 ( scheme host port path query fragment)
# --------------------------------------------------------------------- #
from urllib.parse import urlparse, urlsplit, urlencode

# URL 주소 분석 후 6가지 데이터 반환
data = urlparse("https://lms.knu.ac.kr/ilos/main/member/login_form.acl?id=rhsnfl1122&paswword:helloworld")
print(f"data => {data}")
print(f"data.scheme => {data.scheme}")  # 프로토콜
print(f"data.netloc => {data.netloc}")  # 네트워크 위치
print(f"data.path => {data.path}")  # 경로
print(f"data.params => {data.params}")
print(f"data.query => {data.query}")
print(f"data.fragment => {data.fragment}")

# URL 분석 데이터를 나누어서 튜플로 반환
data2 = urlsplit("https://lms.knu.ac.kr/ilos/main/member/login_form.acl?id=rhsnfl1122&paswword:helloworld")
print(f"data2 = {data2}")

# URL Query 를 Encoding : % Encoding 이라고도 함
# 알파벳, 숫자 등 몇몇 문자 ASCII 제외 나머지
# 1 바이트 단위 묶어서 16진수 인코딩
# dict 타입을 넣어야함
url = urlencode({'name':'조동현'})
print(url)
