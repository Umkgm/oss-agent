작성: Claude Code / 확인: (이름)

# week9/tools.py 함수 정리

## 개요

- 영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스 정보를 가져오는 모듈임
- 사용 라이브러리: `pandas`, `requests`, `json`
- API 키: `secret.py`의 `API_KEY`를 import 해서 사용함
- 요청 주소(`BASE_URL`): KOBIS 일별 박스오피스 조회 API (`searchDailyBoxOfficeList.json`)

## 함수 목록

| 함수 | 입력 | 반환 |
|------|------|------|
| `get_box_office_rank1(date)` | 8자리 날짜 문자열 (예: `"20260824"`) | 그 날짜 박스오피스 1위 영화 제목 (문자열) |

## `get_box_office_rank1(date)`

- 지정한 날짜의 박스오피스 1위 영화 제목을 돌려주는 함수임
- 동작 순서
  1. `key`(API 키)와 `targetDt`(날짜)로 요청 파라미터를 만듦
  2. `requests.get`으로 KOBIS API를 호출함 (timeout 10초)
  3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList`(영화 목록)를 꺼냄
  4. 목록의 첫 번째 영화(1위)의 `movieNm`(영화 제목)을 반환함

```python
def get_box_office_rank1(date):
    # 그 날짜의 박스오피스 1위 영화 제목을 돌려주는 함수
    # 받는 것: date - 8자리 문자열 날짜 (예: "20260824")
    # 돌려주는 것: 1위 영화 제목 (문자열)
    params = {"key": API_KEY, "targetDt": date}            # API 키와 조회 날짜를 요청 파라미터로 구성
    response = requests.get(BASE_URL, params=params, timeout=10)  # KOBIS API 호출 (10초 제한)
    data = response.json()                                 # 응답을 JSON(dict)으로 변환
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"] # 일별 박스오피스 영화 목록 추출
    return movies[0]["movieNm"]                            # 1위 영화 제목 반환
```

## 참고 사항

- `pandas`, `json`은 import 되어 있으나 실제로 사용되지 않음
- docstring의 매개변수 이름이 `data`로 적혀 있으나 실제 이름은 `date`임
- 오류 처리가 없음
  - 네트워크 오류, 잘못된 API 키, 결과가 빈 경우(`movies`가 빈 리스트)에 예외가 발생함
