import glob, os.path, re, json

def chek_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2}', name).group()
    with open(fname, "r", encoding='utf-8') as f:
        text = f.read()
    text = text.lower()  # 소문자 변환

    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")

    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n - code_a] += 1

    total = sum(cnt)
    freq = list(map(lambda n : n / total, cnt))
    return freq, lang


def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = chek_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs": freqs, "labels": labels}


data = load_files("./DATA/train/*.txt")
test = load_files("./DATA/test/*.txt")

with open("./DATA/freq.json", "w", encoding='utf-8') as fp:
    json.dump([data, test], fp)
