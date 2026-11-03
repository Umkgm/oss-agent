# 라이브러리 없이 분류별 평균 점수 구하기 (5주차 2일차)
f = open("scores.csv", encoding="utf-8")
lines = f.readlines()
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

totals = {}
counts = {}
for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue
    c = parts[cat_idx]
    if c not in totals:
        totals[c] = 0
        counts[c] = 0
    totals[c] = totals[c] + score
    counts[c] = counts[c] + 1

for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))
