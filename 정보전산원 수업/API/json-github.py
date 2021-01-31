import urllib.request as req
import os.path, random
import json

# JSON 데이터 내려받기
url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSON 파일 분석하기
items = json.load(open(savename, "r", encoding='utf-8'))

# 출력하기
for item in items:
    print(item["name"] + "-" + item["owner"]["login"])