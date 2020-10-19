import requests
import env

url = "http://www.naver.com"
headers = {"User-Agent":env.User_Agent}
res = requests.get(url, headers = headers)
res.raise_for_status()
with open("naver.html", "w", encoding="utf8") as f:
    f.write(res.text)

