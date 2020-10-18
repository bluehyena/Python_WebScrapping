import re
import env

# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")

print(env.User_Agent)

# . (ca.e) : 하나의 문자를 의미 > care, cafe | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (x)
# $ (se$) : 문자열의 끝 > case, base | face (x)

def print_match(m):
    if m:
        print("m.group():", m.group()) #일치하는 문자열반환
        print("m.string():", m.string) #입력받은 문자열
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열 시작/끝 index
    else:
        print("매칭 x")

# m = p.match("careless")

# print(m.group()) # 매치 x 시 에러발생

# print_match(m)

#m = p.search("careless") # search : 주어진 문자열 중 일치하는게 있는지 확인.
#print_match(m)


#lst = p.findall("careless, goodcare cafe")  # find all: 일치하는 모든 것들을 리스트로 반환
#print(lst)

#1. p = re.compile("원하는 형태")
#2. m = p.match("비교할 문자열") : 처음부터 주어진문자열이 일치하는지 확인
#3. m = p.search("비교할 문자열") : 주어진 문자열중 일치하는게 있는지 확인
#4. lst = p.findall("비교할 문자열") : 일치하는 모든 것들을 리스트로 반환
