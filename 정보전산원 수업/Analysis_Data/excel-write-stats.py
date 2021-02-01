import csv
import openpyxl

filename =r"C:\Users\rhsnf\바탕 화면\stats_104102.xlsx"
book = openpyxl.load_workbook(filename)
# print(book)

sheet = book.active
#print(sheet)

for i in range(0, 9):
    total = int(sheet[str(chr(i + 66)) + "3"].value)  # chr함수는 특정 값을 주면 ASCII로 반환해줌
    # print(total)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    # print(seoul)
    output = total - seoul
    print("서울 제외 인구 : ", output)

    sheet[str(chr(i + 66)) + "21"] = output

filename = "population.xlsx"
book.save(filename)
