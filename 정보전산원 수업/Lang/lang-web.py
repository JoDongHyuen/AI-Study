# ------------------------------------------------------------------------
# 웹 브라우저를 통한 언어 판별 프로그램
# URL을 통해서 접속 & 데이터 입력 & 검사 & 결과처리
# (1) SERVER 구동 : pytoh -m http.server --cgi 8080 (터미널에서 실행)
# (2) URL : http://localhost:8080/cgi-bin/lang_web.py (웹 브라우져에서 실행)
#  -----------------------------------------------------------------------

import cgi, os.path
import joblib, codecs, sys

# 표준 출력 인코딩 설정
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

pklfile = os.path.dirname(__file__) + "/lang_model.pkl"
clf = joblib.load(pklfile)


# 텍스트 입력 양식 출력하기
def show_form(text, msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
        <html><body><form>
        <textarea name="text" rows = "8" cols = "40">{0}</textarea>
        <p><input type="submit" value="판정"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(cgi.html.escape(text), msg))


# 판정하기
def detect_lang(text):
    text = text.lower()
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26:
            cnt[n] += 1
    total = sum(cnt)

    if total == 0:
        return "입력이 없습니다"
    freq = list(map(lambda n: n / total, cnt))
    # 언어 예측하기
    res = clf.predict([freq])
    # 언어 코드를 한국어로 변환하기
    lang_dic = {"en": "영어", "fr": "프랑스어", "id": "인도네시아어", "tl": "티갈로그어"}
    return lang_dic[res[0]]


# 입력 양식의 값 읽어 들이기

form = cgi.FieldStorage()
text = form.getvalue("text", default="")
msg = ""
if text != "":
    lang = detect_lang(text)
    msg = "판정 결과:" + lang

show_form(text, msg)
