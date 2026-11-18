# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
박스오피스 조회

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
Python, requests, pandas, 그리고 week12 폴더의 tools.py와 secret.py가 있어야 함

## 설치
boxoffice 폴더를 week12 폴더의 .claude/skills/ 아래에 둠

## 바깥으로 요청하는 곳
https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json, 보내는 값: API 키, 조회 날짜

## 키
이 저장소와 파일에는 키가 없으므로 secret.py에 넣는다

## 권한
boxoffice.py를 실행할 때마다 물어봄

## 라이선스
MIT License 파일위치:.claude/skills/boxoffice/LICENSE.txt
