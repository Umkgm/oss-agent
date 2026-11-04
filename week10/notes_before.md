# week9/tools.py 함수 정리 (수정 전)

## 개요

`week9/tools.py`는 영화진흥위원회(KOBIS) 오픈 API를 사용해 일별 박스오피스 정보를 가져오는 모듈이다.

- 사용 라이브러리: `pandas`, `requests`, `json`
- API 키: `secret.py`의 `API_KEY`를 import 해서 사용
- 요청 주소(`BASE_URL`): KOBIS 일별 박스오피스 조회 API (`searchDailyBoxOfficeList.json`)

## 함수 목록

| 함수 | 입력 | 반환 |
|------|------|------|
| `get_box_office_rank1(date)` | 8자리 날짜 문자열 (예: `"20260824"`) | 그 날짜 박스오피스 1위 영화 제목 (문자열) |

## `get_box_office_rank1(date)`

지정한 날짜의 박스오피스 1위 영화 제목을 돌려준다.

동작 순서:

1. `key`(API 키)와 `targetDt`(날짜)를 요청 파라미터로 만든다.
2. `requests.get`으로 KOBIS API를 호출한다 (timeout 10초).
3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList`(영화 목록)를 꺼낸다.
4. 목록의 첫 번째 영화(1위)의 `movieNm`(영화 제목)을 반환한다.

## 참고 사항

- `pandas`와 `json`은 import 되어 있지만 실제로 사용되지 않는다.
- docstring에는 매개변수 이름이 `data`로 적혀 있지만 실제 이름은 `date`이다.
- 오류 처리가 없다. 네트워크 오류, 잘못된 API 키, 결과가 비어 있는 경우(`movies`가 빈 리스트)에는 예외가 발생한다.
