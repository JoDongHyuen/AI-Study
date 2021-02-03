# --------------------------------------
# 보스턴 집값 데이터
# --------------------------------------

from sklearn.datasets import load_boston  # 함수 1개만 로딩

# 데이터 준비 ---------------------------------------------
bdata = load_boston()
feature = bdata.data  # 데이터(피처) 13개
target = bdata.target  # 라벨(정답 타겟) 1개

print(f"type(bdata) => {type(bdata)}")
print(f"dir(bdata) => {dir(bdata)}")
print(f"bdata.feature_names => {bdata.feature_names}")
# print(f"bdata.DESCR => {bdata.DESCR}")

