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