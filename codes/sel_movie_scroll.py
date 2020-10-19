from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

# Move to page
url = "https://play.google.com/store/movies/top"
browser.get(url)

# Scroll Down
# 해상도 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920*1080
# browser.execute_script("window.scrollTo(0, 2080)")

#Scroll Down to Bottom
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("Scroll Complete")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인된 영화만 필터링
    original_price = movie.find("span", attrs={"class":"SUZt4c djCUy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <할인되지 않은 영화 제외> ")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"})

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    #올바른 링크 : https://play.google.com + link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()