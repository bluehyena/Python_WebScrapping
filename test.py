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




url = "https://www.google.com/search?q=&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJg8yk6r7sAhUEA4gKHUI8ChoQ_AUoA3oECAsQBQ&biw=929&bih=886"

# image_num = int(input("저장할 이미지 갯수를 입력하세요 : "))

browser = webdriver.Chrome()
print(type(browser))
print(type(3))