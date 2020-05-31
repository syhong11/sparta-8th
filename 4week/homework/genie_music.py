
# 1. 지니 뮤직에 있는 노래 1~50위 곡 크롤링
# https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# MongoDB에 연결하기
client = MongoClient('localhost', 27017)
# MongoDB의 Database에 접속
db = client.dbsparta

# requests 로 HTML 파일을 불러오기
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',
    headers=headers
)
soup = BeautifulSoup(data.text, 'html.parser')

# musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
musics = soup.select('.music-list-wrap > table > tbody > tr')

for music in musics:
     title_tag = music.select_one('td.info > a.title')
     artist_tag = music.select_one('td.info > a.artist')
     rank_tag = music.select_one('td.number')

     title = title_tag.text
     title = title.lstrip()

     artist = artist_tag.text

     rank = rank_tag.find(text=True, recursive=False)
     rank = rank.rstrip()

     print(rank, title, artist)

     # 실행 시 매번 동일한 데이터 저장됨
    #  db.genie.insert_one({
    #      'rank' : rank,
    #      'title' :  title,
    #      'artist' : artist
    #  })


    # title_tag = music.find('td', {'class': 'info'}).find('a', {'class' : 'title ellipsis'})
    # artist_tag = music.find('td', {'class': 'info'}).find('a', {'class' : 'artist ellipsis'})
    # rank_tag = music.select_one('td.number')
    # rank_tag = music.find('td', {'class': 'number'})
    

    # if title_tag is not None and artist_tag is not None and rank_tag is not None:
    #     title = title_tag.text
    #     artist = artist_tag.text
    #     rank = rank_tag.find(text=True, recursive=False)

        # print(rank.strip(), title.strip(), artist)
        # print(rank[0]+rank[1].strip(), title.strip(), artist)