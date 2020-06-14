from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.schoolzonedb                    # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에서 데이터 모두 보기
# all_school = list(db.school.find())
# school = db.school.find_one({'Latitude':36.39605089})
# print(school)
some_key_school = list(db.school.find({'Type':'어린이집'}, {'_id': False}))
print(some_key_school)

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
# same_ages = list(db.users.find({'age':21}))

# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# for school in all_school:      # 반복문을 돌며 모든 결과값을 보기
#     print(school)