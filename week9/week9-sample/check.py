# 분류별 평균 점수를 계산해서 출력한다.

f = open("scores.csv", encoding="utf-8")
lines = f.readlines()
f.close()

for line in lines[1:]:
    name, category, score = line.strip().split(",")
    if score == "":
        print(name, "점수 없음")
    elif not score.isdigit():
        print(name, "숫자가 아님:", score)
