from bs4 import BeautifulSoup as bs
import urllib.request as req

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
url2 = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

# 데이터 가져오기 urlopen()
res = req.urlopen(url)
res2 = req.urlopen(url2)

# 데이터 분석하기
soup = bs(res, "html.parser")
soup2 = bs(res2, "html.parser")

movie = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
print("movie.attres['title] = ", movie.attrs['title'])
print("movie = ", movie.string)

# 영화 순위 뽑아내기 --------------------------------------------------------------------------

movielist = soup.select("div[class=tit3]")
#movielist = soup.select("#old_content > table > tbody > tr > td.title > div > a")
print(movielist[0])

for i in range(0, 50):
    print(f"movie Rank {i + 1} = {movielist[i].string}")

# for idx, item in enumerate(movielist, start=1):
#     print(idx, item.string)

# 환율 뽑아내기 ------------------------------------------------------------------------------

usd = soup2.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
print(usd.string)