# 라이브러리 읽어 들이기
import urllib.request as req
import os.path

# URL과 저장 경로 저장하기 ------------------------------------------
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
DIR = "../Image/"
savename = DIR + "google.png"

# 폴더 존재 여부 체크 및 처리 -----------------------------------------
if not os.path.exists(DIR):
    os.mkdir(DIR)

# 다운로드
filename, header = req.urlretrieve(url, savename)
print(f"filename = {filename}")
print(f"header = {header}")
print("다운로드 완료")
