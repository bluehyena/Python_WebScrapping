import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

#browse
browser.get("http://naver.com")

#login
elem = browser.find_element_by_class_name("link_login")
elem.click()

#id pw
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

#button click
browser.find_element_by_id("log.login").click()

time.sleep(3)

#
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#html info
print(browser.page_source)

browser.quit()