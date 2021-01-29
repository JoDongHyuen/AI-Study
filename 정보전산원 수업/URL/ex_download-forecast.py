# 모듈 로딩
import urllib.request as req
import urllib.parse
import os.path

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
DIR = "../Data/"
savename = DIR + "forecast.txt"
savename2 = DIR + "forecast2.txt"

if not os.path.exists(DIR):
    os.mkdir(DIR)

# 매개변수 encoding
values = {
    'stnID' : '108'
}

params = urllib.parse.urlencode(values)
url = API + "?" + params

resObj = req.urlopen(url)  # HTTP response 타입으로 리턴
data = resObj.read()
text = data.decode("utf-8")

# utf-8 인코딩해서 저장
with open(savename, mode='w', encoding='utf-8') as file:
    file.write(text)

# 바이너리로 저장
with open(savename2, mode='wb') as file:
    file.write(data)
