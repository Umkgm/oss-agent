# week9/tools.py 함수 정리

## 개요

`week9/tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스 정보를 가져오는 모듈이다.

- import: `pandas`, `requests`, `json`, `secret.API_KEY`
- 상수 `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소 (`searchDailyBoxOfficeList.json`)

## 함수 목록

이 파일에는 함수가 **1개** 있다.

| 함수 | 입력 | 반환 |
|------|------|------|
| `get_box_office_rank1(date)` | 8자리 날짜 문자열 (예: `"20260824"`) | 그 날짜 박스오피스 1위 영화 제목 (문자열) |

## `get_box_office_rank1(date)`

주어진 날짜의 박스오피스 1위 영화 제목을 돌려준다.

동작 순서:

1. API 키(`key`)와 날짜(`targetDt`)로 요청 파라미터를 만든다.
2. `requests.get`으로 `BASE_URL`에 요청을 보낸다 (timeout 10초).
3. 응답을 JSON으로 바꾼 뒤 `boxOfficeResult` → `dailyBoxOfficeList`에서 영화 목록을 꺼낸다.
4. 목록의 첫 번째 항목(1위)의 `movieNm`(영화 제목)을 반환한다.

사용 예:

```python
from tools import get_box_office_rank1
print(get_box_office_rank1("20260824"))
```

## 참고 사항

- `pandas`와 `json`은 import만 되고 사용되지 않는다.
- docstring에는 매개변수가 `data`라고 적혀 있지만 실제 이름은 `date`이다.
- 오류 처리가 없어서 네트워크 오류, 잘못된 API 키, 빈 결과(`movies`가 빈 리스트)일 때 예외가 발생한다.
- `secret.py`가 없으면 import 단계에서 실패한다.
