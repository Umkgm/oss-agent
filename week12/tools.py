import pandas as pd
import requests
import json
from secret import API_KEY

BASE_URL = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

def get_box_office_rank1(date):
    '''
    그 날짜의 박스오피스 1위 영화 제목을 알려주는 함수이다.

    받는 것: data - 8자리 문자열로 된 날짜 (예: "20260824")
    돌려주는 것: 1위 영화 제목 (문자열)
    '''
    params = {"key": API_KEY, "targetDt": date}

    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    
    return movies[0]["movieNm"]

def get_movie_audience(date, movie_title):
    """해당 날짜의 박스오피스 목록에서 영화의 일일 관객 수를 반환한다."""
    params = {"key": API_KEY, "targetDt": date}

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == movie_title:
            return f'{int(movie["audiCnt"]):,}명'

    return f"해당 날짜 박스오피스 목록에서 영화를 찾을 수 없습니다: {movie_title}"