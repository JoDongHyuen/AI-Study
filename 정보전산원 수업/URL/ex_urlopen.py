# 라이브러리 읽어 들이기
import urllib.request as req
import os.path

# URL 과 저장 경로 저장하기 ------------------------------------------
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
DIR = "../Image/"
savename = DIR + "google.png"

# 폴더 존재 여부 체크
if not os.path.exists(DIR):
    os.mkdir(DIR)

# HTTP Response 객체 반환 -> byte 데이터
resObj = req.urlopen(url)

'''
about class HTTPResponse

attribute : header, data
method : 
'''

# HTTP Response 에서 정보 읽어오기
header = resObj.getheaders()
data = resObj.read()

print("type(resObj) => ", type(resObj))
print("resObj.getheader() => \n", header)
print("resObj.read() => \n", data)

# 바이너리 데이터 => 문자열 변환
# text = data.decode("utf-8")  # 사람이 알아볼 수 있도록 변환
# print(f"text => {text}")
# 그림이라서 변환은 안됨

# 바이너리라서 모드에 b를 붙여줘야함, raw data 로 저장하는 방식임
with open(savename, mode='wb') as file:
    file.write(data)

print("저장!") if os.path.exists(savename) else print("저장 실패!")
