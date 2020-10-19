import requests
# import csv
import env
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrolldown(interval : int, web_driver : webdriver) -> None:
    assert isinstance(interval, int)
    assert isinstance(browser, webdriver.Chrome)

    prev_height = web_driver.execute_script("return document.body.scrollHeight")
    while True:
        web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(interval)
        curr_height = web_driver.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break
        prev_height = curr_height

search = input("검색어를 입력하세요 :")

url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJg8yk6r7sAhUEA4gKHUI8ChoQ_AUoA3oECAsQBQ&biw=929&bih=886".format(str(search))

# image_num = int(input("저장할 이미지 갯수를 입력하세요 : "))

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get(url)

scrolldown(2, browser)
more_result = browser.find_element_by_xpath("//*[@id='islmp']/div/div/div/div/div[5]/input")
more_result.click()
scrolldown(2, browser)

soup = BeautifulSoup(browser.page_source, "lxml")

images = soup.find_all("img", attrs={"class":"rg_i Q4LuWd"})

for idx, image in enumerate(images):
    image_url = image["src"]
    
print(image_url)