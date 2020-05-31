import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',
    headers=headers
)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    title_tag = music.find('td', {'class': 'info'}).find('a', {'class' : 'title ellipsis'})
    artist_tag = music.find('td', {'class': 'info'}).find('a', {'class' : 'artist ellipsis'})
    rank_tag = music.select_one('td.number')
    # rank_tag = music.find('td', {'class': 'number'})
    

    if title_tag is not None and artist_tag is not None and rank_tag is not None:
        title = title_tag.text
        artist = artist_tag.text
        rank = rank_tag.text

        print(rank[0] + rank[1].strip(), title.strip(), artist)