import requests
from bs4 import BeautifulSoup

url = "https://khu.everytime.kr/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title.get_text())