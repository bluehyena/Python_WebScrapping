import requests
import csv
import env
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search = input("검색어를 입력하세요 :")

url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJg8yk6r7sAhUEA4gKHUI8ChoQ_AUoA3oECAsQBQ&biw=929&bih=886".format(str(search))
headers = {"User-Agent":env.User_Agent, "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"rg_i Q4LuWd"})
for idx, image in enumerate(images):
    print(image["src"])

# url = "https://www.google.com/"
# headers = {"User-Agent":env.User_Agent, "Accept-Language":"ko-KR,ko"}

# search = input("검색어를 입력하세요 : ")
# # image_num = int(input("저장할 이미지 갯수를 입력하세요 : "))

# browser = webdriver.Chrome()
# # browser.maximize_window()
# browser.get(url)

# google_search = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
# google_search.send_keys(search)
# google_search.send_keys(Keys.ENTER)

# try:
#     image_search = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "이미지")))
#     image_search.click()
# finally:
#     browser.quit()

