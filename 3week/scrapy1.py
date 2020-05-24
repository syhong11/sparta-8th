# 웹 스크래밍 = 웹 크롤링
# 웹 사이트 정도를 긁어오는 기술
# - bs4: (beautifulsoup4) -> HTML 파싱을 편리하게.
# - requests -> 브라우저에서 엔터를 치는 효과. URL에 요청하기

import requests
from bs4 import BeautifulSoup

# 크롤링 : 데이터를 훔치는 작업
# 크롤링 > 창 vs 방패
# 요청을 날리는 걸 웹 브라우저가 날리는 것처럼 속이는 작업

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

# for movie in movies:
#     a_tag = movie.select_one('td.title > div > a')

#     if a_tag is not None:
#         print(a_tag.text)

# select : 결과값이 항상 리스트
# select : 결과값이 항상 html 태그

for movie in movies:
    title_tag = movie.select_one('td.title > div > a')
    rate_tag = movie.select_one('td.point')
    rank_tag = movie.select_one('td.ac > img')

    if title_tag is not None and rate_tag is not None and rank_tag is not None:
        title = title_tag.text
        rate = rate_tag.text
        rank = rank_tag["alt"]

        print(rank, title, rate)