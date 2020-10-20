# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만들어라.

# [조회조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ======== 매물 1 =========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# ========= 매물 2 =========
# .....

# [주의사항]
# - 실습시점에 위 매물이 없다면 다른 곳으로 대체 가능

import requests
import time
import env

from bs4 import BeautifulSoup

headers = {"User-Agent":env.User_Agent}

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("=========== 매물 {} ==========".format(index+1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text(), "(공급/전용)")
    print("가격 :", columns[2].get_text(), "(만원)")
    print("동 :", columns[3].get_text())
    print("층 :", columns[4].get_text())