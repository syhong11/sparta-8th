variable = 1
test = 'sparta'

# 자바스크립트 변수명: Camel:  spartaCodingClub
# 파이썬 변수명: Snake:      sparta_coding_club

a = "sparta"
a1 = 'sparta'
# a2 = `` X
# let html = `<li></li>`
a2 = """
Sparta Coding Club
"""
# 따옴표 3개 주석 처리 할 때 또는 함수를 설명할 때(문서화)

a = "Hello"
b = "world"
a + b # Helloword

a = "<li>{}</li>{}".format(test, test2)
a1 = "<li>{title}</li>{comment}".format(
    title=test, comment=test1
)

a = 2
a = 1.0
b = 3

a + b # 5
a - b # -1
a * b # 6
a / b # 0.66667

a5 = 3.55
a6 = 4

a5 * a6 # 실수

a7 = 4
a8 = 4
a9 = 4.0

a7 / a8 # 1
a7 / a9 # 1.0

# 문자열 숫자를 정수 / 실수로 바꾸기
a = "10.0"
a = int("10") # 10
a = float("10.0") # 10.0

# Boolen
a = True
b = False

# a = true
# !a ==> false

not a # False
not b # True

# List
a = [1, 'Test', [], True]
a[0] # 1
a[1] # "Test"

# a.length
len(a)

# null, undefined
None # null

# Dictionary 
a = {
    "test10": None,
    'test': 1234,
    'test0': '12345',
    'test01': "12345",
    "test1": True,
    "test2": [],
    "test3": {

    }
}
a["test"] # 1234
a.get("test") 
# 키가 test인 value 찾는데, 만약에 없으면 defaut로 None
a.get("test10") # None
a.get("test10", 1234) # 1234

# 반복문
# for (let i = 0; i = 10; i++) {}

fruits = ['사과','배','감','귤']

for fruit in fruits:
	print(fruit)

# 사과, 배, 감, 귤 하나씩 꺼내어 찍힙니다.

items = ["test1", "test2", "test3", "test4", "test5"]

for index, item in enumerate(items):
    if index > 1:
        break
    print(idex, item)

# 0 test1
# 1 test2
# 2 test3
# 3 test4
# 4 test5

# JS : map, filter, reduce
# Python Comprehension
a = [1, 2, 3, 4, 5]

b = [i * 3 for i in a]
# b = [3, 6, 9, 12, 15]


# 조건문
if a > 1:
    print('test')
elif a > 3:
    print("test3")
else:
    print("test2")
# =============
a = 10
b = 5
if not a >= 10:
    print("test1")
else:
    print("test2")

# && ||
if a > 5 and b > 3:
    print("test1")
else:
    print("test2")

if a > 5 or b > 3:
    print("test1")

# 함수
# function test(response) {}

def test(a, b, c=10):
    print(a, b, c)

test(1, 2)