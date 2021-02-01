import codecs
import csv

# EUC_KR로 저장된 CSV 파일 읽기
DIR = "../Data/"
filename = DIR + "list-euckr.csv"
filename2 = DIR + "list-euckr2.csv"
csv1 = codecs.open(filename, "r", "utf-8").read()

# CSV을 파이썬 리스트로 변환하기
data = []
rows = csv1.split("\r\n")
for row in rows:
    if row == "":
        continue
    cells = row.split(",")
    data.append(cells)

# 결과 출력하기
for c in data:
    print(c[1], c[2])

with codecs.open(filename2, "w", "utf=8") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "SD 카드", "30000"])
    writer.writerow(["1001", "키보드", "21000"])
    writer.writerow(["1002", "마우스", "15000"])