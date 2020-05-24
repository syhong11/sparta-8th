from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화제목이 매트릭스인 영화의 평점 표시
metrics_movie = list(db.movies.find({'title': '매트릭스'}))
metrics_star = metrics_movie[0]["star"]
print(metrics_star)

# 매트릭스 평점과 같은 영화 가져오기
same_movies = list(db.movies.find({'star': metrics_star}))
for movie in same_movies:
    movie_title = movie["title"]
    print(movie_title)

# 0으로 만들기
db.movies.update_many(
    {'star': metrics_star},
    {'$set': {'star' : 0}}
)