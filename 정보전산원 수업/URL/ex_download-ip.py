# 텍스트기반 파일 다운로드하기
# 라이브러리 로딩
import urllib.request as req
import os.path

# 데이터 변수 선언
url = "http://api.aoikujira.com/ip/ini"
DIR = "../Data/"
savename = DIR + "ini.txt"

# 데이터 저장 폴더 체크
if not os.path.exists(DIR):
    os.mkdir(DIR)

# 웹에서 데이터 가져오기
resObj = req.urlopen(url)  # response 객체를 가져옴
data = resObj.read()  # response 객체에서 데이터만 읽기
text = data.decode('utf-8')  # 바이너리 데이터 사람이 읽을 수 있도록 변환

with open(savename, mode='w', encoding='utf-8') as file:
    file.write(text)