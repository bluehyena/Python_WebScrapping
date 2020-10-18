import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 웹툰 전체목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class가 title 인 모든 a element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())