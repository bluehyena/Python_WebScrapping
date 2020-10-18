import requests
import re
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%98%81%ED%99%94")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

for idx, image in enumerate(images):
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url

    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)