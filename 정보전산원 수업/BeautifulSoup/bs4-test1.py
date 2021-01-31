# 라이브러리 로딩 --------------------------------------
from bs4 import BeautifulSoup

# 데이터 변수 선언 -------------------------------------
html = '''
<html>
<title> 타이틀입니다. </title>
<body>
<h1 id='h11'>스크레이핑이란?</h1>
<p id='p1'>웹 페이지를 분석하는 것</p>
<p align='center'>원하는 부분을 추출하는 것 </p>
</body></html>
'''

# HTML 분석 ------------------------------------------
# 분석할 HTML 데이터 & 분석기 지정
#   => HTML 태그명으로 계층적 접근 및 추출 가능
soup = BeautifulSoup(html,'html.parser')

# HTML 요소 추출 --------------------------------------
# 태그명으로 원하는 부분 추출, 조금 무식한 방법임..
title = soup.html.title
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# find() 함수를 사용한 검출
h1 = soup.find('h1')  # 태그명으로 찾기
h1_2 = soup.find(id='h11')  # 태그의 id 속성으로 찾기
print(f"h1 => {h1.string}, h1_2 => {h1_2.string}")

p1 = soup.find('p')  # 태그명으로 찾기, 여러개 있으면 첫번째꺼 나옴
p1_2 = soup.find(id='p1')  # 태그의 id 속성으로 찾기
print(f"p1 => {p1.string}, p1_2 => {p1_2.string}")

pall = soup.findAll('p')  # 태그명으로 전부 찾기, 리스트로 반환함
print(f"pall => {pall}, pall[0].string => {pall[0].string}")

# 태그 요소의 글자 출력
print("title = " + title.string)
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)

# 태그 요소의 속성 가져오기
print("p2.attrs = ", p2.attrs)  # 태그 모든 속성 dict 타입
print("p2.attrs['align'] = " + p2.attrs['align'])

