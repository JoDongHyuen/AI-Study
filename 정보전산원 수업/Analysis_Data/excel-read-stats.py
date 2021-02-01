import openpyxl

# 변수 선언
filename = r"C:\Users\rhsnf\바탕 화면\stats_104102.xlsx"  # escape문자 그대로 적용시키는 법 => r
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append(([
        row[0].value,
        row[8].value
    ]))

del data[0]
del data[1]
del data[2]

# 정렬
data = sorted(data, key=lambda x: x[1])

# 하위 5개 출력
for i, a in enumerate(data):
    if (i >= 5): break
    print(i + 1, a[0], a[1])
